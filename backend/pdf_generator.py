from fpdf import FPDF
import wikipedia
import uuid
import os

try:
    from duckduckgo_search import DDGS
except:
    DDGS = None


def web_search(query):

    try:

        if DDGS is None:
            return None

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=3
                )
            )

        if results:

            return results[0]["body"]

        return None

    except:

        return None


def generate_pdf(prompt):

    try:

        os.makedirs(
            "generated_pdfs",
            exist_ok=True
        )

        topic = (
            prompt
            .replace(
                "create pdf containing information about",
                ""
            )
            .replace(
                "create pdf about",
                ""
            )
            .replace(
                "generate pdf about",
                ""
            )
            .strip()
        )

        content = None

        try:

            wikipedia.set_lang("en")

            search_results = wikipedia.search(topic)

            if search_results:

               content = wikipedia.summary(
                   search_results[0],
                   sentences=15
               )
               
        except:

            content = web_search(topic)

        if not content:

            content = (
                f"Information about {topic} could not be found."
            )

        pdf = FPDF()

        pdf.add_page()

        pdf.set_auto_page_break(
            auto=True,
            margin=15
        )

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

        print("PDF SAVED:", filename)

        return filename

    except Exception as e:

        print("PDF ERROR:", str(e))

        return None
