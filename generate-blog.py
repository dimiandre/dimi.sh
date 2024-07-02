import os
import markdown
from pathlib import Path
from datetime import datetime
from string import Template

src_dir = Path('blog')
dest_dir = Path('dist/blog')

# Read HTML template
with open('templates/blog_post.html', 'r', encoding='utf-8') as f:
    html_template = f.read()

html_template = Template(html_template)

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

for src_file in src_dir.glob('*.md'):
    # Read Markdown file
    with open(src_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert to HTML
    html_content = markdown.markdown(md_text)

    # Extract date and title from the file name
    parts = src_file.stem.split('-')
    date_str = '-'.join(parts[:3])  # Get the date part (first three elements after splitting by '-')
    title = ' '.join(parts[3:]).capitalize()  # Get the title part (the rest of the parts)
    date = datetime.strptime(date_str, "%Y-%m-%d").strftime('%B %d, %Y')

    # Generate the HTML file using the template
    html_text = html_template.substitute(
        title=title,
        date=date,
        content=html_content
    )

    # Write to HTML file in destination directory
    dest_file = dest_dir / src_file.with_suffix('.html').name
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(html_text)

print("Conversion completed successfully.")
