from fpdf import FPDF
import wikipedia
import uuid
import os

# =========================================
# PDF GENERATOR
# =========================================

def generate_pdf(prompt):

    try:

        os.makedirs(
            "generated_pdfs",
            exist_ok=True
        )

        topic = (
            prompt
            .replace("create pdf of", "")
            .replace("make pdf of", "")
            .replace("generate pdf of", "")
            .strip()
        )

        # GET REAL INFO

        try:

            content = wikipedia.summary(
                topic,
                sentences=10
            )

        except:

            content = (
                f"No information found about {topic}"
            )

        # CREATE PDF

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=16
        )

        pdf.multi_cell(
            0,
            10,
            txt=content
        )

        filename = (
            f"generated_pdfs/{uuid.uuid4()}.pdf"
        )

        pdf.output(filename)

        return filename

    except Exception as e:

        print(f"PDF Error: {e}")

        return None