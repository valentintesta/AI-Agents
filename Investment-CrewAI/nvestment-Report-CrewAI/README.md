# 📊 Stock Analysis Toolkit – Crew AI

This project is a modular and extensible toolkit for analyzing individual stocks using a combination of **fundamental metrics**, **technical indicators**, and **risk analytics**. It pulls data from **Yahoo Finance via `yfinance`**, processes it using **Pandas** and **NumPy**, and optionally serves insights through a **Streamlit dashboard**. The toolkit is designed for integration with **LLM agents via `CrewAI` and `ChatGroq`**, enabling automated reasoning and reporting.

---

## 🧩 1. Data Collection

- **Real-Time and Historical Data**  
  Stock data is fetched using `yfinance`, including daily historical prices, financial statements, and key company info.
  
- **News Scraper**  
  Retrieves relevant stock news headlines from `yfinance.Ticker.news`.

---

## 📈 2. Fundamental Analysis

- **Valuation Metrics**
  - Price-to-Earnings Ratio (PE)
  - Forward PE
  - Price-to-Book (PB)
  - Enterprise Value-to-EBITDA (EV/EBITDA)

- **Profitability**
  - EPS (ttm)
  - Return on Equity (ROE)
  - Net Margin
  - Gross Margin
  - Free Cash Flow

- **Growth**
  - Revenue and earnings growth trends
  - Year-over-year comparisons

---

## 📉 3. Risk Analysis

- **Volatility**  
  Standard deviation of log returns.

- **Value at Risk (VaR)**  
  Uses historical simulation to estimate the potential daily loss at a given confidence level.

- **Sharpe & Sortino Ratios**  
  Evaluate risk-adjusted return with/without penalizing upside volatility.

- **Beta Calculation**  
  Estimates the stock’s sensitivity to market movement.

- **Max Drawdown**  
  Measures the largest historical peak-to-trough drop.

---

## 📊 4. Technical Indicators

- **Moving Averages**  
  Simple and exponential MAs to assess trends.

- **Momentum**
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)

- **Trend Detection**  
  Classifies trend as bullish, bearish, or neutral using moving average crossovers.

---

## 🧠 5. LLM & Agent Integration

- **ChatGroq + LLaMA 3 (70B)**  
  The code integrates with Groq-hosted LLaMA 3 for fast, context-aware analysis using `ChatGroq`.

- **CrewAI-Ready**  
  Designed to be used with multi-agent frameworks like CrewAI. Each function can serve as a tool for reasoning agents in financial report generation, portfolio evaluation, or conversational workflows.

---

## 🛠️ 6. Utilities & Structure

- Modular functions for:
  - Trend classification
  - Ratio formatting
  - Data preprocessing

- Easily extendable with new indicators or output formats (e.g., PDF reporting, chatbot UI).
