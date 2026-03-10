import json
from credit_manager.signal_extractor import final_value
with open("credit_manager/news_extract.txt", "r", encoding="utf-8") as f:
    data1 = json.load(f)

all_text = ""

for article in data1["articles"]:
    if article["title"]:
        all_text += article["title"] + " "
    if article["description"]:
        all_text += article["description"] + " "

all_text = all_text.lower()

with open("section_data.txt", "r", encoding="utf-8") as f:


    data = f.read()

def normalize_signals(signals):

    defaults = {
        "revenue_growth": 0,
        "profit_margin": 0,
        "debt_to_equity": 1,
        "litigation_detected": False,
        "litigation_count": 0,
        "auditor_remark": "Clean"
    }

    for key, value in defaults.items():
        signals.setdefault(key, value)

    return signals

json_part = data[data.find("{"):data.rfind("}")+1]

signals = json.loads(json_part)
signals = normalize_signals(signals)




def internal_risk_score(signals):

    score = 0
    revenue_growth = signals.get("revenue_growth")
    debt_to_equity = signals.get("debt_to_equity")
    profit_margin = signals.get("profit_margin")

    # litigation
    if signals["litigation_detected"]:
        if signals["litigation_count"]:

            score += signals["litigation_count"]
        else:
            score += 1

    # revenue growth
    if revenue_growth is not None:
        if revenue_growth > 5:
            score += 0
        elif revenue_growth >= 0:
            score += 1
        else:
            score += 2
    

    # debt to income
    if debt_to_equity is not None:
        if debt_to_equity > 0.5:
            score += 3
        elif debt_to_equity > 0.3:
            score += 2

    if profit_margin is not None:
        if profit_margin > 7.5:
            score -=3
        elif profit_margin > 5.5:
            score -=1
        else:
            score +=2

    
    return score



internal_score = internal_risk_score(signals)

news_score = final_value(all_text)

final_score = internal_score + (news_score * 0.5)

print("final score: ", final_score)
