import os
import shutil
import re
import codecs

# Try importing markdown, if not available, we might need to rely on basic text processing or ask user to install it.
try:
    import markdown
except ImportError:
    print("Error: 'markdown' library not found. Please run: pip install markdown")
    exit(1)

SOURCE_DIR = "english_chapters"
OUTPUT_DIR = "public"
CSS_FILE = "style.css"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="{root_path}style.css">
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

NAV_TEMPLATE = """
<div class="navigation">
    {prev_link}
    <a href="index.html" class="nav-btn">Volume Index</a>
    {next_link}
</div>
"""

def clean_title(filename):
    # Remove numbering like "001-" or "01-" and extension
    name = os.path.splitext(filename)[0]
    # Replace underscores and hyphens with spaces
    name = name.replace('_', ' ').replace('-', ' ')
    # Try to clean up leading numbers "001 Chapter..." -> "Chapter..."
    match = re.match(r'^\d+\s*(.*)', name)
    if match:
        return match.group(1)
    return name

def generate_css():
    css_content = """
body {
    font-family: 'Georgia', 'Times New Roman', serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    min-height: 100vh;
}

h1, h2, h3 {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    color: #2c3e50;
}

h1 {
    text-align: center;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

a {
    color: #3498db;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.chapter-list {
    list-style: none;
    padding: 0;
}

.chapter-list li {
    margin: 10px 0;
    border-bottom: 1px solid #eee;
}

.chapter-list a {
    display: block;
    padding: 10px;
    font-size: 1.1em;
}

.chapter-list a:hover {
    background-color: #f9f9f9;
    text-decoration: none;
}

.navigation {
    display: flex;
    justify-content: space-between;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #eee;
}

.nav-btn {
    display: inline-block;
    padding: 8px 16px;
    background-color: #3498db;
    color: white;
    border-radius: 4px;
    font-family: sans-serif;
    font-size: 0.9em;
}

.nav-btn:hover {
    background-color: #2980b9;
    text-decoration: none;
    color: white;
}

.volume-list {
    display: grid;
    gap: 20px;
}

.volume-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    transition: transform 0.2s;
}

.volume-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.volume-card h2 {
    margin-top: 0;
}

/* Markdown Content Styling */
.content p {
    margin-bottom: 1.2em;
    text-indent: 0;
}

/* Chinese-style paragraph spacing if needed, but English usually prefers margin-bottom */
"""
    with open(os.path.join(OUTPUT_DIR, CSS_FILE), 'w') as f:
        f.write(css_content)

def main():
    if not os.path.exists(SOURCE_DIR):
        print(f"Source directory '{SOURCE_DIR}' not found.")
        return

    # Clean and recreate output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    generate_css()

    volumes = []
    
    # Walk through source directory 
    # Valid volumes should be 01-..., 02-..., etc.
    entries = sorted(os.listdir(SOURCE_DIR))
    
    for entry in entries:
        vol_path = os.path.join(SOURCE_DIR, entry)
        if os.path.isdir(vol_path) and not entry.startswith('.'):
            volumes.append(entry)

    main_index_content = "<h1>Illumine Lingao - English Translation</h1>\n<div class='volume-list'>"

    for vol_dir_name in volumes:
        vol_title = clean_title(vol_dir_name)
        vol_output_dir = os.path.join(OUTPUT_DIR, vol_dir_name)
        os.makedirs(vol_output_dir)
        
        main_index_content += f"""
        <div class="volume-card">
            <h2><a href="{vol_dir_name}/index.html">{vol_title}</a></h2>
        </div>
        """

        # Process chapters within volume
        vol_source_path = os.path.join(SOURCE_DIR, vol_dir_name)
        chapters = sorted([f for f in os.listdir(vol_source_path) if f.endswith('.md')])
        
        vol_index_content = f"<h1>{vol_title}</h1>\n<ul class='chapter-list'>"
        
        for i, chapter_filename in enumerate(chapters):
            chapter_title = clean_title(chapter_filename)
            chapter_html_filename = os.path.splitext(chapter_filename)[0] + ".html"
            
            # Generate Chapter Page
            in_file_path = os.path.join(vol_source_path, chapter_filename)
            out_file_path = os.path.join(vol_output_dir, chapter_html_filename)
            
            with codecs.open(in_file_path, 'r', 'utf-8') as f:
                md_content = f.read()
                
            html_body = markdown.markdown(md_content)
            
            # Navigation
            prev_link = ""
            if i > 0:
                prev_file = os.path.splitext(chapters[i-1])[0] + ".html"
                prev_link = f'<a href="{prev_file}" class="nav-btn">← Previous</a>'
            
            next_link = ""
            if i < len(chapters) - 1:
                next_file = os.path.splitext(chapters[i+1])[0] + ".html"
                next_link = f'<a href="{next_file}" class="nav-btn">Next →</a>'
            
            nav_html = NAV_TEMPLATE.format(
                prev_link=prev_link,
                next_link=next_link
            )
            
            full_page = HTML_TEMPLATE.format(
                title=chapter_title,
                root_path="../",
                content=f"<div class='content'>{html_body}</div>{nav_html}"
            )
            
            with open(out_file_path, 'w', encoding='utf-8') as f:
                f.write(full_page)
            
            # Add to Volume Index
            vol_index_content += f"<li><a href='{chapter_html_filename}'>{chapter_title}</a></li>"

        vol_index_content += "</ul>"
        vol_index_content += f'<div style="margin-top: 30px;"><a href="../index.html" class="nav-btn">← Back to Main Index</a></div>'
        
        with open(os.path.join(vol_output_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(HTML_TEMPLATE.format(
                title=vol_title,
                root_path="../",
                content=vol_index_content
            ))
            
    main_index_content += "</div>"
    
    with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(HTML_TEMPLATE.format(
            title="Illumine Lingao",
            root_path="./",
            content=main_index_content
        ))

    print(f"Site generated successfully in '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()
