import sys
from selenium import webdriver
from bs4 import BeautifulSoup
import re

def main():
    # Check if a filename has been provided
    if len(sys.argv) != 2:
        print("Usage: python sel.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=chrome_options)  # For Chrome

    # Load the local HTML file using the filename from the command line.
    driver.get(f'file://{filename}')

    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Replace non-breaking spaces with regular spaces
    text = soup.get_text(separator=' ', strip=True).replace(u'\xa0', ' ')

    # Remove punctuation (except for hyphens and apostrophes)
    text = re.sub(r'[^\w\s-]', '', text)

    # Condense multiple spaces into one
    text = ' '.join(text.split())

    # Count words
    word_count = len(text.split())

    print(f'Rendered Word Count: {word_count}')

    driver.quit()

if __name__ == "__main__":
    main()
