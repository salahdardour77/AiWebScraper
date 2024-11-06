import string

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service


def scrape_website(website):
    print("Connecting to Scraping Browser...")

    # Set up Firefox options (similar to Chrome options)
    options = FirefoxOptions()
    options.headless = True  # Run in headless mode if needed

    # Initialize Firefox WebDriver instead of Chrome
    driver_path = "./geckodriver.exe"
    service = Service(executable_path=driver_path)
    driver = Firefox(service=service, options=options)

    try:
        driver.get(website)
        print("Navigated! Scraping page content...")

        # Retrieve and return the page source
        html = driver.page_source
        return html

    finally:
        # Ensure the browser is closed
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_content(content: str) -> str:
    clean_string = ''.join(c for c in content if c not in string.punctuation and c != '\n')
    return clean_string


def split_content(dom_content: str, max_length: int) -> list:
    return [dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)]

