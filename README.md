# 临高启明 (Lingao Qiming) Web Scraper

A Node.js web scraper that extracts chapters from the Chinese web novel "临高启明" (Lingao Qiming) from 69shuba.com for offline reading.

## Overview

This project contains:
- **2,876 chapters** of the web serial "临高启明" (Lingao Qiming)
- Individual markdown files for each chapter
- Automated scraping tools using Playwright

## Project Structure

```
├── chapters/           # All novel chapters in markdown format
├── scraper.js          # Main scraper for all chapters
├── missing_chapters_scraper.js  # Scraper for missing chapters only
├── package.json        # Node.js dependencies
├── README.md          # This file
└── .gitignore         # Git ignore rules
```

## Novel Information

- **Title**: 临高启明 (Lingao Qiming)
- **Author**: 吹牛者 (Chuī Niú Zhě)
- **Genre**: 历史军事 (Historical Military)
- **Chapters**: 2,876
- **Source**: 69书吧 (69shuba.com)

## Features

- ✅ Complete chapter extraction with proper formatting
- ✅ Individual markdown files for easy epub conversion
- ✅ Error handling and retry logic
- ✅ Rate limiting to respect server limits
- ✅ Clean content extraction (ads and navigation removed)

## Setup

1. Install dependencies:
```bash
npm install
```

2. Run the scraper:
```bash
# Scrape all chapters
node scraper.js

# Scrape only missing chapters
node missing_chapters_scraper.js
```

## Chapter Files

Each chapter is saved as `XXX-chapter-title.md` where:
- `XXX` is the 3-digit chapter number
- `chapter-title` is the sanitized Chinese title

Example: `001-第1章-常师德对其指控的答辩.md`

## Usage for EPUB Creation

The markdown files can be easily converted to EPUB format using tools like:
- pandoc
- Calibre
- Custom markdown-to-epub converters

## Technical Details

- **Browser**: Playwright with Chromium
- **Content Extraction**: Custom CSS selectors targeting `.txtnav` elements
- **Rate Limiting**: 1-second delays between requests
- **Error Handling**: Network timeouts and retry logic
- **File Encoding**: UTF-8 for proper Chinese character support

## Status

- ✅ Scraping completed: 2,876 chapters
- ✅ Content verified: Full Chinese text with proper formatting
- ✅ File organization: Sequential numbering and consistent naming
- ✅ Git repository: Ready for version control

## License

This project is for personal use only. Please respect the original content creators and website terms of service.