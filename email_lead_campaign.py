from crewai import Task, Crew
from backlinker_types import Customer

import concurrent.futures

from agents.email_writter import get_email_writter
from agents.customer_researcher import get_customer_research_agent
from agents.company_web_researcher import get_company_web_researcher
from agents.backlinker_expert import get_backlinker_expert

# init defined the python env variables manually since the .env file was having issues
from init import init
init()

Email_writter = get_email_writter(Verbose=True)
Customer_researcher = get_customer_research_agent()
Company_researcher = get_company_web_researcher()
backlinker_expert = get_backlinker_expert()

daniel = Customer("daniel@nugbase.com", "COO", "Daniel Steigman", "https://nugbase.com", "https://pursuethepassion.com/why-are-you-passionate-about-global-health/", "Nugbase", "https://www.linkedin.com/in/nighttrek/")
jamie = Customer("jamie@carepatron.com", "CEO", "Jamie Frew", "https://www.carepatron.com", "https://pursuethepassion.com/why-are-you-passionate-about-global-health/", "Carepatron", "https://www.linkedin.com/in/jamie-frew-b843618")


def generate_lead_email_tasks(customer = jamie):
    return [
        Task(
            description=f"""Search the internet for information and Research the customer's role at their company and what their company does. Look into their current SEO strategy and identify areas where https://www.backlinker.ai/ could help optimize it. 
                Customer details:
                    - Name: {customer.name} 
                    - Position: {customer.position}
                    - Email: {customer.email}
                    - Business name: {customer.business_name}
                    - Website: {customer.website} 
                    - Existing backlink: {customer.existing_backlink_url}
                    - LinkedIn profile: {customer.linkedin}""",
            expected_output="""A report and summary of who the customer is what their role in their company is and anything found about the persons history along with citations.""",
            agent=Customer_researcher,
            
        ),
        Task(
            description=f"""Read the research reports from the customer and company research agents and provide advice on how to sell this specific customer about the backlinker product.""",
            expected_output="""A bullet point list of advice on how this specific customer could benefit from the backlinker service and what the backlinker product can do for them.""",
            agent=backlinker_expert,
        ),
        Task(
            description=f"""
                Read the research reports and the bullet list of advice from the product expert. Write a personalized sales email from Bennet Heyn, the CEO of backlinker.ai, to a potential customer to convince them to use the SEO product https://www.backlinker.ai/.
                Customer details:
                    - Name: {customer.name} 
                    - Position: {customer.position}
                    - Email: {customer.email}
                    - Business name: {customer.business_name}
                    - Website: {customer.website} 
                    - Existing backlink: {customer.existing_backlink_url}
                    - LinkedIn profile: {customer.linkedin}""",
            expected_output="""A personalized email ptching a customer to use backlinker.ai to increase their SEO. The email should be from Bennett heyn the CEO of backlinker.ai.""",
            agent=Email_writter,
            output_file=f"./email_leads_output/email_{customer.email}.txt"
        )
    ]

def sequential_lead_processing(customers = [jamie, daniel]):
    for customer in customers:
        tasks = generate_lead_email_tasks(customer)
        Lead_generation_crew = Crew(
            name=f"Lead Generation Crew for {customer.email}",
            agents=[Customer_researcher, backlinker_expert, Email_writter],
            tasks=tasks,
            verbose=True,
        )
        Lead_generation_crew.kickoff()



def multi_threaded_crew_runner(customers = [jamie, daniel], num_threads = 4):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for customer in customers:
            tasks = generate_lead_email_tasks(customer)
            Lead_generation_crew = Crew(
                name=f"Lead Generation Crew for {customer.email}",
                agents=[Customer_researcher, backlinker_expert, Email_writter],
                tasks=tasks,
                verbose=True,
            )
            futures.append(executor.submit(Lead_generation_crew.kickoff))
        
        for future in concurrent.futures.as_completed(futures):
            future.result()


sequential_lead_processing()