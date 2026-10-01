const { chromium } = require('playwright');
const fs = require('fs');

const BASE_URL = 'https://www.69shuba.com/book/6418/';
const KNOWN_COUNT = 2901; // chapters known locally as of last scrape

(async () => {
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
        await page.goto(BASE_URL, { waitUntil: 'networkidle', timeout: 30000 });
        await page.waitForTimeout(3000);

        const chapterLinks = await page.evaluate(() => {
            const links = [];
            const elements = document.querySelectorAll('li a[href*="/txt/6418/"]');
            elements.forEach(el => {
                const href = el.getAttribute('href');
                const text = el.textContent.trim();
                if (href && text) {
                    links.push({ url: href, title: text });
                }
            });
            return links;
        });

        console.log(`Site currently lists ${chapterLinks.length} chapters (local copy has ${KNOWN_COUNT})`);

        if (chapterLinks.length === 0) {
            fs.writeFileSync('./page_content.html', await page.content());
            console.log('No chapter links found — page content saved to page_content.html');
            return;
        }

        // Show last 5 known + all new chapters
        console.log('\nLast 5 chapters already known locally:');
        for (let i = Math.max(0, KNOWN_COUNT - 5); i < Math.min(KNOWN_COUNT, chapterLinks.length); i++) {
            console.log(`  ${i + 1}: ${chapterLinks[i].title}  (${chapterLinks[i].url})`);
        }

        if (chapterLinks.length > KNOWN_COUNT) {
            console.log(`\nNEW chapters (${chapterLinks.length - KNOWN_COUNT}):`);
            for (let i = KNOWN_COUNT; i < chapterLinks.length; i++) {
                console.log(`  ${i + 1}: ${chapterLinks[i].title}  (${chapterLinks[i].url})`);
            }
            // Save indices for the missing-chapters scraper
            const newIndices = [];
            for (let i = KNOWN_COUNT + 1; i <= chapterLinks.length; i++) newIndices.push(i);
            fs.writeFileSync('new_chapter_indices.txt', newIndices.join('\n') + '\n');
            console.log(`\nWrote ${newIndices.length} new chapter indices to new_chapter_indices.txt`);
        } else {
            console.log('\nNo new chapters found.');
        }

        // Also dump the full list for reference
        fs.writeFileSync('chapter_list_current.json', JSON.stringify(chapterLinks, null, 2));
        console.log('Full current chapter list saved to chapter_list_current.json');
    } catch (error) {
        console.error('Error:', error.message);
        process.exitCode = 1;
    } finally {
        await browser.close();
    }
})();
