# 📈 Automated Stock Monitoring & Alert System

A real-time stock alert system that analyzes market data and sends SMS alerts when significant price movements occur — powered by **Python**, **APIs**, and **automation**.

> 🚀 Built to streamline stock tracking for active investors and demonstrate end-to-end development of data-driven automation tools.

---

## 🔍 Overview

This system monitors daily closing prices of selected stocks and automatically:

- Detects significant price movements (e.g., >5%)
- Scrapes the latest related financial news
- Sends **real-time SMS alerts** with context using **Twilio**

---

## 🧰 Tech Stack

| Component         | Tools / APIs                        |
|------------------|-------------------------------------|
| Data Source       | Alpha Vantage API                  |
| News Integration  | NewsAPI                            |
| Alert Delivery    | Twilio (SMS)                       |
| Web Scraping      | BeautifulSoup, requests            |
| Automation        | Python scripting + scheduling (e.g. `schedule`, `cron`) |
| DevOps / Hosting  | Local / Cloud-ready (optional for deployment) |

---

## 💡 Key Features

- 📊 **Market Movement Detection**  
  Calculates percentage change in stock closing prices and flags major movements.

- 📰 **Live News Scraping**  
  Scrapes relevant financial headlines related to the flagged stock.

- 📱 **SMS Alerts**  
  Sends concise, informative messages to your phone with price delta and headlines.

- 🔁 **Fully Automated**  
  Set it and forget it — can run on a schedule or cloud deployment.

---

## ⚙️ How It Works

1. Fetch stock time series data from Alpha Vantage
2. Calculate daily price changes
3. If threshold exceeded (e.g. ±5%), trigger news fetch
4. Format and send SMS via Twilio

---

## 🚀 Getting Started

1. **Clone the Repo**
```bash
git clone https://github.com/JJama51657/stock-alert-system.git
cd stock-alert-system
