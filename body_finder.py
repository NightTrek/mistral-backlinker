from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.headless = True  # Enable headless mode
    # Automatically manage firefoxdriver
    # Set the path to the GeckoDriver executable
    gecko_driver_path = "/usr/local/bin/geckodriver"

    driver = webdriver.Firefox(service=Service(executable_path=gecko_driver_path), options=options)
    return driver

def get_cleaned_html(url):
    driver = setup_driver()
    try:
        # Navigate to the URL
        driver.get(url)
        # Get the page source
        page_source = driver.page_source
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(page_source, "html.parser")
        # Find the body tag
        body = soup.find('body')
        # Remove specific tags by decomposing them
        for tag in body.find_all(["script", "head", "link"]):
            tag.decompose()
        # Iterate over all tags to clean up attributes
        for tag in body.find_all(True):
            attrs_to_keep = {}
            # For <a> tags, keep the href attribute
            if tag.name == "a" and tag.has_attr("href"):
                attrs_to_keep["href"] = tag["href"]
            # For <img> tags, keep the alt attribute
            if tag.name == "img" and tag.has_attr("alt"):
                attrs_to_keep["alt"] = tag["alt"]
            # For any tag, if it has a title attribute, keep it
            if tag.has_attr("title"):
                attrs_to_keep["title"] = tag["title"]
            # Update the tag's attributes to only keep the ones we want
            tag.attrs = attrs_to_keep
        # Return the prettified HTML of the body
        return body.prettify()
    finally:
        driver.quit()
