from langchain_community.agent_toolkits.financial_datasets.toolkit import FinancialDatasetsToolkit
from langchain_community.utilities.financial_datasets import FinancialDatasetsAPIWrapper
from langchain_core.tools import Tool
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool
import os
import requests
import streamlit as st
from langchain_groq import ChatGroq
from crewai import Agent, Task, Crew

# Set your API keys
os.environ["FINANCIAL_DATASETS_API_KEY"] = "8b969e06-4ac0-4785-b4b6-b174729b5d35"
os.environ["GROQ_API_KEY"] = "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"

# Groq models
model1 = ChatGroq(model="groq/llama-3.3-70b-versatile", temperature=0.4)
model2 = ChatGroq(model="groq/deepseek-r1-distill-llama-70b", temperature=0.8)

# Initialize wrapper and toolkit
api_wrapper = FinancialDatasetsAPIWrapper(
    financial_datasets_api_key=os.environ["FINANCIAL_DATASETS_API_KEY"]
)
toolkit = FinancialDatasetsToolkit(api_wrapper=api_wrapper)

# Adapt tools for CrewAI
def adapt_tools_for_crewai(tools):
    valid_tools = []
    for tool in tools:
        if isinstance(tool, Tool):
            valid_tools.append(tool)
        elif isinstance(tool, dict) and all(k in tool for k in ["name", "description", "func"]):
            valid_tools.append(tool)
    return valid_tools

adapted_tools = adapt_tools_for_crewai(toolkit.get_tools())

# Extra tools
extra_tools = [
    DirectoryReadTool(directory=r'C:\\Users\\valen\\OneDrive\\Desktop\\DATA APP\\Agent AI\\Warren-Buffet-Agent\\sample'),
    FileReadTool(),
    SerperDevTool()
]

# Manual API request setup to fetch financials
def get_financials(ticker, period='annual', limit=100, start_date='2020-01-01', end_date='2024-01-01'):
    headers = {
        "X-API-KEY": os.environ["FINANCIAL_DATASETS_API_KEY"]
    }
    url = (
        f'https://api.financialdatasets.ai/financials/'
        f'?ticker={ticker}'
        f'&period={period}'
        f'&limit={limit}'
        f'&report_period_lte={end_date}'
        f'&report_period_gte={start_date}'
    )
    response = requests.get(url, headers=headers)
    return response.json().get('financials')

# Streamlit app interface
st.set_page_config(page_title="Value Investing App", layout="wide")
st.title("📊 Warren Buffett-Style Value Investing App")


st.markdown("Enter a stock ticker (e.g., AAPL, MSFT, NVDA) to evaluate its intrinsic value using Owner Earnings and DCF methods.")

ticker = st.text_input("Ticker symbol:", value="AAPL")

if ticker:
    st.subheader(f"Financial data for {ticker}")
    with st.spinner("Fetching financial data..."):
        financial_data = get_financials(ticker)
    if financial_data:
        st.success("Data fetched successfully!")
        if isinstance(financial_data, list):
            st.json(financial_data[:5])
        else:
            st.json(financial_data)
    else:
        st.error("No financial data found or an error occurred.")

# Agents
owner_earnings_valuator = Agent(
    role="Owner Earnings Valuator",
    goal="Generate a concise summary of the company's intrinsic value based on the owner earnings method.",
    backstory=(
        "You are a financial analyst influenced by Warren Buffett’s thinking. "
        "You focus on real cash flows available to shareholders and explain your findings briefly and clearly "
        "for executive audiences with no unnecessary technical depth."
    ),
    tools=adapted_tools,
    llm=model1,
    verbose=True
)

dcf_valuator = Agent(
    role="Discounted Cash Flow (DCF) Valuator",
    goal="Provide a high-level summary of the company's intrinsic value using the DCF method.",
    backstory=(
        "You are a valuation expert who communicates future cash flow projections in a simple, digestible way. "
        "Avoid going deep into formulas — focus on clarity and what matters for decision-making."
    ),
    tools=adapted_tools,
    llm=model1,
    verbose=True
)

investment_memo_editor = Agent(
    role="Executive Summary Editor",
    goal=(
        "Craft concise, structured Executive Summaries inspired by Warren Buffett’s memo style, "
        "based on valuation outputs and aligned with company samples."
    ),
    backstory=(
        "You are a seasoned financial communicator and value investor. "
        "You specialize in writing short, impactful executive memos. "
        "Your task is to synthesize valuation findings into a clear summary, using "
        "prior samples stored at 'C:\\Users\\valen\\OneDrive\\Desktop\\DATA APP\\Agent AI\\Warren-Buffet-Agent\\sample' to match tone, format, and depth. "
        "Start the memo with a short introduction: company name, business model, and customer persona. "
        "Avoid excessive detail—focus on clarity and investment logic."
    ),
    tools=extra_tools,
    llm=model2,
    verbose=True
)

# Define Tasks
def define_tasks(ticker):
    owner_earnings_task = Task(
        description=f"Calculate the intrinsic value of {ticker} using the owner earnings method.",
        expected_output="Short summary Owner earnings-based valuation.",
        agent=owner_earnings_valuator
    )

    dcf_valuation_task = Task(
        description=f"Estimate the intrinsic value of {ticker} using the Discounted Cash Flow (DCF) method, do an analysis but don't go too deep.",
        expected_output="DCF valuation short summary result.",
        agent=dcf_valuator
    )

    memo_editorial_task = Task(
        description=(
            f"Write a short executive summary for {ticker} using the tone, structure, and depth of previous memos stored in "
            f"'C:\\Users\\valen\\OneDrive\\Desktop\\DATA APP\\Agent AI\\Warren-Buffet-Agent\\sample'. The memo must include:\n"
            f"1. A brief summary (2–3 lines) of the owner earnings valuation\n"
            f"2. A brief summary (2–3 lines) of the DCF valuation\n"
            f"3. A final investment recommendation in plain, confident language\n\n"
            f"The output should be clear, professional, and under 300 words. Match the formatting of prior reports. "
            f"Don't overexplain or go too technical. Prioritize clarity and investor logic."
        ),
        expected_output="Concise and well-formatted executive summary memo aligned with previous writing style.",
        agent=investment_memo_editor
    )

    return [owner_earnings_task, dcf_valuation_task, memo_editorial_task]

# Create Crew
def create_valuation_crew(ticker):
    tasks = define_tasks(ticker)
    agents = [owner_earnings_valuator, dcf_valuator, investment_memo_editor]
    return Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

# Run Crew when button is clicked
if ticker:
    if st.button("Run Valuation Report"):
        st.subheader("Generating Executive Memo...")
        valuation_crew = create_valuation_crew(ticker)

        with st.spinner("Running agents and compiling insights..."):
            report = valuation_crew.kickoff()

        if report:
            st.success("Executive Summary Generated")
            st.markdown("---")
            st.markdown(report)
        else:
            st.error("No result returned by the crew.")
