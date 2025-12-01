const { chromium } = require('playwright');

async function testChapterPage() {
    const browser = await chromium.launch({ headless: false });
    const context = await browser.newContext({
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    });
    const page = await context.newPage();

    try {
        const chapterUrl = 'https://www.69shuba.com/txt/6418/3767219';
        console.log(`Loading chapter page: ${chapterUrl}`);

        await page.goto(chapterUrl, {
            waitUntil: 'networkidle',
            timeout: 30000
        });

        await page.waitForTimeout(3000);

        // Save the page content
        const content = await page.content();
        require('fs').writeFileSync('./chapter_page_content.html', content);

        // Take a screenshot
        await page.screenshot({ path: 'chapter_page_screenshot.png', fullPage: true });

        console.log('Chapter page content saved to chapter_page_content.html');
        console.log('Screenshot saved to chapter_page_screenshot.png');

        // Try to find content with different selectors
        console.log('\nTesting different content selectors:');
        const selectors = [
            '.content',
            '.chapter-content',
            '.text-content',
            '#content',
            '.read-content',
            'article',
            '.novel-content',
            '.txt',
            '.text',
            '.reads',
            '#reads',
            '.chapter'
        ];

        for (const selector of selectors) {
            const element = await page.$(selector);
            if (element) {
                const text = await element.textContent();
                console.log(`✓ Found selector "${selector}" with ${text.length} characters`);
                if (text.length > 100) {
                    console.log(`  First 200 chars: ${text.substring(0, 200)}...`);
                }
            } else {
                console.log(`✗ No element found for selector "${selector}"`);
            }
        }

        await page.waitForTimeout(5000);

    } catch (error) {
        console.error('Error:', error);
    } finally {
        await browser.close();
    }
}

testChapterPage();