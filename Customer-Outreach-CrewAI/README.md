# Customer Outreach Campaign

This project implements an AI-powered customer outreach campaign system using CrewAI. It uses multiple AI agents to analyze potential leads and create personalized outreach messages.

## Requirements

- Python >= 3.10 and <= 3.13
- Required packages listed in `requirements.txt`

## Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `GROQ_MODEL_NAME`: The model to use (e.g., 'deepseek-r1-dist-llama-70b')
   - `OPENAI_API_TYPE`: Set to 'openai' to disable onnxruntime
   - `SERPER_API_KEY`: Your Serper API key

You can set these either in your environment or by creating a `.env` file in the project root.

4. Create an `instructions` directory in your project root to store any outreach templates or guidelines.

## Usage

You can use the customer outreach system in two ways:

1. Run the example campaign:
```bash
python customer_outreach.py
```

2. Import and use in your own code:
```python
from customer_outreach import run_campaign

result = run_campaign(
    lead_name="CompanyName",
    industry="Industry",
    key_decision_maker="Decision Maker Name",
    position="Position",
    milestone="Recent Milestone"
)
print(result)
```

## Features

- Lead profiling using AI
- Sentiment analysis for communication
- Personalized email draft generation
- Integration with search tools for lead research
- Customizable outreach templates

## Project Structure

- `customer_outreach.py`: Main implementation file
- `requirements.txt`: Project dependencies
- `instructions/`: Directory for outreach templates and guidelines
- `.env`: Environment variables (create this file) 