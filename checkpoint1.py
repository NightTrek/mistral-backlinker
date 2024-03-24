from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import pandas as pd
import re
import urllib.parse



def get_phone(response_text):
    phone = re.search(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response_text)
    return phone.group(0) if phone else 'Phone number not found'

def get_email(response_text):
    email = re.search(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response_text)
    return email.group(0) if email else 'Email not found'

def extract_and_process_links(driver, base_url):
    driver.get(base_url)
    links = driver.find_elements("css selector", "a[href]")
    base_domain = urllib.parse.urlparse(base_url).netloc  # Extract the domain of the base URL
    results = []
    for link in links:
        href = link.get_attribute('href')
        link_domain = urllib.parse.urlparse(href).netloc  # Extract the domain of each found link
        # Check if the link domain is different from the base domain and not a LinkedIn URL
        if href and link_domain != base_domain and "linkedin.com" not in href and "twitter.com" not in href and "pinterest.com" not in href and "featured.com" not in href:
            results.append(href)
    return results


def setup_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def process_website(driver, url):
    try:
        driver.get(url)
        response_text = driver.page_source
        phone = get_phone(response_text)
        email = get_email(response_text)

        print(f'Processed {url}:') 
        print(f'Phone: {phone}, Email: {email}\n')
        return {'Website': url, 'Phone': phone, 'Email': email}
    except WebDriverException as e:
        print(f"Error accessing {url}: {e}")
        return None

# Setup Selenium WebDriver
driver = setup_driver()

# Load initial URLs from CSV
initial_urls_df = pd.read_csv('initial_urls.csv')
print("Loaded URLs:", initial_urls_df['Website'].tolist())

results = []

for _, row in initial_urls_df.iterrows():
    initial_url = row['Website']
    external_links = extract_and_process_links(driver, initial_url)
    print(f"Found {len(external_links)} external links from {initial_url}")
    
    for link in external_links:
        result = process_website(driver, link)
        if result:
            results.append(result)
            results_df = pd.DataFrame(results)
            results_df.to_csv('output_partial2.csv', index=False)

driver.quit()



# Save results
results_df = pd.DataFrame(results)
results_df.to_csv('output.csv', index=False)
