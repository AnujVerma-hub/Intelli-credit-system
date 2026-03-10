import json 
import spacy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

risk_keywords = {
    "litigation": [
        "lawsuit", "litigation", "court case", "legal dispute", "sued"
    ],
    "fraud": [
        "fraud", "scam", "misconduct", "corruption", "money laundering"
    ],
    "regulatory": [
        "rbi", "sec", "antitrust", "regulatory action", "investigation",
        "probe", "fine", "penalty"
    ],
    "financial_distress": [
        "insolvency", "bankruptcy", "default", "nclt",
        "liquidation", "debt crisis"
    ],
    "management_risk": [
        "resigned", "fired", "leadership crisis", "ceo exit"
    ]
}

weights = {
    "litigation": 2,
    "fraud": 3,
    "regulatory": 2,
    "financial_distress": 4,
    "management_risk": 1
}

with open("credit_manager/news_extract.txt", "r", encoding="utf-8") as f:
    data = json.load(f)


all_text = ""

for article in data["articles"]:
    if article["title"]:
        all_text += article["title"] + " "
    if article["description"]:
        all_text += article["description"] + " "

all_text = all_text.lower()

def analyse_risk(tokens, risk_dict):

    category_scores = {category: 0 for category in risk_dict}

    for token in tokens:
        for category, keywords in risk_dict.items():
            if token in keywords:
                category_scores[category] +=1

    

    
    
    return category_scores


def score_predict(category_score, weights):
    total_score = 0

    for category in category_score:
        total_score += category_score[category] * weights[category]

    
    return total_score



def preprocess(text):

    nlp = spacy.load("en_core_web_sm")

    docs = nlp(text)

    tokens = [token.lemma_ for token in docs if not token.is_stop]

    return tokens

def sentiment_analysis(text):
    sen = SentimentIntensityAnalyzer()

    score = sen.polarity_scores(text)
    return score["compound"]

def sentiment_multiplier(sen_score):
    if sen_score < -0.5:
        return 1.5
    elif sen_score < -0.1:
        return 1.2
    elif sen_score > 0.3:
        return 0.7
    else:
        return 1
    





def final_value(text):

    tokens = preprocess(text)

    scores = analyse_risk(tokens, risk_keywords)
    key_score = score_predict(scores, weights)

    sen_score = sentiment_analysis(text)
    sentiment_score = sentiment_multiplier(sen_score)



    final_risk = key_score * sentiment_score

    return final_risk


def classify_risk(score):

    if score == 0:
        return "Low"
    elif score < 10:
        return "Moderate"
    elif score < 25:
        return "High"
    else:
        return "Severe"
    
def classify_risk(score):

    if score == 0:
        return "Low"
    elif score < 10:
        return "Moderate"
    elif score < 25:
        return "High"
    else:
        return "Severe"
    





    




final_risk = final_value(all_text)
score = classify_risk(final_risk)


print("Final Risk Score:", final_risk)
print("Risk Level:", score)


