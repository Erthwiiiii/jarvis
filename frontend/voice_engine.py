from gtts import gTTS
import os
import uuid


def speak(text):

    os.makedirs(
        "temp_audio",
        exist_ok=True
    )

    filename = (
        f"temp_audio/{uuid.uuid4()}.mp3"
    )

    tts = gTTS(text=text, lang="en")

    tts.save(filename)

    return filename
