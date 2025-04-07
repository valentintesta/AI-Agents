# 📈 Investment Portfolio Risk Assessment AI Agent

## 🌟 Project Overview

An AI-powered investment analysis tool that leverages investment portfolio agent that provide comprehensive portfolio insights. This intelligent agent helps investors make data-driven decisions by offering deep portfolio risk assessment, stock profiling, and personalized recommendations.

## 🏗️ Key Features
- **Stock Risk Profiling**: Detailed risk assessment for individual stocks, including volatility, market cap, and return potential.
- **Portfolio Diversification Analysis**: Breakdown of sector allocation and risk levels within a given portfolio. 
- **Expected Return Calculation**: Estimation of annual returns based on historical stock performance.
- **Intelligent Portfolio Adjustments**: Personalized recommendations aligned with user's risk tolerance.
- **Interactive Web Interface**: User-friendly Streamlit application for easy interaction with the AI agent.

## 👨‍🏫 How Crew AI- Agent works

The Investment Portfolio Analysis AI Agent is built on the ReAct (Reasoning and Action) framework, which combines the strength of large language models with a structured approach to problem-solving. Here's the workflow:

1. **Thought**: The agent analyzes the user's query and formulates a plan of action.
2. **Action**: Based on the thought, the agent selects and executes an appropriate tool or API call.
3. **Observation**: The agent observes and interprets the results of the action.
4. **Repeat**: This cycle continues until the agent has gathered enough information to provide a comprehensive answer.

### Extension to Tool Calling

The framework can be extended to incorporate specialized tools:

- **Tool Definition**: Each tool (e.g., stock risk profiler, portfolio analyzer) is defined with clear inputs and outputs.
- **Tool Selection**: The agent learns to choose the most appropriate tool based on the current context and user query.
- **Tool Execution**: The selected tool is called with the necessary parameters.
- **Result Integration**: The agent incorporates tool outputs into its reasoning process for the final response.

This extension allows the agent to leverage specific financial analysis functions while maintaining a flexible, language-model-driven interaction flow.

## 🚀 Technologies Used

- **Backend**: Python
- **AI Model**: Groq API
- **Frontend**: Streamlit
- **Key Libraries**:
  - Groq
  - python-dotenv
  - Logging
  - JSON processing
  - Dataclasses



### Example Queries
- "Get risk profile for NVDA stock"
- "Analyze a portfolio with 40% AAPL, 30% GOOGL, 30% SPY"
- "Calculate expected return for a portfolio"
- "Recommend adjustments for a portfolio with specific risk tolerance"

## 📊 How It Works

The AI agent uses a ReAct (Reasoning and Acting) framework to:
1. Understand the user's investment query
2. Choose appropriate financial analysis tools
3. Generate data-driven insights and recommendations

### Key Components
- **FinancialTools**: Comprehensive analysis methods
- **Agent**: Intelligent interaction and tool selection
- **Streamlit Interface**: User-friendly web application

