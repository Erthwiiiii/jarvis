import streamlit as st

from frontend.theme import load_theme
from frontend.ui import header
from frontend.sidebar import render_sidebar
from frontend.dashboard import render_dashboard
from frontend.chat_ui import render_chat
from frontend.animations import loading_animation
from frontend.widgets import *

from backend.core import process_command
from backend.database import save_message

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

        "role":"user",
        "content":prompt
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

        "role":"assistant",
        "content":response
    })

# =====================================

render_dashboard()