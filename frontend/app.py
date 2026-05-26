import streamlit as st
import sys
import os

# ======================================
# FIX PYTHON PATH FOR RENDER
# ======================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# ======================================
# FRONTEND IMPORTS
# ======================================

from theme import load_theme
from ui import header
from sidebar import render_sidebar
from dashboard import render_dashboard
from chat_ui import render_chat
from animations import loading_animation
from widgets import *

from voice_engine import speak
from system_monitor import system_monitor

# ======================================
# BACKEND IMPORTS
# ======================================

from backend.core import process_command
from backend.database import save_message
from backend.memory import save_memory
from backend.search import web_search
from backend.automation import execute_command

# ======================================
# AI IMPORT
# ======================================

from ai_modules.chatbot import setup_ai

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# ======================================
# LOAD UI
# ======================================

load_theme()

header()

personality, language = render_sidebar()

# ======================================
# GEMINI AI SETUP
# ======================================

api_key = st.secrets["GEMINI_API_KEY"]

model = setup_ai(api_key)

# ======================================
# SESSION STATE
# ======================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# ======================================
# WIDGETS
# ======================================

weather_widget()

finance_widget()

security_widget()

system_monitor()

# ======================================
# DISPLAY OLD CHATS
# ======================================

for msg in st.session_state.messages:

    render_chat(
        msg["role"],
        msg["content"]
    )

# ======================================
# CHAT INPUT
# ======================================

prompt = st.chat_input(
    "⚡ Speak with JARVIS..."
)

# ======================================
# MAIN AI SYSTEM
# ======================================

if prompt:

    # USER MESSAGE

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
    # AUTOMATION SYSTEM
    # ======================================

    automation_response = execute_command(prompt)

    # ======================================
    # AI RESPONSE
    # ======================================

    if automation_response != "Command not recognized":

        response = automation_response

    else:

        response = process_command(
            model,
            prompt
        )

    # ======================================
    # SHOW RESPONSE
    # ======================================

    render_chat(
        "assistant",
        response
    )

    # ======================================
    # SPEAK RESPONSE
    # ======================================

    try:

        speak(response)

    except:

        pass

    # ======================================
    # SAVE DATABASE
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
    # SAVE MEMORY
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
    # SAVE SESSION
    # ======================================

    st.session_state.messages.append({

        "role": "assistant",
        "content": response
    })

# ======================================
# DASHBOARD
# ======================================

render_dashboard()