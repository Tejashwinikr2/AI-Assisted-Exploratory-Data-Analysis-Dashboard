#AI-Assisted Exploratory Data **Analysis Dashboard**  
 [![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)  
 [![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)  
 [![Google Gemini](https://img.shields.io/badge/AI%20Model-Gemini%202.5%20Flash-4285F4?logo=google)](https://ai.google.dev/gemini-api)  
 [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
 
# AI-Driven Exploratory Data Analysis Dashboard

## Overview
An interactive dashboard that automates exploratory data analysis using AI. Upload a CSV and instantly get descriptive statistics, visual summaries, correlation maps, and plain-language observations generated with Google Gemini. The tool is designed for analysts, students, and non-technical users who want fast, interpretable EDA without writing code.

## Key Features
- **Instant Summaries:** Automatic column-level summaries and dataset statistics.  
- **Visualizations:** Histograms, box plots, scatter plots and correlation heatmaps to reveal distributions and relationships.  
- **AI Insights:** Natural-language interpretations of key metrics and notable patterns via the Google-GenAI SDK (Gemini).  
- **Multi-language Output:** Insight text can be rendered in multiple languages.  
- **File Upload:** Supports CSV uploads; easy-to-use UI for quick exploration.  
- **Extensible:** Modular codebase enables adding new charts, metrics or models.

## Why Use This
- **Saves time:** Automates repetitive EDA tasks and speeds up analysis.  
- **Beginner-friendly:** Useful for non-programmers who need immediate, dependable data summaries.  
- **Insightful:** Turns numeric results into actionable descriptions.  
- **Ready to extend:** Use as a baseline to add domain-specific checks or advanced models.

## Tech Stack
- **Language:** Python  
- **UI:** Streamlit  
- **Data:** pandas, numpy  
- **Visualizations:** matplotlib, seaborn  
- **AI:** Google-GenAI SDK (Gemini)  
- **Config:** python-dotenv for secure keys

## Installation
1. Clone the repo:
```bash
git clone https://github.com/<your-username>/AI-Assisted-Exploratory-Data-Analysis-Dashboard.git
cd AI-Assisted-Exploratory-Data-Analysis-Dashboard

2. Create a virtual environment and install:
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt

3. Configure API keys:
Copy .env.example to .env and add your Google API key / credentials.

4. Run:
streamlit run app.py

Screenshots:
<img width="1366" height="720" alt="Screenshot 2025-10-31 201635" src="https://github.com/user-attachments/assets/6f741543-5e3a-4c77-b91c-6ab26a19247e" />
<img width="1366" height="720" alt="Screenshot 2025-10-31 201726" src="https://github.com/user-attachments/assets/207f6567-bb29-41c8-a620-af417cce6bae" />
<img width="1366" height="720" alt="Screenshot 2025-10-31 201744" src="https://github.com/user-attachments/assets/df7be9f4-1898-481b-996e-234f592504b9" />
<img width="1366" height="720" alt="Screenshot 2025-10-31 202626" src="https://github.com/user-attachments/assets/96c3a624-dce4-437f-902c-7771f30d0b4a" />
<img width="1366" height="720" alt="Screenshot 2025-10-31 202746" src="https://github.com/user-attachments/assets/3f86c704-512a-4d29-92e5-f23c567be508" />

Requirements
streamlit>=1.38.0  
pandas>=2.2.0  
numpy>=1.26.0  
seaborn>=0.13.0  
matplotlib>=3.9.0  
python-dotenv>=1.0.1  
google-genai>=0.2.0

Usage

Upload a CSV via the dashboard.
Explore the auto-generated charts and read the AI-produced insights.
Export visuals or copy insights for reporting.
Author & Contact

Tejashwini K R
🎓 MCA (AI & ML) | Data & Analytics Enthusiast
https://github.com/Tejashwinikr2

tejashwinikr840@gmail.com

Acknowledgments
Gemini API – for powerful AI insights
Streamlit – for fast interactive UI
Seaborn & Matplotlib – for visualization
Pandas – for data handling
