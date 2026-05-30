from fpdf import FPDF
import wikipedia
import uuid
import os

def generate_pdf(prompt):

    try:

        os.makedirs(
            "generated_pdfs",
            exist_ok=True
        )

        topic = (
            prompt
            .replace("create pdf containing information about", "")
            .replace("create pdf about", "")
            .replace("generate pdf about", "")
            .strip()
        )

        try:

            content = wikipedia.summary(
                topic,
                sentences=15
            )

        except:

            content = topic

        pdf = FPDF()

        pdf.add_page()

        pdf.set_font(
            "Arial",
            size=12
        )

        pdf.multi_cell(
            0,
            8,
            content
        )

        filename = (
            f"generated_pdfs/{uuid.uuid4()}.pdf"
        )

        pdf.output(filename)

        return filename

    except Exception as e:

        print("PDF ERROR:", e)

        return None