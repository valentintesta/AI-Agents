import os
import warnings
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, DirectoryReadTool, FileReadTool
from langchain.tools import BaseTool
from langchain_openai import ChatOpenAI
from datetime import datetime

# Warning control
warnings.filterwarnings('ignore')

# Configure environment variables
os.environ['GROQ_API_KEY'] = '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'  # Replace with your actual key
os.environ['GROQ_MODEL_NAME'] = 'llama-3.3-70b-versatile'
os.environ['OPENAI_API_TYPE'] = 'openai'  # This disables onnxruntime
os.environ['SERPER_API_KEY'] = '0c0b8da9a9b6eb951d74e7899cde06541842a7d1'  # Replace with your actual key

# Configure the LLM
llm = ChatOpenAI(
    openai_api_key=os.environ['GROQ_API_KEY'],
    model=os.environ['GROQ_MODEL_NAME'],
    openai_api_base="https://api.groq.com/openai/v1",
    max_tokens=1024,
    temperature=0.5
)

# Create custom sentiment analysis tool
class SentimentAnalysisTool(BaseTool):
    name: str = "Sentiment Analysis Tool"
    description: str = ("Analyzes the sentiment of text "
         "to ensure positive and engaging communication.")

    def _run(self, argument: str) -> str:
        return "positive"

eReadTool()
sentiment_analysis_tool = SentimentAnalysisTool()# Initialize tools
serper_dev_tool = SerperDevTool()
directory_read_tool = DirectoryReadTool(directory='./instructions')
file_read_tool = Fil

# Create agents
sales_rep_agent = Agent(
    role="Sales Representative",
    goal="Identify high-value leads that match our ideal customer profile",
    backstory=(
        "As a member of the dynamic sales team at DevRev, your mission is to uncover high-value leads in the ever-evolving digital landscape. "
        "Equipped with cutting-edge AI tools and a deep understanding of customer needs, you analyze data, trends, and interactions to "
        "identify opportunities that can drive growth and improve customer experiences. "
        "With DevRev's AI-powered capabilities, you ensure that each lead aligns with the company's vision of transforming customer support and product development. "
        "Your role is pivotal in facilitating meaningful engagements and contributing to the company's mission of optimizing customer satisfaction and operational efficiency."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

lead_sales_rep_agent = Agent(
    role="Lead Sales Representative",
    goal="Nurture leads with personalized, compelling communications",
    backstory=(
        "As a key member of the DevRev sales team, you serve as the critical link between potential clients and the tailored solutions DevRev offers. "
        "By crafting engaging, personalized messages, you not only inform leads about the transformative power of DevRev's platform, "
        "but also make them feel understood and valued. "
        "Your role is essential in guiding leads through a journey from initial curiosity to active commitment, "
        "ensuring that every interaction fosters trust and excitement. "
        "With the power of AI-backed insights and a customer-centric approach, you elevate the sales experience, ensuring that each lead "
        "receives a highly relevant, compelling reason to engage with DevRev's innovative solutions."
    ),
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Create tasks
lead_profiling = Task(
    description=(
        "Conduct an in-depth analysis of {lead_name}, "
        "a company in the {industry} sector "
        "that recently showed interest in our solutions. "
        "Utilize all available data sources "
        "to compile a detailed profile, "
        "focusing on key decision-makers, recent business "
        "developments, and potential needs "
        "that align with our offerings. "
        "This task is crucial for tailoring "
        "our engagement strategy effectively.\n"
        "Don't make assumptions and "
        "only use information you absolutely sure about."
    ),
    expected_output=(
        "A comprehensive report on {lead_name}, "
        "including company background, "
        "key personnel, recent milestones, and identified needs. "
        "Highlight potential areas where "
        "our solutions can provide value, "
        "and suggest personalized engagement strategies."
    ),
    tools=[serper_dev_tool, file_read_tool],
    agent=sales_rep_agent
)

personalized_outreach_task = Task(
    description=(
        "Using the insights gathered from "
        "the lead profiling report on {lead_name}, "
        "craft a personalized outreach campaign "
        "aimed at {key_decision_maker}, "
        "the {position} of {lead_name}. "
        "The campaign should address their recent {milestone} "
        "and how our solutions can support their goals. "
        "Your communication must resonate "
        "with {lead_name}'s company culture and values, "
        "demonstrating a deep understanding of "
        "their business and needs.\n"
        "Don't make assumptions and only "
        "use information you absolutely sure about."
    ),
    expected_output=(
        "A series of personalized email drafts "
        "tailored to {lead_name}, "
        "specifically targeting {key_decision_maker}."
        "Each draft should include "
        "a compelling narrative that connects our solutions "
        "with their recent achievements and future goals. "
        "Ensure the tone is engaging, professional, "
        "and aligned with {lead_name}'s corporate identity."
    ),
    tools=[serper_dev_tool, sentiment_analysis_tool],
    agent=lead_sales_rep_agent
)

# Create crew
crew = Crew(
    tasks=[lead_profiling, personalized_outreach_task],
    agents=[sales_rep_agent, lead_sales_rep_agent],
    memory=True,
    verbose=2
)

def run_campaign(lead_name, industry, key_decision_maker, position, milestone):
    """
    Run the customer outreach campaign for a specific lead.
    
    Args:
        lead_name (str): Name of the target company
        industry (str): Industry sector of the company
        key_decision_maker (str): Name of the key decision maker
        position (str): Position of the key decision maker
        milestone (str): Recent milestone or achievement
        
    Returns:
        str: Campaign results
    """
    inputs = {
        "lead_name": lead_name,
        "industry": industry,
        "key_decision_maker": key_decision_maker,
        "position": position,
        "milestone": milestone
    }
    
    return crew.kickoff(inputs=inputs)

def save_to_markdown(result, lead_name):
    """
    Save campaign results to a markdown file.
    
    Args:
        result (str): The campaign results to save
        lead_name (str): Name of the lead company for the filename
    
    Returns:
        str: Path to the created markdown file
    """
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/campaign_report_{lead_name}_{timestamp}.md"
    
    # Create the markdown content
    markdown_content = f"""# Campaign Report for {lead_name}
Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{result}
"""
    
    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    return filename

if __name__ == "__main__":
    # Example usage
    lead_name = "DeepLearningAI"
    result = run_campaign(
        lead_name=lead_name,
        industry="Online Learning Platform",
        key_decision_maker="Andrew Ng",
        position="CEO",
        milestone="product launch"
    )
    
    # Save results to markdown file
    output_file = save_to_markdown(result, lead_name)
    print(f"Campaign report has been saved to: {output_file}")