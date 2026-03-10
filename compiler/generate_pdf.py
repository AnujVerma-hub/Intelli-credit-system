from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

def generate_pdf(signals, internal_score, news_score, final_score, five_cs, explanation, decision):

    c = canvas.Canvas("credit_risk_report.pdf", pagesize=letter)

    y = 750

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "AI Credit Risk Assessment Report")
    c.setFont("Helvetica", 10)
    y -= 40

    c.drawString(50, y, "Financial Signals")
    y -= 20

    for key, value in signals.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 20

    y -= 10
    c.drawString(50, y, f"Internal Risk Score: {internal_score}")
    y -= 20

    c.drawString(50, y, f"News Risk Score: {news_score}")
    y -= 20

    c.drawString(50, y, f"Final Risk Score: {final_score}")
    y -= 30

    c.drawString(50, y, "Five C's Analysis")
    y -= 20

    for key, value in five_cs.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 20

    y -= 20
    c.drawString(50, y, "AI Risk Explanation")
    y -= 20

    textobject = c.beginText(60, y)
    textobject.setFont("Helvetica", 10)

    for paragraph in explanation.split("\n"):
        wrapped = textwrap.wrap(paragraph, 90)
        for line in wrapped:
            textobject.textLine(line)

    c.drawText(textobject)

    y = textobject.getY() - 20

    c.drawString(50, y, f"Final Decision: {decision}")

    c.save()