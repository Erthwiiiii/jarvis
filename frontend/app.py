# =========================================
# ULTRA JARVIS APP.PY
# FULL PROFESSIONAL VERSION
# =========================================

import streamlit as st
import os
import time
import sys
import psutil
import pycountry
import pandas as pd
import plotly.express as px
import datetime
import webbrowser

# =========================================
# PATH SETUP
# =========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# =========================================
# IMPORTS
# =========================================

from streamlit_option_menu import option_menu

from frontend.camera_module import camera_input_section
from frontend.video_module import video_uploader_section

from backend.speech_to_text import listen_voice
from frontend.voice_engine import speak

from backend.image_generator import generate_image
from backend.video_generator import generate_video
from backend.pdf_generator import generate_pdf

from backend.core import process_command
from backend.memory import save_memory

from backend.file_analyzer import (
    read_pdf,
    analyze_image
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

h1,h2,h3 {
    color: cyan;
}

.stSidebar {
    background-color: #1e293b;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "personality" not in st.session_state:
    st.session_state.personality = "Helpful"

if "language" not in st.session_state:
    st.session_state.language = "English"

# =========================================
# HEADER
# =========================================

st.title("🤖 ULTRA JARVIS")
st.caption("Advanced AI Assistant")

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("⚡ JARVIS")

    selected = option_menu(
        "Navigation",
        [
            "Chat",
            "Dashboard",
            "System",
            "Settings"
        ],
        icons=[
            "chat",
            "bar-chart",
            "cpu",
            "gear"
        ],
        default_index=0
    )

    st.divider()

    personality = st.selectbox(
        "Personality",
        [
            "Helpful",
            "Professional",
            "Casual",
            "Creative"
        ]
    )

#=============================================
#LIGHTWEIGHT LANGUAGE LIST
#=============================================
    try:

        languages = []
        for language in pycountry.languages:

            try:
                if hasattr(language, "name"):
                    
                    languages.append(language.name)

            except:
                pass
        
        language = sorted(list(set(languages)))[:300]
    
    except:

        language = [
            "English",
            "hindi",
            "tamil",
            "telugu"
        ]

#========================================
#LANGUAGE SELECTOR
#========================================

    language = st.selectbox(
        "🌍 Select Language",
        language
    )

# =========================================
# TOP STATUS
# =========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🌡️ Temperature", "25°C")

with col2:
    st.metric("💹 Market", "↑ 2.5%")

with col3:
    st.metric("🔒 Security", "✅ Safe")

st.divider()

# =========================================
# CHAT PAGE
# =========================================

if selected == "Chat":

    st.subheader("💬 Chat With JARVIS")

    camera_input_section()
    video_uploader_section()

    # =====================================
    # FILE UPLOADER
    # =====================================

    uploaded_file = st.file_uploader(
        "📂 Upload File",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ]
    )

    # =====================================
    # FILE PROCESSING
    # =====================================

    if uploaded_file is not None:

        if "pdf" in uploaded_file.type:

            pdf_text = read_pdf(uploaded_file)

            st.text_area(
                "PDF Content",
                pdf_text,
                height=300
            )

        elif "image" in uploaded_file.type:

            st.image(uploaded_file)

            image_data = analyze_image(
                uploaded_file
            )

            st.json(image_data)

    # =====================================
    # CHAT HISTORY
    # =====================================

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.markdown(msg["content"])

    # =====================================
    # VOICE INPUT
    # =====================================

    prompt = None

    if st.button("🎤 Speak"):

        voice_text = listen_voice()

        st.info(f"You said: {voice_text}")

        prompt = voice_text

    # =====================================
    # TEXT INPUT
    # =====================================

    if prompt is None:

        prompt = st.chat_input(
            "⚡ Ask JARVIS..."
        )

    # =====================================
    # PROCESS MESSAGE
    # =====================================

    if prompt:

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):

            st.markdown(prompt)

        response = ""

        # =====================================
        # LOADING
        # =====================================

        with st.spinner("⚡ JARVIS Processing..."):

            # =================================
            # IMAGE GENERATION
            # =================================

            if (
                "create image" in prompt.lower()
                or "generate image" in prompt.lower()
                or "image of" in prompt.lower()
            ):

                with st.chat_message("assistant"):

                    st.markdown(
                        "⚡ Generating Image..."
                    )

                    image_path = generate_image(prompt)

                    if (
                        image_path
                        and os.path.exists(image_path)
                    ):

                        st.image(
                            image_path,
                            width=500
                        )

                        response = (
                            "Image generated successfully sir."
                        )

                        st.success(response)

                        st.balloons()

                    else:

                        response = (
                            "Image generation failed sir."
                        )

                        st.error(response)

            # =================================
            # VIDEO GENERATION
            # =================================

            elif (
                "create video" in prompt.lower()
                or "generate video" in prompt.lower()
            ):

                with st.chat_message("assistant"):

                    st.markdown(
                        "⚡ Generating Video..."
                    )

                    duration = 10

                    if "30 second" in prompt.lower():
                        duration = 30

                    elif "1 minute" in prompt.lower():
                        duration = 60

                    elif "5 minute" in prompt.lower():
                        duration = 300

                    elif "10 minute" in prompt.lower():
                        duration = 600

                    elif "30 minute" in prompt.lower():
                        duration = 1800

                    elif "1 hour" in prompt.lower():
                        duration = 3600

                    video_prompt = (
                        prompt
                        .replace("create video of", "")
                        .replace("generate video of", "")
                        .strip()
                    )

                video_path = generate_video(
                      video_prompt,
                      duration
                    )

                    if (
                        video_path
                        and os.path.exists(video_path)
                    ):

                        st.video(video_path)

                        response = (
                            f"{duration} seconds video generated successfully sir."
                        )

                        st.success(response)

                        st.balloons()

                    else:

                        response = (
                            "Video generation failed sir."
                        )

                        st.error(response)

                        if st.button("🔄 Retry Video"):

                            retry_path = generate_video(
                               video_prompt,
                                duration
                            )

                            if retry_path:

                                st.video(retry_path)

                                st.success(
                                    "Video generated successfully sir."
                                )

            # =================================
            # PDF GENERATION
            # =================================

            elif (
                "create pdf" in prompt.lower()
                or "generate pdf" in prompt.lower()
                or "make pdf" in prompt.lower()
            ):

                with st.chat_message("assistant"):

                    st.markdown(
                        "⚡ Generating PDF..."
                    )

                    pdf_topic = (
                        prompt
                        .replace("create pdf about", "")
                        .replace("generate pdf about", "")
                        .replace("make pdf about", "")
                        .replace("create pdf containing information about", "")
                        .strip()
                    )

                    pdf_path = generate_pdf(pdf_topic)

                    if (
                        pdf_path
                        and os.path.exists(pdf_path)
                    ):

                        response = (
                            "PDF generated successfully sir."
                        )

                        st.success(response)

                        st.balloons()

                        with open(pdf_path, "rb") as file:

                            st.download_button(
                                "📥 Download PDF",
                                file,
                                file_name="jarvis.pdf"
                            )

                    else:

                        response = (
                            "PDF generation failed sir."
                        )

                        st.error(response)

            # =================================
            # OPEN YOUTUBE
            # =================================

            elif "youtube" in prompt.lower():

                search = (
                    prompt.replace("play", "")
                    .replace("on youtube", "")
                )

                url = (
                    "https://www.youtube.com/results?search_query="
                    + search.replace(" ", "+")
                )

                webbrowser.open(url)

                response = (
                    f"Opening YouTube for {search}"
                )

            # =================================
            # OPEN GOOGLE
            # =================================

            elif "google" in prompt.lower():

                search = (
                    prompt.replace("search", "")
                    .replace("on google", "")
                )

                url = (
                    "https://www.google.com/search?q="
                    + search.replace(" ", "+")
                )

                webbrowser.open(url)

                response = (
                    f"Searching Google for {search}"
                )

            # =================================
            # TIME
            # =================================

            elif "time" in prompt.lower():

                current_time = (
                    datetime.datetime.now().strftime(
                        "%I:%M %p"
                    )
                )

                response = (
                    f"Current time is {current_time}"
                )

            # =================================
            # DATE
            # =================================

            elif "date" in prompt.lower():

                current_date = (
                    datetime.datetime.now().strftime(
                        "%d %B %Y"
                    )
                )

                response = (
                    f"Today's date is {current_date}"
                )

            # =================================
            # NORMAL AI RESPONSE
            # =================================

            else:

                response = process_command(prompt)

                with st.chat_message("assistant"):

                    placeholder = st.empty()

                    typed = ""

                    for char in response:

                        typed += char

                        placeholder.markdown(typed)

                        time.sleep(0.01)

        # =====================================
        # SAVE CHAT
        # =====================================

        st.session_state.messages.append({

            "role": "assistant",

            "content": response
        })

        # =====================================
        # SAVE MEMORY
        # =====================================

        try:

            save_memory(
                "user",
                prompt
            )

            save_memory(
                "assistant",
                response
            )

        except:
            pass

        # =====================================
        # VOICE OUTPUT
        # =====================================

        try:

            audio_path = speak(response)

            if audio_path:

                st.audio(audio_path)

        except:
            pass

# =========================================
# DASHBOARD
# =========================================

elif selected == "Dashboard":

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Conversations",
            len(st.session_state.messages)
        )

    with col2:

        st.metric(
            "AI Status",
            "ONLINE"
        )

    with col3:

        st.metric(
            "Memory",
            "ACTIVE"
        )

    data = pd.DataFrame({

        "Features": [
            "AI Chat",
            "Images",
            "Videos",
            "PDF",
            "Voice"
        ],

        "Usage": [
            95,
            90,
            80,
            85,
            92
        ]
    })

    fig = px.bar(
        data,
        x="Features",
        y="Usage",
        title="JARVIS FEATURES"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================
# SYSTEM PAGE
# =========================================

elif selected == "System":

    st.subheader("⚡ System Monitor")

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    st.metric("CPU", f"{cpu}%")
    st.progress(cpu / 100)

    st.metric("RAM", f"{ram}%")
    st.progress(ram / 100)

    st.metric("DISK", f"{disk}%")
    st.progress(disk / 100)

# =========================================
# SETTINGS PAGE
# =========================================

elif selected == "Settings":

    st.subheader("⚙️ Settings")

    st.success("All settings working properly.")

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption("🤖 ULTRA JARVIS v5.0")
