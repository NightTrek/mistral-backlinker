import json
import csv

# Open the JSON file and load the data
with open('output.json', 'r') as f:
    data = json.load(f)

# Create a list to store the customer data
customers = []

# Iterate through the JSON data and extract the customer information
for url, customer_data in data.items():
    customer = json.loads(customer_data)
    for customer_url, customer_info in customer.items():
        customer_row = {
            'name': customer_info['name'],
            'position': customer_info['position'],
            'linkedin': customer_info['linkedin'],
            'business_name': customer_info['business_name'],
            'website_url': customer_info['website_url']
        }
        customers.append(customer_row)

# Write the customer data to a CSV file
with open('output_leads.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'position', 'linkedin', 'business_name', 'website_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for customer in customers:
        writer.writerow(customer)