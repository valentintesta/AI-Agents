# 📊 Warren Buffett-Style Value Investing App

This application provides AI-assisted valuation reports for publicly traded companies, modeled after **Warren Buffett’s value investing philosophy**.  
It combines **financial APIs**, **large language models (via Groq)**, and **CrewAI agents** to deliver structured executive memos on intrinsic value using both **Owner Earnings** and **Discounted Cash Flow (DCF)** methods.

---

## 🚀 Features

- 🔍 **Stock Evaluation**  
  Input a stock ticker and fetch historical financials.

- 🤖 **AI Financial Agents**
  - **Owner Earnings Valuator**: Estimates intrinsic value using Buffett’s preferred method.
  - **DCF Valuator**: Projects future cash flows to derive a valuation.
  - **Executive Summary Editor**: Crafts a polished investment memo in Buffett’s tone.

- 📂 **Document-Aware Memos**  
  Aligns tone and structure with past reports stored locally.

- 🧠 **Multiple LLMs**  
  Uses powerful Groq-hosted models to ensure performance and style control.

---

## 🧠 How It Works

### 🔄 Data Fetching
- Financial data is retrieved using the `FinancialDatasetsAPIWrapper`.

### 🧑‍💼 Agent Roles
- Each agent is fine-tuned for a specific financial task and communication style.
- Agents are powered by adapted tools including:
  - File reading
  - Directory scanning
  - Web search

### 👥 Crew Execution
- Tasks are assigned per agent:
  - Owner earnings valuation
  - DCF analysis
  - Executive memo synthesis
- Output is a final structured investment memo designed for executive audiences.

---

## 💡 Inspired By

- **Warren Buffett's principles** on value investing  
- **CrewAI** for agent/task coordination  
- **Groq** for lightning-fast LLM inference  
- **FinancialDatasets API** for real-time data  

---

> 📌 *This app aims to blend the best of Buffett-style value investing with the speed and reasoning of AI agents.*

