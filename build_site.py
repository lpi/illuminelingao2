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

try:
    from ebooklib import epub
except ImportError:
    print("Error: 'ebooklib' library not found. Please run: pip install ebooklib")
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
    <header>
        <a href="{root_path}index.html" class="site-title">Illumine Lingao (English Translation)</a>
        <div class="header-links">
            <a href="https://github.com/lpi/illuminelingao2" class="github-btn">📚 GitHub</a>
            <a href="https://discord.gg/69ryTJuXZN" class="discord-btn">💬 Discord</a>
        </div>
    </header>
    <div class="container">
        {content}
    </div>
</body>
</html>
"""

NAV_TEMPLATE = """
<div class="chapter-nav">
    {prev_link}
    <a href="index.html">{volume_name} Index</a>
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

def get_volume_display_name(vol_dir_name):
    """Extract a clean volume name like 'Volume 6' from directory name."""
    # Handle special folder names
    if vol_dir_name == '00-preface':
        return 'Preface'
    if vol_dir_name == 'extras':
        return 'Extras'
    
    title = clean_title(vol_dir_name)
    # Try to extract volume number and name
    match = re.match(r'(\d+)\s*(.*)', vol_dir_name)
    if match:
        vol_num = int(match.group(1))
        vol_name = match.group(2).replace('_', ' ').replace('-', ' ').strip()
        if vol_name:
            return f"Volume {vol_num}: {vol_name.title()}"
        return f"Volume {vol_num}"
    return title

def get_chapter_title_from_content(md_content, fallback_title):
    """Extract chapter title from the first line of markdown content.
    
    Expects format like: # Chapter 1275: Chemical Talk on the Commuter Train
    Returns the title without the leading '# ' prefix.
    """
    lines = md_content.strip().split('\n')
    if lines:
        first_line = lines[0].strip()
        # Check if it's a markdown header
        if first_line.startswith('# '):
            return first_line[2:].strip()
        elif first_line.startswith('#'):
            return first_line[1:].strip()
    return fallback_title

def generate_css():
    css_content = """
/* Radial gradient background with blue/purple vignette effect */
body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    color: #333;
    margin: 0;
    padding: 0;
    background: radial-gradient(ellipse at center, #e8f0ff 0%, #b8c8e8 60%, #8898c8 100%);
    min-height: 100vh;
}

/* Persistent header bar */
header {
    background-color: #e0e0e0;
    padding: 10px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #ccc;
}

.site-title {
    font-size: 1.3em;
    font-weight: bold;
    color: #333;
    text-decoration: none;
}

.site-title:hover {
    text-decoration: underline;
}

.header-links {
    display: flex;
    gap: 10px;
}

.github-btn {
    background-color: #333;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9em;
}

.github-btn:hover {
    background-color: #555;
}

.discord-btn {
    background-color: #5865F2;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9em;
}

.discord-btn:hover {
    background-color: #4752C4;
}

/* Main content container with white background and blue glow */
.container {
    max-width: 800px;
    margin: 30px auto;
    padding: 30px 40px;
    background-color: #fff;
    box-shadow: 0 0 40px rgba(100, 120, 180, 0.4);
    min-height: calc(100vh - 150px);
}

/* Typography */
h1 {
    font-size: 1.8em;
    margin-bottom: 20px;
    color: #333;
}

h2 {
    font-size: 1.4em;
    margin-bottom: 15px;
    color: #333;
}

/* Standard blue links */
a {
    color: #0000EE;
    text-decoration: underline;
}

a:visited {
    color: #551A8B;
}

a:hover {
    color: #0000EE;
}

/* Yellow disclaimer box */
.disclaimer {
    background-color: #FFF8DC;
    border: 1px solid #DDD8BC;
    padding: 15px;
    margin: 20px 0;
    font-size: 0.9em;
    line-height: 1.5;
}

/* Homepage links section */
.home-links {
    text-align: center;
    margin-bottom: 20px;
}

.home-links a {
    margin: 0 10px;
}

/* Volume list on homepage */
.volume-list {
    margin-top: 20px;
}

.volume-list a {
    display: block;
    margin: 8px 0;
    font-size: 1.1em;
}

/* Chapter list on volume pages */
.chapter-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.chapter-list li {
    margin: 4px 0;
}

.chapter-list a {
    font-size: 0.95em;
}

/* Chapter navigation bar */
.chapter-nav {
    background-color: #f0f0f0;
    padding: 8px 15px;
    margin-bottom: 20px;
    text-align: center;
    border: 1px solid #ddd;
}

.chapter-nav a {
    margin: 0 15px;
}

/* Chapter content */
.content {
    text-align: left;
}

.content p {
    margin-bottom: 1em;
    text-align: justify;
}

/* Back link styling */
.back-link {
    margin-top: 30px;
    display: block;
}
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
        # Skip hidden directories, "unresolved", "characters" (empty), and "extras" (added at end)
        if os.path.isdir(vol_path) and not entry.startswith('.') and entry not in ('unresolved', 'characters', 'extras'):
            volumes.append(entry)
    
    # Add extras folder at the end if it exists
    extras_path = os.path.join(SOURCE_DIR, 'extras')
    if os.path.exists(extras_path) and os.path.isdir(extras_path):
        volumes.append('extras')

    # Build a global ordered list of all chapters for cross-volume navigation
    # Each entry: (vol_dir_name, chapter_filename, chapter_html_path_from_root)
    global_chapter_list = []
    for vol_dir_name in volumes:
        vol_source_path = os.path.join(SOURCE_DIR, vol_dir_name)
        chapters = sorted([f for f in os.listdir(vol_source_path) if f.endswith('.md')])
        for chapter_filename in chapters:
            chapter_html_filename = os.path.splitext(chapter_filename)[0] + ".html"
            global_chapter_list.append((vol_dir_name, chapter_filename, f"{vol_dir_name}/{chapter_html_filename}"))

    # Build main index (homepage)
    main_index_content = """<h1>Illumine Lingao</h1>
