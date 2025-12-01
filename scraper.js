const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://www.69shuba.com/book/6418/';
const OUTPUT_DIR = './chapters';

// Create output directory if it doesn't exist
if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

async function scrapeChapters() {
    console.log('Starting browser...');
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

        console.log(`Loading main page: ${BASE_URL}`);
        await page.goto(BASE_URL, {
            waitUntil: 'networkidle',
            timeout: 30000
        });

        // Wait for the page to load
        await page.waitForTimeout(3000);

        // Try to find chapter links
        const chapterLinks = await page.evaluate(() => {
            const links = [];

            // Look for the specific pattern found in the HTML: li a[href*="/txt/6418/"]
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

        console.log(`Found ${chapterLinks.length} chapter links`);

        if (chapterLinks.length === 0) {
            console.log('No chapter links found. Let me check the page content...');
            const pageContent = await page.content();
            fs.writeFileSync('./page_content.html', pageContent);
            console.log('Page content saved to page_content.html for inspection');

            // Also save a screenshot to see what's on the page
            await page.screenshot({ path: 'page_screenshot.png', fullPage: true });
            console.log('Screenshot saved to page_screenshot.png');
            return;
        }

        // Process each chapter
        for (let i = 0; i < chapterLinks.length; i++) { // Scrape all chapters
            const chapter = chapterLinks[i];
            console.log(`Processing chapter ${i + 1}: ${chapter.title}`);

            try {
                // Make URL absolute if it's relative
                let chapterUrl = chapter.url;
                if (chapterUrl.startsWith('/')) {
                    chapterUrl = `https://www.69shuba.com${chapterUrl}`;
                }

                console.log(`Navigating to: ${chapterUrl}`);
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
                const fileName = `${String(i + 1).padStart(3, '0')}-${sanitizeFileName(chapter.title || chapterContent.title || `Chapter ${i + 1}`)}.md`;
                const filePath = path.join(OUTPUT_DIR, fileName);

                const markdown = `# ${chapterContent.title || chapter.title}

${chapterContent.content}
`;

                fs.writeFileSync(filePath, markdown, 'utf8');
                console.log(`Saved: ${fileName}`);

                // Add delay between requests
                await page.waitForTimeout(1000);

            } catch (error) {
                console.error(`Error processing chapter ${i + 1}:`, error.message);
            }
        }

    } catch (error) {
        console.error('Scraping error:', error);
    } finally {
        await browser.close();
    }
}

function sanitizeFileName(fileName) {
    return fileName.replace(/[<>:"/\\|?*]/g, '-').replace(/\s+/g, '-').substring(0, 100);
}

scrapeChapters().then(() => {
    console.log('Scraping completed!');
}).catch(error => {
    console.error('Scraping failed:', error);
});