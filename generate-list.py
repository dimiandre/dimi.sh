from html.parser import HTMLParser
import os
import datetime
import re

from html.parser import HTMLParser

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.recording = 0
        self.data = ''
        self.first_paragraph_found = False

    def handle_starttag(self, tag, attrs):
        if tag == 'p' and not self.first_paragraph_found:
            self.recording += 1

    def handle_endtag(self, tag):
        if tag == 'p' and self.recording:
            self.recording -= 1
            self.first_paragraph_found = True

    def handle_data(self, data):
        if self.recording and not self.first_paragraph_found:
            self.data = data

def get_date_from_filename(filename):
    # Remove the file extension and split the components
    parts = filename.replace(".html", "").split("-")
    
    # First four components should be year, month, day
    year = int(parts[0])
    month = int(parts[1])
    day = int(parts[2])

    return datetime.date(year, month, day)

def get_title_from_filename(filename):
    # Remove the file extension and split the components
    parts = filename.replace(".html", "").split("-")

    # All components after the first four form the title
    title = " ".join(parts[3:])

    return title.capitalize()

def get_first_paragraph_from_file(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    parser = MyHTMLParser()
    parser.feed(content)
    return parser.data

def generate_blog_list():
    # List all files in the blog directory
    files = os.listdir("dist/blog")

    # Filter out non-HTML files
    files = [f for f in files if f.endswith(".html")]

    # Sort the files by date, newest first
    files.sort(key=get_date_from_filename, reverse=True)

    blog_list_html = ""

    for filename in files:
        date = get_date_from_filename(filename)
        title = get_title_from_filename(filename)
        first_paragraph = get_first_paragraph_from_file(f"dist/blog/{filename}")

        blog_list_html += f"""
        <div class="post">
            <span class="date">{date.strftime('%B %d, %Y')}</span>
            <h2><a href="/blog/{filename}" class="post-link">{title}</a></h2>
            <p>{first_paragraph}</p>
        </div>
        """

    return blog_list_html

if __name__ == "__main__":
    blog_list_html = generate_blog_list()

    with open("dist/index.html", "r") as file:
        content = file.read()

    content = re.sub('<!--BLOG_LIST_START-->.*<!--BLOG_LIST_END-->', f'<!--BLOG_LIST_START-->{blog_list_html}<!--BLOG_LIST_END-->', content, flags=re.DOTALL)

    with open("dist/index.html", "w") as file:
        file.write(content)
