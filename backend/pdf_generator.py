from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import wikipedia

def generate_pdf(prompt):

    topic = prompt.lower()

    topic = topic.replace(
        "create pdf of",
        ""
    )

    topic = topic.replace(
        "make pdf in which information about",
        ""
    )

    topic = topic.strip()

    try:

        content = wikipedia.summary(
            topic,
            sentences=12
        )

    except:

        content = "Information not found."

    path = "jarvis_document.pdf"

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph(
        f"<b>{topic.title()}</b>",
        styles['Title']
    )

    story.append(title)

    story.append(Spacer(1, 20))

    body = Paragraph(
        content,
        styles['BodyText']
    )

    story.append(body)

    doc.build(story)

    return path
