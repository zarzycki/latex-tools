const puppeteer = require('puppeteer');

(async () => {
    // Check if a filename has been provided
    if (process.argv.length !== 3) {
        console.error("Usage: node countwords.js <filename>");
        process.exit(1);
    }

    const filename = process.argv[2];

    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Load the local HTML file using the filename from the command line.
    await page.goto(`file://${__dirname}/${filename}`);

    // Evaluate script on the page
    const wordCount = await page.evaluate(() => {
        const bodyText = document.body.innerText;
        return bodyText.split(/\s+/).filter(Boolean).length;
    });

    console.log(`Rendered Word Count: ${wordCount}`);

    await browser.close();
})();