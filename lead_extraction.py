import json

def extract_leads_from_html(html_string):
    leads = {}
    json_object = json.dumps(leads, indent=4)
    print(json_object)
    return json_object
