import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st

# FRONTEND IMPORTS
from theme import load_theme
from ui import header
from sidebar import render_sidebar
from dashboard import render_dashboard
from chat_ui import render_chat
from animations import loading_animation
from widgets import *

# BACKEND IMPORTS
from backend.core import process_command
from backend.database import save_message

# AI IMPORT
from ai_modules.chatbot import setup_ai

# =====================================

st.set_page_config(
    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# =====================================

load_theme()

header()

personality, language = render_sidebar()

# =====================================
# GEMINI AI SETUP
# =====================================

api_key = st.secrets["GEMINI_API_KEY"]

model = setup_ai(api_key)

# =====================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# =====================================

weather_widget()

finance_widget()

security_widget()

# =====================================

for msg in st.session_state.messages:

    render_chat(
        msg["role"],
        msg["content"]
    )

# =====================================

prompt = st.chat_input(
    "⚡ Speak with JARVIS..."
)

# =====================================

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

    # =====================================
    # AI RESPONSE
    # =====================================

    response = process_command(
        model,
        prompt
    )

    # =====================================

    render_chat(
        "assistant",
        response
    )

    # =====================================

    save_message(
        "user",
        prompt
    )

    save_message(
        "assistant",
        response
    )

    # =====================================

    st.session_state.messages.append({

        "role": "assistant",
        "content": response
    })

# =====================================

render_dashboard()