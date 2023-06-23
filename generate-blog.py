import os
import markdown
from pathlib import Path

src_dir = Path('blog')
dest_dir = Path('dist/blog')

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

for src_file in src_dir.glob('*.md'):
    # Read Markdown file
    with open(src_file, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert to HTML
    html_text = markdown.markdown(md_text)

    # Write to HTML file in destination directory
    dest_file = dest_dir / src_file.with_suffix('.html').name
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(html_text)

print("Conversion completed successfully.")
