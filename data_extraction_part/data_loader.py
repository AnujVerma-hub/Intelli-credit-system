import os
import pdfplumber
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract
import re



def load_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".txt":
        return load_txt(file_path)

    elif extension == ".pdf":
        return load_pdf(file_path)

    else:
        raise ValueError("Unsupported file format")
    

def load_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return {
        "text": normalize_text(text),
        "source_type": "txt",
        "metadata": {
            "file_name": os.path.basename(file_path),
            "length": len(text)
        }
    }


def load_pdf(file_path):
    text = extract_text_pdf(file_path)

    # If very little text extracted → assume scanned
    if len(text.strip()) < 500:
        text = extract_text_ocr(file_path)
        source_type = "pdf_scanned"
    else:
        source_type = "pdf_text"

    return {
        "text": normalize_text(text),
        "source_type": source_type,
        "metadata": {
            "file_name": os.path.basename(file_path),
            "length": len(text)
        }
    }


def extract_text_pdf(file_path):
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""

    return text


def extract_text_ocr(file_path):
    text = ""
    images = convert_from_path(file_path)

    for img in images:
        text += pytesseract.image_to_string(img)

    return text




def normalize_text(text):
    text = text.lower()
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()



doc = load_document("data_extraction_part/apple_annual_report.pdf")

print(doc["source_type"])
print(doc["metadata"])
print(doc["text"][:500])

