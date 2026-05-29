from fpdf import FPDF
import uuid
import wikipedia
import os

# =========================================
# PDF GENERATOR
# =========================================

def generate_pdf(text):

    try:

        # =====================================
        # CREATE FOLDER
        # =====================================

        os.makedirs(
            "generated_pdfs",
            exist_ok=True
        )

        # =====================================
        # PDF FILE
        # =====================================

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=14
        )

        # =====================================
        # TITLE
        # =====================================

        pdf.cell(
            200,
            10,
            txt="ULTRA JARVIS PDF",
            ln=True,
            align="C"
        )

        pdf.ln(10)

        # =====================================
        # CONTENT
        # =====================================

        pdf.multi_cell(
            0,
            10,
            txt=text
        )

        # =====================================
        # SAVE FILE
        # =====================================

        filename = (
            f"generated_pdfs/{uuid.uuid4()}.pdf"
        )

        pdf.output(filename)

        return filename

    except Exception as e:

        print("PDF ERROR:", e)

        return None
