from gtts import gTTS
import uuid
import os

# =========================================
# VOICE ENGINE
# =========================================

def speak(text):

    try:

        os.makedirs(
            "voices",
            exist_ok=True
        )

        filename = (
            f"voices/{uuid.uuid4()}.mp3"
        )

        tts = gTTS(
            text=text,
            lang="en"
        )

        tts.save(filename)

        return filename

    except Exception as e:

        print(f"Voice Error: {e}")

        return None