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

# ======================================
# BACKEND IMPORTS
# ======================================

from backend.core import process_command
from backend.database import save_message
from backend.memory import save_memory
from backend.search import web_search

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
    # AI RESPONSE
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