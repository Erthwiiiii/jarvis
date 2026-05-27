from reportlab.pdfgen import canvas
import os
import time

def generate_pdf(text):

    os.makedirs(
        "generated_pdfs",
        exist_ok=True
    )

    filename = f"generated_pdfs/file_{int(time.time())}.pdf"

    c = canvas.Canvas(filename)

    c.drawString(
        100,
        750,
        text
    )

    c.save()

    return filename
