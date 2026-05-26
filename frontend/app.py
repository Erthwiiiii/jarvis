import streamlit as st

# FRONTEND
from theme import load_theme
from ui import header
from sidebar import render_sidebar
from dashboard import render_dashboard
from chat_ui import render_chat
from animations import loading_animation
from widgets import *

from voice_engine import speak
from system_monitor import system_monitor
from system_control import *

# BACKEND
from backend.core import process_command
from backend.database import save_message
from backend.memory import save_memory
from backend.search import web_search

# AI
from ai_modules.chatbot import setup_ai

# ======================================

st.set_page_config(

    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# ======================================

load_theme()

header()

personality, language = render_sidebar()

# ======================================

api_key = st.secrets["GEMINI_API_KEY"]

model = setup_ai(api_key)

# ======================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# ======================================

weather_widget()

finance_widget()

security_widget()

system_monitor()

# ======================================

st.sidebar.title("⚡ Quick Controls")

if st.sidebar.button("Open Google"):

    open_google()

if st.sidebar.button("Open YouTube"):

    open_youtube()

if st.sidebar.button("Open GitHub"):

    open_github()

# ======================================

for msg in st.session_state.messages:

    render_chat(
        msg["role"],
        msg["content"]
    )

# ======================================

prompt = st.chat_input(
    "⚡ Speak with JARVIS..."
)

# ======================================

if prompt:

    st.session_state.messages.append({

        "role": "user",
        "content": prompt
    })

    render_chat(
        "user",
        prompt
    )

    loading_animation()

    # ======================================

    response = process_command(
        model,
        prompt
    )

    # ======================================

    render_chat(
        "assistant",
        response
    )

    speak(response)

    # ======================================

    save_message(
        "user",
        prompt
    )

    save_message(
        "assistant",
        response
    )

    # ======================================

    save_memory(
        "user",
        prompt
    )

    save_memory(
        "assistant",
        response
    )

    # ======================================

    st.session_state.messages.append({

        "role": "assistant",
        "content": response
    })

# ======================================

render_dashboard()