# IntelliCredit — AI Powered Credit Risk Assessment System

## Overview
IntelliCredit is an AI-assisted credit risk assessment prototype that analyzes company annual reports and external risk signals to generate an automated credit risk evaluation report.

The system extracts financial indicators from annual reports, combines them with external signals such as news risk indicators, computes a risk score, and produces a structured Credit Risk Assessment Report (PDF) with explanations and lending recommendations.

This prototype demonstrates how financial institutions can automate the initial credit evaluation process, reducing manual effort and improving scalability


## Problem Statement:
Financial institutions rely heavily on manual analysis of lengthy annual reports to evaluate the creditworthiness of companies.

This process is:

 *Time-consuming

 *Difficult to scale

 *Prone to missing key risk indicators

There is a need for an automated system that can extract financial signals, analyze risk indicators, and generate a clear credit risk report.


## Proposed Solution:



IntelliCredit automates the credit analysis pipeline:

-Extract text from company annual reports

-Detect financial signals such as revenue growth, profit margin, debt ratio, and legal risks

-Integrate external risk indicators (news signals)

-Compute a credit risk score

-Generate an AI-assisted credit risk explanation

-Produce a structured Credit Risk Assessment Report

## Demo

Prototype execution example:

Final Risk Score: 22.0  
Risk Level: High  
Recommendation: Loan Rejected

The system automatically analyzes a company annual report, extracts financial signals, calculates credit risk, and generates a structured credit risk assessment report.

### System Architecture:
<img width="1100" height="618" alt="Screenshot 2026-03-10 183231" src="https://github.com/user-attachments/assets/ac4c4b9d-a6f3-4ed8-ac96-db1322dbd91d" />


### Prototype Execution

<img width="1428" height="235" alt="Screenshot 2026-03-10 183342" src="https://github.com/user-attachments/assets/1da9a921-2a1d-4e3c-a351-3f81caef4876" />



### Tech Stack:

-Python

-PDF Text Extraction

-Rule-Based Financial Signal Extraction

-Risk Scoring Engine

-ReportLab (PDF Generation)


### Real World Application:

-Banks and lending institutions

-Financial analysts

-Credit rating teams

-Risk monitoring platforms

### Future Improvements:

-NLP-based financial data extraction

-Real-time news sentiment analysis

-Machine learning credit risk models

-Integration with financial APIs and databases

-Dashboard for interactive risk monitoring

### Quick start:
```
git clone https://github.com/yourusername/intelli-credit-system.git
cd intelli-credit-system

```

```
pip install -r requirements.txt
```

```
python main.py
```






