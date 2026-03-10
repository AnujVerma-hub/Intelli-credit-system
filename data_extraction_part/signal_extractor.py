import re
from data_loader import load_document
from sectioner import split_into_sections
import json

import re

def extract_financial_signals(financial_text):

    signals = {}

    text = financial_text.lower()

    # Revenue growth
    rev_match = re.search(r'(-?\d+\.?\d*)\s*%.*(yoy|year over year|increase|growth)', text)
    if rev_match:
        signals["revenue_growth"] = float(rev_match.group(1))

    # Profit margin
    margin_match = re.search(r'(profit margin|net margin|operating margin).*?(\d+\.?\d*)\s*%', text)
    if margin_match:
        signals["profit_margin"] = float(margin_match.group(2))

    # Debt to equity
    debt_match = re.search(r'(debt[- ]?to[- ]?equity).*?(\d+\.?\d*)', text)
    if debt_match:
        signals["debt_to_equity"] = float(debt_match.group(2))

    return signals

def extract_legal_signals(legal_text):

    signals = {}

    text = legal_text.lower()

    if "litigation" in text or "legal proceeding" in text or "lawsuit" in text:
        signals["litigation_detected"] = True

        count_match = re.search(r'(\d+)\s+(cases|proceedings|lawsuits)', text)

        if count_match:
            signals["litigation_count"] = int(count_match.group(1))
        else:
            signals["litigation_count"] = 1

    else:
        signals["litigation_detected"] = False
        signals["litigation_count"] = 0

    return signals

def extract_auditor_signals(auditor_text):

    signals = {}

    text = auditor_text.lower()

    if "qualified opinion" in text:
        signals["auditor_remark"] = "Qualified"

    elif "adverse opinion" in text:
        signals["auditor_remark"] = "Adverse"

    elif "disclaimer of opinion" in text:
        signals["auditor_remark"] = "Disclaimer"

    else:
        signals["auditor_remark"] = "Clean"

    return signals


def extract_operational_signals(management_text):

    signals = {}

    text = management_text.lower()

    util_match = re.search(r'(\d+)\s*%.*utilization', text)

    if util_match:
        signals["factory_utilization"] = int(util_match.group(1))

    return signals

def extract_all_signals(sections):

    signals = {}

    if "financial_highlights" in sections:
        signals.update(extract_financial_signals(sections["financial_highlights"]))

    if "legal_proceedings" in sections:
        signals.update(extract_legal_signals(sections["legal_proceedings"]))

    if "auditor_report" in sections:
        signals.update(extract_auditor_signals(sections["auditor_report"]))

    if "management_discussion" in sections:
        signals.update(extract_operational_signals(sections["management_discussion"]))

    return signals


doc = load_document("data_extraction_part/apple_annual_report.pdf")
sections = split_into_sections(doc["text"])
signals = extract_all_signals(sections)

print(signals)

with open("Data/section_data.txt", "a", encoding="utf-8") as f:
    json_str = json.dumps(signals,ensure_ascii=False)
    f.write(json_str + "\n")

