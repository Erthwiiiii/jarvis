from fpdf import FPDF
import wikipedia
import uuid
import os

# =========================================
# PDF GENERATOR
# =========================================

def generate_pdf(prompt):

    os.makedirs(
        "generated_pdfs",
        exist_ok=True
    )

    topic = (
        prompt
        .replace("create pdf", "")
        .replace("make pdf", "")
        .replace("generate pdf", "")
        .replace("about", "")
        .strip()
    )

    try:

        content = wikipedia.summary(
            topic,
            sentences=15
        )

    except:

        content = (
            f"No information found about {topic}"
        )

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        size=16
    )

    pdf.cell(
        200,
        10,
        txt=topic.title(),
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.multi_cell(
        0,
        10,
        content
    )

    filename = (
        f"generated_pdfs/{uuid.uuid4()}.pdf"
    )

    pdf.output(filename)

    return filename