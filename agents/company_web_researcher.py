from crewai import Agent
from crewai_tools import WebsiteSearchTool

web_rag_tool = WebsiteSearchTool()


def get_company_web_researcher():
    return Agent(
        role="Company_researcher",
        goal="Identify information about customers company using the company website to help write personalzied sales emails",
        backstory="""You are an expert is customer research and SEO. You are really good at identifing details about customers business including What the buisness sells information about their products and the industry their business works in.""",
        tools=[web_rag_tool],
    )


# example task
        # Task(
        #     description=f"""Look into the customers company website and research what the company does and what their SEO strategy is. Identify who their primary customer profile is what their product or service does and what their competitors are.
        #         Customer details:
        #             - Name: {customer.name} 
        #             - Position: {customer.position}
        #             - Email: {customer.email}
        #             - Business name: {customer.business_name}
        #             - Website: {customer.website} 
        #             - Existing backlink: {customer.existing_backlink_url}
        #             - LinkedIn profile: {customer.linkedin}""",
        #     expected_output="""A report and summary of the company who their customers are and what the compay does along with citations.""",
        #     agent=Company_researcher,
        # ),