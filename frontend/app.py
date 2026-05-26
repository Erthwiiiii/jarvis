import streamlit as st
import pandas as pd
import psutil
import time
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from streamlit_option_menu import option_menu
from backend.core import process_command
from backend.database import save_message
from backend.memory import save_memory
from backend.search import web_search

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(

    page_title="JARVIS AI",

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

.stChatMessage {

    border-radius: 15px;

    padding: 10px;
}

h1,h2,h3 {

    color: cyan;
}

</style>

""", unsafe_allow_html=True)

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("⚡ JARVIS")

    selected = option_menu(

        "Navigation",

        ["Chat", "Dashboard", "System"],

        icons=[
            "chat",
            "speedometer2",
            "cpu"
        ],

        default_index=0
    )

# =========================================
# HEADER
# =========================================

st.title("🤖 JARVIS PHASE 7")

st.caption("Advanced Cloud AI Assistant")

# =========================================
# SESSION MEMORY
# =========================================

if "messages" not in st.session_state:

    st.session_state.messages = []

# =========================================
# CHAT PAGE
# =========================================

if selected == "Chat":

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.markdown(msg["content"])

    prompt = st.chat_input(
        "Talk with JARVIS..."
    )

    if prompt:

        st.session_state.messages.append({

            "role": "user",

            "content": prompt
        })

        with st.chat_message("user"):

            st.markdown(prompt)

        # =====================================
        # SEARCH MODE
        # =====================================

        if "search" in prompt.lower():

            response = web_search(prompt)

        else:

            response = process_command(prompt)

        # =====================================
        # TYPING EFFECT
        # =====================================

        with st.chat_message("assistant"):

            placeholder = st.empty()

            typed = ""

            for char in response:

                typed += char

                placeholder.markdown(typed)

                time.sleep(0.01)

        st.session_state.messages.append({

            "role": "assistant",

            "content": response
        })

        # =====================================
        # SAVE MEMORY
        # =====================================

        save_memory("user", prompt)

        save_memory("assistant", response)

# =========================================
# DASHBOARD PAGE
# =========================================

elif selected == "Dashboard":

    st.subheader("📊 AI Dashboard")

    data = pd.DataFrame({

        "Tasks": [

            "AI Chat",

            "Memory",

            "Search",

            "Dashboard"
        ],

        "Usage": [

            90,

            80,

            70,

            85
        ]
    })

    fig = px.bar(

        data,

        x="Tasks",

        y="Usage",

        title="JARVIS SYSTEM STATUS"
    )

    st.plotly_chart(

        fig,

        use_container_width=True
    )

    st.success(
        "All systems operational."
    )

# =========================================
# SYSTEM PAGE
# =========================================

elif selected == "System":

    st.subheader("⚡ System Monitor")

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    st.metric(

        "CPU Usage",

        f"{cpu}%"
    )

    st.progress(cpu / 100)

    st.metric(

        "RAM Usage",

        f"{ram}%"
    )

    st.progress(ram / 100)

    st.metric(

        "Disk Usage",

        f"{disk}%"
    )

    st.progress(disk / 100)

    st.info(
        "Cloud systems active."
    )
