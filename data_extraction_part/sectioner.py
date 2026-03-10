from data_loader import load_document


SECTION_KEYWORDS = {
    "financial_highlights": [
        "financial highlights",
        "financial summary",
        "key financial"
    ],
    "auditor_report": [
        "independent auditor",
        "auditor report",
        "auditors have issued"
    ],
    "legal_proceedings": [
        "legal proceedings",
        "litigation",
        "court case"
    ],
    "management_discussion": [
        "management discussion",
        "management discussion and analysis",
        "md&a"
    ]
}

def split_into_sections(text):
    sections = {}
    text_lower = text.lower()

    # Find starting index of each section
    section_positions = {}

    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            idx = text_lower.find(keyword)
            if idx != -1:
                section_positions[section] = idx
                break

    # Sort sections by position in text
    sorted_sections = sorted(section_positions.items(), key=lambda x: x[1])

    # Extract section text
    for i, (section, start_pos) in enumerate(sorted_sections):
        if i + 1 < len(sorted_sections):
            end_pos = sorted_sections[i + 1][1]
        else:
            end_pos = len(text)

        sections[section] = text[start_pos:end_pos].strip()

    return sections

doc = load_document("data_extraction_part/apple_annual_report.pdf")

sections = split_into_sections(doc["text"])

for name, content in sections.items():
    print(f"\n--- {name.upper()} ---\n")
    print(content[:300])


with open("Data/section_data.txt", "w", encoding="utf-8") as f:
    f.write("Section Report\n")
    for name, content in sections.items():
        f.write(f"\n -- {name.upper()}--\n")
        f.write(content[:300])

