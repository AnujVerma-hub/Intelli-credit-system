def five_cs_analysis(signals, news_score):
    revenue_growth = signals.get("revenue_growth")
    debt_to_equity = signals.get("debt_to_equity")
    profit_margin = signals.get("profit_margin")

    return {
        "Character": "Risky due to litigation and negative media"
        if signals["litigation_detected"] else "Stable",

        "Capacity": "weak repayment ability"
        if revenue_growth < 0 else "Stable",

        
        
        "Capital": "Low profitability"
        if profit_margin < 10 else "Healthy",

        "Conditions": "Industry slowdown mentioned",
        
        "Collateral": "High leverage risk"
        if debt_to_equity > 2 else "Moderate leverage"
        
    }