import requests
import os
import json


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.1:8b-instruct-q4_0"


def generate_llm_explanation(signals, internal_score, news_score, final_score):
        prompt = f"""
You are a financial credit risk analyst.

Financial Signals:
Revenue Growth: {signals['revenue_growth']}%
Profit Margin: {signals['profit_margin']}%
Debt to Equity: {signals['debt_to_equity']}
Litigation Cases: {signals['litigation_count']}
Auditor Remark: {signals['auditor_remark']}

Internal Risk Score: {internal_score}
News Risk Score: {news_score}

Final Risk Score: {final_score}

Explain the company's credit risk in a professional report style.
If any of the financial signals are mssing, then say "insufficient financial disclosure".
If load is approved then then also give a specific load amount range based on financial signals.
Mention key risk drivers and whether lending is advisable. And be brief do not over explain use minimum sentences.
"""
        response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "prompt": prompt,
                    "stream": False
                               
                }
        )

        return response.json()["response"]
        
