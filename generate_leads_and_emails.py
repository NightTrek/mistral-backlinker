from backlinker_types import Customer
from full_email_export import generate_leads_from_csv
from email_lead_campaign import sequential_lead_processing
import json

print("Going through the list of websites and extracting the leads")

# # step one generate the leads using full_email_export.py
generate_leads_from_csv()




# step two load the json file output.json 
customers = []
with open('output.json') as f:
    data = json.load(f)
    for key in data:
        value = data[key]
        backlinkInfo = json.loads(value)
        for website in backlinkInfo:
            customerInfo = backlinkInfo[website]
            customers.append(
                Customer(
                    name=customerInfo.get('name', 'None'),
                    position=customerInfo.get('position', 'None'),
                    business_name=customerInfo.get('business_name', 'None'),
                    website=website,
                    existing_backlink_url=key,
                    email=customerInfo.get('email', 'None'),
                    linkedin=customerInfo.get('linkedin', 'None'),
                    
                )
            )


print("====================================================")
print("Writing outreach emails")
print(f"Generating emails for {len(customers)} customers")


sequential_lead_processing(customers)