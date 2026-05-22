from gtts import gTTS
import streamlit as st

# =========================================

def speak(text):

    try:

        tts = gTTS(text=text, lang="en")

        tts.save("voice.mp3")

        audio = open("voice.mp3", "rb")

        st.audio(audio.read())

    except:

        pass