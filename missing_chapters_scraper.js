const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://www.69shuba.com/book/6418/';
const OUTPUT_DIR = './chapters';

// Read missing chapters from the file
const missingChapters = fs.readFileSync('missing_chapters.txt', 'utf8')
    .split('\n')
    .filter(line => line.trim())
    .map(num => parseInt(num));

console.log(`Found ${missingChapters.length} missing chapters to scrape`);

async function scrapeMissingChapters() {
    console.log('Starting browser for missing chapters...');
    const browser = await chromium.launch({
        headless: true,
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        ]
    });

    try {
        const context = await browser.newContext({
            userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            extraHTTPHeaders: {
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
        });
        const page = await context.newPage();

        // First, load the main page to get the chapter list
        console.log(`Loading main page: ${BASE_URL}`);
        await page.goto(BASE_URL, {
            waitUntil: 'networkidle',
            timeout: 30000
        });

        await page.waitForTimeout(3000);

        // Get all chapter links
        const chapterLinks = await page.evaluate(() => {
            const links = [];
            const elements = document.querySelectorAll('li a[href*="/txt/6418/"]');
            elements.forEach(el => {
                const href = el.getAttribute('href');
                const text = el.textContent.trim();
                if (href && text) {
                    links.push({
                        url: href,
                        title: text
                    });
                }
            });
            return links;
        });

        console.log(`Found ${chapterLinks.length} total chapter links`);

        // Process only missing chapters
        for (let i = 0; i < missingChapters.length; i++) {
            const chapterNum = missingChapters[i];
            const chapterIndex = chapterNum - 1; // Convert to 0-based index

            if (chapterIndex >= chapterLinks.length) {
                console.log(`Chapter ${chapterNum} not found in chapter list`);
                continue;
            }

            const chapter = chapterLinks[chapterIndex];
            console.log(`Processing missing chapter ${chapterNum}: ${chapter.title}`);

            // Check if file already exists
            const fileName = `${String(chapterNum).padStart(3, '0')}-${sanitizeFileName(chapter.title)}.md`;
            const filePath = path.join(OUTPUT_DIR, fileName);

            if (fs.existsSync(filePath)) {
                console.log(`  Chapter ${chapterNum} already exists, skipping...`);
                continue;
            }

            try {
                // Make URL absolute if it's relative
                let chapterUrl = chapter.url;
                if (chapterUrl.startsWith('/')) {
                    chapterUrl = `https://www.69shuba.com${chapterUrl}`;
                }

                console.log(`  Navigating to: ${chapterUrl}`);
                await page.goto(chapterUrl, {
                    waitUntil: 'networkidle',
                    timeout: 30000
                });

                await page.waitForTimeout(2000);

                // Extract chapter content
                const chapterContent = await page.evaluate(() => {
                    let content = '';
                    let title = '';

                    // Get content from the .txtnav div, but exclude navigation and ads
                    const contentElement = document.querySelector('.txtnav');
                    if (contentElement) {
                        // Clone the element to manipulate it
                        const clone = contentElement.cloneNode(true);

                        // Remove unwanted elements
                        const unwantedSelectors = [
                            '.tools',
                            '.bread',
                            '#txtright',
                            '.bottom-ad',
                            'script',
                            'iframe',
                            'h3.mytitle',
                            '.txtinfo'
                        ];

                        unwantedSelectors.forEach(selector => {
                            const elements = clone.querySelectorAll(selector);
                            elements.forEach(el => el.remove());
                        });

                        content = clone.textContent.trim();
                    }

                    // Try to find title
                    const titleSelectors = [
                        'h1',
                        '.chapter-title',
                        '.title',
                        'h2',
                        '.readTitle'
                    ];

                    for (const selector of titleSelectors) {
                        const element = document.querySelector(selector);
                        if (element) {
                            title = element.textContent.trim();
                            break;
                        }
                    }

                    return { title, content };
                });

                // Create markdown file
                const markdown = `# ${chapterContent.title || chapter.title}

${chapterContent.content}
`;

                fs.writeFileSync(filePath, markdown, 'utf8');
                console.log(`  Saved: ${fileName}`);

                // Add delay between requests
                await page.waitForTimeout(1000);

            } catch (error) {
                console.error(`  Error processing chapter ${chapterNum}:`, error.message);
                // Add longer delay after errors
                await page.waitForTimeout(3000);
            }

            // Progress update
            if ((i + 1) % 50 === 0) {
                console.log(`Progress: ${i + 1}/${missingChapters.length} missing chapters processed`);
            }
        }

        console.log('Missing chapters scraping completed!');

    } catch (error) {
        console.error('Scraping error:', error);
    } finally {
        await browser.close();
    }
}

function sanitizeFileName(fileName) {
    return fileName.replace(/[<>:"/\\|?*]/g, '-').replace(/\s+/g, '-').substring(0, 100);
}

scrapeMissingChapters().then(() => {
    console.log('Missing chapters scraping completed!');
}).catch(error => {
    console.error('Missing chapters scraping failed:', error);
});