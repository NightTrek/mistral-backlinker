# Lead Extractor and Contact Info Finder

## Overview


This Python script is part of our lead generation toolkit designed to scrape contact information (phone numbers and emails) from websites listed in a CSV file. Our toolkit utilizes Selenium WebDriver for browsing and web page scraping, but it has been expanded with additional capabilities.

Now, this set of tools includes the following components:

1. Scraper: A script that uses Selenium WebDriver to navigate websites and extract required contact information.
2. Parser (Mistral): Our parser processes website HTML using Mistral and produces structured JSON objects for each lead.
3. Research Agents: A set of agents that research each lead, gathering additional information about their industry, company size, and potential needs.
4. Pitch Advisors: Agents that advise on the best way to pitch our Backlinker product based on the gathered data.
5. Email Writers: Agents that use the researched info and sales advice to write personalized emails as the CEO of Backlinker.

We're constantly improving our tools, so stay tuned for more updates!

The script is efficient in filtering out irrelevant links and focuses on extracting valuable leads and contact information, making it a powerful tool for digital marketing and sales prospecting.

## Setup Instructions

Ensure you have Python 3 and pip installed on your system. This script is built and tested with Python 3.8+.

1. Install python requirements

```
pip install -r requirements.txt
```

2. Prepare the `articles.csv`


The script expects a CSV file named articles.csv in the script directory, containing a column Website with URLs to process.

3. install the GeckoDriver and put it in your path

The default expected instal location is 
```
/usr/local/bin/geckodriver
```

you can find the driver (here)[https://github.com/mozilla/geckodriver/releases]

## Running Instructions

```
python3 generate_leads_and_emails.py
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

## Agent generated emails

The agents are responsible for writing personalized emails to the leads based on the research they've done. 
They automatically output each of the emails into the email_leads_output folder. You can see some examples aditional examples there

Sample Output:

```
Subject: Grow Your Healthcare Business with Backlinker.ai

Dear Jamie,

My name is Bennett Heyn, and I'm the Co-Founder and CEO of Backlinker.ai. I came across your impressive work at Carepatron and wanted to reach out about how our SEO services could benefit your healthcare technology business.

As the Co-Founder and CEO yourself, I know you're laser-focused on growing Carepatron and expanding your reach in the healthcare industry. With your background in psychology and business, and your passion for mental health and wellness, I believe Backlinker.ai can be a valuable partner in achieving your goals.

Our AI-powered link building platform specializes in generating high-quality, relevant backlinks from authoritative websites in the healthcare space. By leveraging Carepatron's existing backlink from PursueThePassion.com, we can further boost your domain authority and search engine visibility - making it easier for healthcare providers to find and convert on your industry-leading practice management software.

Beyond just link building, our team can work with you to develop a content strategy that positions Carepatron as a thought leader on topics related to mental health, self-care, and the future of healthcare technology. This will not only attract new customers, but also help you retain and expand relationships with your existing client base.

I'd welcome the opportunity to discuss how Backlinker.ai can support Carepatron's growth objectives. Please let me know if you have any availability for a quick call in the coming days.

I look forward to connecting.

Best regards,
Bennett Heyn
Co-Founder & CEO, Backlinker.ai
```