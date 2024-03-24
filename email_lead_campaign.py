from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, WebsiteSearchTool
from backlinker_types import Customer

google_search = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

Customer_Reasercher = Agent(
    role="Customer_researcher",
    goal="Identify information about customers to help write personalzied sales emails",
    backstory="""You are an expert is customer research and SEO.
    You are really good at identifing personal details about customers including their role at their company. You are great at reading websites about your customer to identify information about their SEO strategy.
    You are great at reading their company website to identify what their company does.""",
    tools=[google_search],
    # llm=large,
)

company_researcher = Agent(
    role="Company_researcher",
    goal="Identify information about customers company using the company website to help write personalzied sales emails",
    backstory="""You are an expert is customer research and SEO. You are really good at identifing details about customers business including What the buisness sells information about their products and the industry their business works in.""",
    tools=[web_rag_tool],
    
)


Email_writter  = Agent(
    role="Lead Generation Email Writter",
    goal="Write personalized emails based on user research",
    backstory="""You are Bennett Heyn. You Scale businesses through strategic analysis and backlinks. Currently a Full time Business Analyst at Adobe. Co-Founder at Backlinker. Helping websites build authority backlinks with reporter outreach.
 You are a internet sales expert with lots of experience doing outreach and lead generation. You love using researchers to give you personal information about the customer to help write more personalized emails.
    You enjoy using information about the customers SEO strategy and personal success to sell the product. You write emails from yourself to customers to make them more likely to use your product.""",
    allow_delegation=True,
    verbose=True,
    # llm=large,
)


BacklinkAI_Expert = Agent(
    role="Product expert",
    goal="Inform other Agents about the https://www.backlinker.ai/ product and answer their questions. Help write emails that include accurate details about the product",
    backstory=""" YOu are an expert in backlinker AI and SEO strategy. We use the power of AI to automate your reporter outreach. Get more organic traffic & backlinker with no additional effort from your. We manage the process end-to-end. Clients Results
We generate, on average, nearly 150 quotes per month for our clients depending on the categories and niches they are focused on, and get backlinks to reputable sites (examples below).
DR 91 Backlink
zdnet.com
DR 91 Backlink
aol.com
DR 90 Backlink
lifewire.com
DR 84 Backlink
cmswire.com
DR 84 Backlink
marketingsherpa.com
DR 84 Backlink
familyhandyman.com
DR 82 Backlink
gobankingrates.com
DR 77 Backlink
techbullion.com
____
Provide Your Name, Website, Bio, & other info
Just give us your info so that we can set up an account for you. This information will be included in the emails so that reporters can credit the quote to your name and give your website a backlink.

Our AI assistant will craft quality pitches to earn backlinks

More than 50+ AI pitches sent per month

____ 
We Gather Reporter Quote Requests and Use AI To Match Your Bio To Relevant Queries
AI determines which queries are relevant to your bio and then we will respond to relevant pitches

If your bio is more general it will reply to more queries

Great Bios often lead to better pitch categorization and generation

Responding to relevant pitches leads to more backlinks
_____
AI Will Create Pitches For You & Submit Them For Requests
Our powerful AI system will generate thoughtful, technical responses and send pitches on your behalf.

Our AI assistant will craft quality pitches to earn backlinks

Anywhere from 50-300+ AI emails sent per month

Emails are sent with time delay to avoid suspicion

__
How Is This Better Than Other Services
We've talked with people who have spent $1000+ per month on link building companies and our service is:
- Cheaper
- Our AI-enabled system can reply to more requests
- Completely hands off for you
- You can see all pitches we submit on your behalf
""",
# llm=small,
)



daniel = Customer("daniel@nugbase.com", "COO", "Daniel Steigman", "https://nugbase.com", "https://pursuethepassion.com/why-are-you-passionate-about-global-health/", "Nugbase", "https://www.linkedin.com/in/nighttrek/")
jamie = Customer("jamie@carepatron.com", "CEO", "Jamie Frew", "https://www.carepatron.com", "https://pursuethepassion.com/why-are-you-passionate-about-global-health/", "Carepatron", "https://www.linkedin.com/in/jamie-frew-b843618")


def build_task_list(customers = [daniel, jamie]):
    task_list = []
    for customer in customers:
        task_list.append(Task(
            description=f"""Write a personalized sales email from Bennet Heyn, the CEO of backlinker.ai, to a potential customer to convince them to use the SEO product https://www.backlinker.ai/.

                        Customer details:
                        - Name: {customer.name} 
                        - Position: {customer.position}
                        - Email: {customer.email}
                        - Business name: {customer.business_name}
                        - Website: {customer.website} 
                        - Existing backlink: {customer.existing_backlink_url}
                        - LinkedIn profile: {customer.linkedin}

                        Step 1 Ask query the Research Agent
                        Instructions:
                        Identify more details about the customer's role at their company and what their company does. Look into their current SEO strategy and identify areas where https://www.backlinker.ai/ could help optimize it. Provide this information to be used in the email.

                        Step 2 query the Product Expert Agent
                        Instructions: 
                        Using the customer details and information from the Research Agent, provide an initial draft of the sales email. Explain how https://www.backlinker.ai/ can optimize their SEO strategy for a fraction of the cost. Personalize the pitch based on the customer's specific needs and how the product can improve their system.
                        Step 3: Write the firs draft of the email.

                        Step 4: ask the product expert to review the draft email and provide advice and additional product details to further personalize and strengthen the sales pitch before submitting the final email.
                        Step 5 based on the product expert's feedback, revise the email to finish the sales email.

                        """,
            expected_output="""A personalized email ptching a customer to use backlinker.ai to increase their SEO. The email should be from Bennett heyn the CEO of backlinker.ai.""",
            agent=Email_writter,
            output_file=f"./email_leads_output/email_task_{customer.email}",
        ))

    return task_list
 
# Here is the existing quote we found when we about you
# summorize their business 
#

Lead_generation_crew = Crew(
    name="Lead Generation Crew",
    agents=[Customer_Reasercher, company_researcher, Email_writter, BacklinkAI_Expert],
    tasks=build_task_list(),
    verbose=2,
)

Lead_generation_crew.kickoff()