import pyttsx3
import uuid
import os

# =========================================
# VOICE ENGINE
# =========================================

engine = pyttsx3.init()

engine.setProperty(
    "rate",
    170
)

engine.setProperty(
    "volume",
    1.0
)

# =========================================
# SPEAK FUNCTION
# =========================================

def speak(text):

    os.makedirs(
        "voices",
        exist_ok=True
    )

    filename = (
        f"voices/{uuid.uuid4()}.mp3"
    )

    engine.save_to_file(
        text,
        filename
    )

    engine.runAndWait()

    return filename