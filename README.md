# Lead Extractor and Contact Info Finder

## Overview

This Python script is designed for scraping websites listed in a CSV file to extract contact information (phone numbers and emails) and generate leads. The script uses Selenium WebDriver for browsing and scraping web pages. It performs the following main functions:

1. Setup Selenium WebDriver: Initializes a headless Chrome browser for automated navigation through web pages.
2. Load URLs: Reads a list of URLs from a CSV file named articles.csv.
3. Extract and Process Links: For each URL, it extracts external links that do not belong to social media or specified domains and gathers contact information from these links.
4. Extract Leads: Utilizes custom modules (body_finder and lead_extraction) to clean up HTML content and extract leads, which are then outputted in JSON format.
5. Save Results: The extracted contact information and leads are saved into CSV files for further processing or analysis.

The script is efficient in filtering out irrelevant links and focuses on extracting valuable leads and contact information, making it a powerful tool for digital marketing and sales prospecting.

## Setup Instructions

Ensure you have Python 3 and pip installed on your system. This script is built and tested with Python 3.8+.

1. Install python requirements
```
pip install -r requirements.txt
```
2. Prepare the `articles.csv`

The script expects a CSV file named articles.csv in the script directory, containing a column Website with URLs to process.


## Running Instructions

```
python3 full_email_export.py
```

## Example outputs
1. Extract quoted experts (leads) and their contact info from articles:
```
{
  "https://bulldogdigitalmedia.co.uk/": {
    "name": "Georgia O’Brien-Perry",
    "position": "Digital PR Manager",
    "linkedin": "https://www.linkedin.com/in/georgia-obrien-perry",
    "businessName": "Bulldog Digital Media"
  },
  "https://www.lydiabagarozza.com/": {
    "name": "Lydia Bagarozza",
    "position": "Publicist",
    "linkedin": "https://www.linkedin.com/in/lydia-bagarozza-9212b180",
    "businessName": "Lydia Bagarozza LLC"
  },
  "https://www.novakidschool.com/": {
    "name": "Dominique Harmse",
    "position": "PR Manager",
    "linkedin": "https://www.linkedin.com/in/dominique-harmse",
    "businessName": "Novakid"
  },
  "https://www.emich.edu": {
    "name": "Brittany Mobley",
    "position": "Senior Media Relations Specialist",
    "linkedin": "https://www.linkedin.com/in/brittanyemobley",
    "businessName": "Eastern Michigan University"
  }
}
```
