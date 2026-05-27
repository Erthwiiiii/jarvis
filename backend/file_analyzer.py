import pdfplumber
from PIL import Image

# ==========================================
# READ PDF
# ==========================================

def read_pdf(file):

    text = ""

    try:

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

        return text

    except Exception as e:

        return f"PDF Error: {str(e)}"

# ==========================================
# READ IMAGE
# ==========================================

def analyze_image(image):

    try:

        img = Image.open(image)

        return {

            "Format": img.format,
            "Size": img.size,
            "Mode": img.mode

        }

    except Exception as e:

        return f"Image Error: {str(e)}"
