import streamlit as st
import pandas as pd
import plotly.express as px
import psutil
import time
import sys
import os
import pycountry

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
# SAFE IMPORTS
# =========================================

try:
    from frontend.system_monitor import system_monitor
except:
    def system_monitor():
        pass

try:
    from frontend.animations import loading_animation
except:
    def loading_animation():
        with st.spinner("🤖 JARVIS Processing..."):
            time.sleep(1)

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

        ["Chat", "Dashboard", "System", "Settings"],

        icons=[
            "chat",
            "speedometer2",
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

    st.session_state.personality = personality

    # =====================================
    # ALL LANGUAGES
    # =====================================

    languages = sorted(

        [

            language.name

            for language in pycountry.languages

            if hasattr(language, 'name')

        ]

    )

    language = st.selectbox(

        "🌍 Select Language",

        languages,

        index=languages.index("English")

    )

    st.session_state.language = language

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

    st.subheader("💬 Chat with JARVIS")

    # =====================================
    # CAMERA
    # =====================================

    camera_input_section()

    # =====================================
    # VIDEO UPLOADER
    # =====================================

    video_uploader_section()

    # =====================================
    # FILE UPLOADER
    # =====================================

    uploaded_file = st.file_uploader(

        "📂 Upload PDF or Image",

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

        file_type = uploaded_file.type

        # PDF

        if "pdf" in file_type:

            st.success("✅ PDF Uploaded")

            pdf_text = read_pdf(uploaded_file)

            st.subheader("📄 PDF CONTENT")

            st.text_area(

                "Extracted Text",

                pdf_text,

                height=300
            )

        # IMAGE

        elif "image" in file_type:

            st.success("✅ Image Uploaded")

            st.image(uploaded_file)

            image_data = analyze_image(
                uploaded_file
            )

            st.subheader("🖼️ IMAGE DETAILS")

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

        st.info(
            f"You said: {voice_text}"
        )

        prompt = voice_text

    # =====================================
    # TEXT INPUT
    # =====================================

    if prompt is None:

        prompt = st.chat_input(
            "⚡ Speak with JARVIS..."
        )

    # =====================================
    # PROCESS MESSAGE
    # =====================================

    if prompt:

        # USER MESSAGE

        st.session_state.messages.append({

            "role": "user",

            "content": prompt
        })

        with st.chat_message("user"):

            st.markdown(prompt)

        # =================================
        # LOADING
        # =================================

        loading_animation()

        # =====================================
        # IMAGE GENERATION
        # =====================================

        if "create image" in prompt.lower():

           image_path = generate_image(prompt)

           response = (
               "Image generated successfully sir."
            )

            # SAVE CHAT

            st.session_state.messages.append({

                "role": "assistant",

                "content": response
       })

            # DISPLAY RESPONSE

            with st.chat_message("assistant"):

               st.markdown(
                   "⚡ JARVIS PROCESSING ⚡"
           )

               st.image(image_path)

               st.success(response)

            # SPEAK

            try:

                 speak(response)

            except:

                    pass


        # =====================================
        # VIDEO GENERATION
        # =====================================

        elif "create video" in prompt.lower():

            video_path = generate_video(prompt)

            response = "Video created successfully sir."

            with st.chat_message("assistant"):

                st.video(video_path)

                st.success(response)

        # =====================================
        # PDF GENERATION
        # =====================================

        elif "create pdf" in prompt.lower():

            pdf_path = generate_pdf(prompt)

            response = "PDF created successfully sir."

            with st.chat_message("assistant"):

                st.success(response)

                with open(pdf_path, "rb") as file:

                    st.download_button(

                        "Download PDF",

                        file,

                        file_name="jarvis.pdf"
                    )

        # =====================================
        # NORMAL AI RESPONSE
        # =====================================

        else:

            response = process_command(prompt)

            with st.chat_message("assistant"):

                placeholder = st.empty()

                typed = ""

                for char in response:

                    typed += char

                    placeholder.markdown(typed)

                    time.sleep(0.005)

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

        except Exception as e:

            st.warning(
                f"Memory Error: {e}"
            )

        # =====================================
        # VOICE OUTPUT
        # =====================================

        try:

            audio_path = speak(response)

            st.audio(audio_path)

        except Exception as e:

            st.warning(
                f"Voice Error: {e}"
            )

# =========================================
# DASHBOARD PAGE
# =========================================

elif selected == "Dashboard":

    st.subheader("📊 AI Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💬 Conversations",
            len(
                st.session_state.messages
            ) // 2
        )

    with col2:
        st.metric(
            "🧠 Memory Usage",
            "80%"
        )

    with col3:
        st.metric(
            "⚡ AI Usage",
            "90%"
        )

    with col4:
        st.metric(
            "🔧 System",
            "✅ Active"
        )

# =========================================
# SYSTEM PAGE
# =========================================

elif selected == "System":

    st.subheader("⚡ System Monitor")

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "CPU Usage",
            f"{cpu}%"
        )

    with col2:
        st.metric(
            "RAM Usage",
            f"{ram}%"
        )

    with col3:
        st.metric(
            "Disk Usage",
            f"{disk}%"
        )

# =========================================
# SETTINGS PAGE
# =========================================

elif selected == "Settings":

    st.subheader("⚙️ Settings")

    st.info("Settings panel ready.")

# =========================================
# FOOTER
# =========================================

st.divider()

f1, f2, f3 = st.columns(3)

with f1:
    st.caption("🤖 JARVIS v2.0")

with f2:
    st.caption(
        f"💭 {st.session_state.personality}"
    )

with f3:
    st.caption(
        f"🌍 {st.session_state.language}"
    )

# =========================================
# SYSTEM MONITOR
# =========================================

try:

    system_monitor()

except:

    pass
