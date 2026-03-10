import json
from credit_score import internal_risk_score
from five_cs import five_cs_analysis
from generate_pdf import generate_pdf
from credit_manager.signal_extractor import final_value
from credit_manager.new_api import new_api
from credit_manager.AI_assistant import generate_llm_explanation


def normalize_signals(signals):

    defaults = {
        "revenue_growth": None,
        "profit_margin": None,
        "debt_to_equity": 1,
        "litigation_detected": False,
        "litigation_count": None,
        "auditor_remark": "Clean"
    }

    for key, value in defaults.items():
        signals.setdefault(key, value)

    return signals


with open("section_data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    
json_part = content[content.find("{"):]
signals = json.loads(json_part)
signals = normalize_signals(signals)



internal_score = internal_risk_score(signals)


with open("credit_manager/news_extract.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

all_text = ""

for article in data["articles"]:
    if article["title"]:
        all_text += article["title"] + " "
    if article["description"]:
        all_text += article["description"] + " "

all_text = all_text.lower()

news_score = final_value(all_text)
final_score = internal_score + news_score

five_cs = five_cs_analysis(signals, news_score)

explanation = generate_llm_explanation(signals,internal_score, news_score, final_score)


if final_score > 7:
    decision = "Loan Rejected"
elif final_score > 4:
    decision = "Manual Review Required"
else:
    decision = "Loan Approved"


generate_pdf(signals,internal_score, news_score, final_score, five_cs, explanation,decision)




