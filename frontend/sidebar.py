import streamlit as st
import random
from datetime import datetime

def render_sidebar():

    with st.sidebar:

        st.title("⚡ JARVIS CONTROL")

        st.success("🟢 AI ONLINE")

        st.info(
            datetime.now().strftime(
                "%H:%M:%S"
            )
        )

        st.divider()

        personality = st.selectbox(
            "AI Personality",
            [
                "Iron Man",
                "Cyberpunk",
                "Professional",
                "Hacker",
                "Ultra Intelligence"
            ]
        )

        language = st.selectbox(
            "Language",
            [
                "en",
                "hi",
                "fr",
                "de"
            ]
        )

        st.divider()

        cpu = random.randint(20,80)
        ram = random.randint(30,90)

        st.write("### SYSTEM STATUS")

        st.progress(cpu)
        st.caption(f"CPU : {cpu}%")

        st.progress(ram)
        st.caption(f"RAM : {ram}%")

        st.divider()

        uploaded = st.file_uploader(
            "Upload File",
            type=[
                "png",
                "jpg",
                "txt",
                "pdf"
            ]
        )

        return personality, language