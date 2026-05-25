import sys
import os

# =====================================
# FIX PYTHON IMPORT PATH
# =====================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# =====================================

import streamlit as st

# =====================================
# FRONTEND IMPORTS
# =====================================

from theme import load_theme
from ui import header
from sidebar import render_sidebar
from dashboard import render_dashboard
from chat_ui import render_chat
from animations import loading_animation
from widgets import *

from system_monitor import system_monitor
from voice_ui import voice_panel

# =====================================
# BACKEND IMPORTS
# =====================================

from backend.core import process_command
from backend.database import save_message
from backend.search import web_search
from backend.memory import save_memory

# =====================================
# AI IMPORTS
# =====================================

from ai_modules.chatbot import setup_ai

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# LOAD THEME
# =====================================

load_theme()

header()

# =====================================
# SIDEBAR
# =====================================

personality, language = render_sidebar()

system_monitor()

voice_panel()

# =====================================
# GEMINI AI SETUP
# =====================================

api_key = st.secrets["GEMINI_API_KEY"]

model = setup_ai(api_key)

# =====================================
# SESSION STATE
# =====================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# =====================================
# WIDGETS
# =====================================

weather_widget()

finance_widget()

security_widget()

# =====================================
# DISPLAY OLD CHATS
# =====================================

for msg in st.session_state.messages:

    render_chat(
        msg["role"],
        msg["content"]
    )

# =====================================
# USER INPUT
# =====================================

prompt = st.chat_input(
    "⚡ Speak with JARVIS..."
)

# =====================================
# CHAT SYSTEM
# =====================================

if prompt:

    # SAVE USER MESSAGE
    st.session_state.messages.append({

        "role": "user",
        "content": prompt
    })

    save_memory(
        "user",
        prompt
    )

    save_message(
        "user",
        prompt
    )

    # SHOW USER MESSAGE
    render_chat(
        "user",
        prompt
    )

    # LOADING
    loading_animation()

    # =====================================
    # WEB SEARCH MODE
    # =====================================

    if prompt.lower().startswith("search"):

        search_query = prompt.replace(
            "search",
            ""
        )

        results = web_search(
            search_query
        )

        response = "\n".join(results)

    else:

        # =====================================
        # AI RESPONSE
        # =====================================

        response = process_command(
            model,
            prompt
        )

    # =====================================
    # SHOW RESPONSE
    # =====================================

    render_chat(
        "assistant",
        response
    )

    # =====================================
    # SAVE RESPONSE
    # =====================================

    save_memory(
        "assistant",
        response
    )

    save_message(
        "assistant",
        response
    )

    st.session_state.messages.append({

        "role": "assistant",
        "content": response
    })

# =====================================
# DASHBOARD
# =====================================

render_dashboard()