<div class="home-links">
    <a href="downloads/illuminelingao.epub">Download EPUB</a>
    <a href="https://github.com/lpi/illuminelingao2">GitHub Repository</a>
    <a href="https://discord.gg/69ryTJuXZN">Join Discord</a>
</div>
<div class="disclaimer">
    Disclaimer: This is an unofficial fan translation of the Chinese original novel "临高启明" (Illumine Lingao) by 吹牛者 (Boaster). The translations were generated using Opus 4.5.<br><br>
    You can read the original Chinese version <a href="https://lgqm.halu.lu/">here</a>.
</div>
<div class="volume-list">
"""

    global_idx = 0  # Track position in global chapter list
    
    for vol_dir_name in volumes:
        vol_display_name = get_volume_display_name(vol_dir_name)
        vol_output_dir = os.path.join(OUTPUT_DIR, vol_dir_name)
        os.makedirs(vol_output_dir)
        
        main_index_content += f'<a href="{vol_dir_name}/index.html">{vol_display_name}</a>\n'

        # Process chapters within volume
        vol_source_path = os.path.join(SOURCE_DIR, vol_dir_name)
        chapters = sorted([f for f in os.listdir(vol_source_path) if f.endswith('.md')])
        
        # Volume index page
        vol_index_content = f"<h1>{vol_display_name}</h1>\n<ul class='chapter-list'>\n"
        
        for i, chapter_filename in enumerate(chapters):
            chapter_html_filename = os.path.splitext(chapter_filename)[0] + ".html"
            
            # Generate Chapter Page
            in_file_path = os.path.join(vol_source_path, chapter_filename)
            out_file_path = os.path.join(vol_output_dir, chapter_html_filename)
            
            with codecs.open(in_file_path, 'r', 'utf-8') as f:
                md_content = f.read()
            
            # Extract title from markdown content (first line), fallback to filename
            fallback_title = clean_title(chapter_filename)
            chapter_title = get_chapter_title_from_content(md_content, fallback_title)
                
            html_body = markdown.markdown(md_content)
            
            # Navigation - use global chapter list for cross-volume nav
            prev_link = ""
            if global_idx > 0:
                prev_vol, prev_file, prev_path = global_chapter_list[global_idx - 1]
                # If same volume, use relative link; otherwise use ../ path
                if prev_vol == vol_dir_name:
                    prev_href = os.path.splitext(prev_file)[0] + ".html"
                else:
                    prev_href = "../" + prev_path
                prev_link = f'<a href="{prev_href}">« Previous</a>'
            
            next_link = ""
            if global_idx < len(global_chapter_list) - 1:
                next_vol, next_file, next_path = global_chapter_list[global_idx + 1]
                # If same volume, use relative link; otherwise use ../ path
                if next_vol == vol_dir_name:
                    next_href = os.path.splitext(next_file)[0] + ".html"
                else:
                    next_href = "../" + next_path
                next_link = f'<a href="{next_href}">Next »</a>'
            
            global_idx += 1
            
            # Get short volume name for nav bar (e.g., "Volume 6")
            vol_short_name = get_volume_display_name(vol_dir_name).split(':')[0]
            
            nav_html = NAV_TEMPLATE.format(
                prev_link=prev_link,
                next_link=next_link,
                volume_name=vol_short_name
            )
            
            full_page = HTML_TEMPLATE.format(
                title=chapter_title + " - Illumine Lingao",
                root_path="../",
                content=f"{nav_html}<div class='content'>{html_body}</div>{nav_html}"
            )
            
            with open(out_file_path, 'w', encoding='utf-8') as f:
                f.write(full_page)
            
            # Add to Volume Index
            vol_index_content += f"<li><a href='{chapter_html_filename}'>{chapter_title}</a></li>\n"

        vol_index_content += "</ul>\n"
        vol_index_content += '<a href="../index.html" class="back-link">« Back to Main Index</a>'
        
        with open(os.path.join(vol_output_dir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(HTML_TEMPLATE.format(
                title=vol_display_name + " - Illumine Lingao",
                root_path="../",
                content=vol_index_content
            ))
            
    main_index_content += "</div>\n"
    
    with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(HTML_TEMPLATE.format(
            title="Illumine Lingao - English Translation",
            root_path="./",
            content=main_index_content
        ))

    print(f"Site generated successfully in '{OUTPUT_DIR}'")
    
    # Generate EPUB
    generate_epub(volumes)

def generate_epub(volumes):
    """Generate EPUB file from all chapters."""
    book = epub.EpubBook()
    
    # Set metadata
    book.set_identifier('illumine-lingao-en')
    book.set_title('Illumine Lingao (English Translation)')
    book.set_language('en')
    book.add_author('吹牛者 (Boaster)')
    book.add_metadata('DC', 'description', 'An unofficial fan translation of the Chinese novel 临高启明')
    
    # CSS for EPUB
    epub_css = '''
    body { font-family: Georgia, serif; line-height: 1.6; }
    h1 { font-size: 1.5em; margin-bottom: 1em; }
    h2 { font-size: 1.3em; margin-bottom: 0.8em; }
    p { margin-bottom: 0.8em; text-align: justify; }
    '''
    css_item = epub.EpubItem(uid="style", file_name="style/main.css", media_type="text/css", content=epub_css)
    book.add_item(css_item)
    
    all_chapters = []
    toc = []
    
    for vol_dir_name in volumes:
        vol_display_name = get_volume_display_name(vol_dir_name)
        vol_source_path = os.path.join(SOURCE_DIR, vol_dir_name)
        chapter_files = sorted([f for f in os.listdir(vol_source_path) if f.endswith('.md')])
        
        vol_chapters = []
        
        for chapter_filename in chapter_files:
            in_file_path = os.path.join(vol_source_path, chapter_filename)
            
            with codecs.open(in_file_path, 'r', 'utf-8') as f:
                md_content = f.read()
            
            fallback_title = clean_title(chapter_filename)
            chapter_title = get_chapter_title_from_content(md_content, fallback_title)
            
            # Convert markdown to HTML
            html_body = markdown.markdown(md_content)
            
            # Create EPUB chapter
            chapter_id = os.path.splitext(chapter_filename)[0]
            epub_chapter = epub.EpubHtml(
                title=chapter_title,
                file_name=f'{vol_dir_name}/{chapter_id}.xhtml',
                lang='en'
            )
            epub_chapter.content = f'<html><body>{html_body}</body></html>'
            epub_chapter.add_item(css_item)
            
            book.add_item(epub_chapter)
            all_chapters.append(epub_chapter)
            vol_chapters.append(epub_chapter)
        
        # Add volume section to TOC
        if vol_chapters:
            toc.append((epub.Section(vol_display_name), vol_chapters))
    
    # Set TOC and spine
    book.toc = toc
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    book.spine = ['nav'] + all_chapters
    
    # Create downloads directory
    downloads_dir = os.path.join(OUTPUT_DIR, 'downloads')
    os.makedirs(downloads_dir, exist_ok=True)
    
    # Write EPUB
    epub_path = os.path.join(downloads_dir, 'illuminelingao.epub')
    epub.write_epub(epub_path, book, {})
    print(f"EPUB generated: {epub_path}")

if __name__ == "__main__":
    main()
