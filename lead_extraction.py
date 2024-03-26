from openai import OpenAI
import os
import json

from init import init
init()

default_prompt = """
I provided you with the pure HTML of a website. The website is an article that is centered around a topic and has experts provide quotes to provide their opinions on the topics. There are usually several experts that are usually quoted with their Names, Positions, and Websites/Businesses. These experts usually have outbound links to their linkedin and or company website.

I will provide you with a list of all the ahref links from the website as well as the pure HTML for the page.

I want you to return a JSON object where the keys are the website urls and the values are objects containing information like Name of the expert it's associated with, their position if applicable, their business name if applicable, and their linkedIn website if applicable.
{
    name: string (required), position: string (required), linkedin: string (required), business_name: string (required), website_url: string (required)
        
}

Please only return website URLs that are directly associated with experts mentioned on the webpage. All other website urls are irrelevant and can be excluded from the json object.



https://www.amazon.com/Pursue-Passion-Brett-Farmiloe/dp/0615283608/ref=sr_1_3?ie=UTF8&qid=1504122781&sr=8-3&keywords=pursue+the+passion
https://www.amazon.com/Pursue-Passion-Brett-Farmiloe/dp/0615283608/ref=sr_1_3?ie=UTF8&qid=1504122781&sr=8-3&keywords=pursue+the+passion
https://www.co.walworth.wi.us/
https://www.carepatron.com/
https://www.promed-dme.com/
https://samfullerplasticsurgery.com/
https://www.saudepulso.com.br/
https://superbee.me/
https://www.facebook.com/pursuethepassion
https://www.amazon.com/Pursue-Passion-Brett-Farmiloe/dp/0615283608/ref=sr_1_3?ie=UTF8&qid=1504122781&sr=8-3&keywords=pursue+the+passion
https://www.amazon.com/Pursue-Passion-Brett-Farmiloe/dp/0615283608/ref=sr_1_3?ie=UTF8&qid=1504122781&sr=8-3&keywords=pursue+the+passion
https://bulldogdigitalmedia.co.uk/
https://www.lydiabagarozza.com/
https://www.novakidschool.com/
https://www.emich.edu/

Do this without writing any code. I just want you to look at the HTML of the website and logically infer the related experts from the websites if they exist. Some links obviously won't have an expert associated with it. In that case, skip.
"""


def extract_leads_from_html(html_content):
    oai = OpenAI(
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_API_BASE"],
    )

    chatResponse = oai.chat.completions.create(
            model=os.environ["OPENAI_MODEL_NAME"],
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": default_prompt + html_content + """ Return only the JSON object with no explanation or extra text. 
            {
                name: string (required),
                position: string (required),
                linkedin: string (required),
                business_name: string (required),
                website_url: string (required)
                 
            }
                 """,}
            ],
            
            response_format={ "type": "json_object" },
            temperature=0.4,
            max_tokens=32000,
        )
    print(chatResponse)
    response = chatResponse.choices[0].message.content
    try:
        json_data = json.dumps(response)
        return json_data
    except json.JSONDecodeError:
        print(f"Invalid JSON response: {response}")
