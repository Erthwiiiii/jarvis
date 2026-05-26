import streamlit as st
import pandas as pd
import plotly.express as px
import psutil
import time
import sys
import os

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

h1, h2, h3 {
    color: cyan;
}

.stSidebar {
    background-color: #1e293b;
}
</style>
""", unsafe_allow_html=True)

# =========================================
# SESSION MEMORY
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = "default"

# =========================================
# HEADER
# =========================================

st.title("🤖 JARVIS")
st.caption("Advanced Cloud AI Assistant")

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:
    st.title("⚡ JARVIS")
    
    selected = option_menu(
        "Navigation",
        ["Chat", "Dashboard", "System"],
        icons=["chat", "speedometer2", "cpu"],
        default_index=0
    )

# =========================================
# CHAT PAGE
# =========================================

if selected == "Chat":
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat input
    prompt = st.chat_input("Talk with JARVIS...")
    
    if prompt:
        
        # Add user message to session
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # =====================================
        # PROCESS RESPONSE
        # =====================================
        
        # Check if search is requested
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
        
        # Add assistant message to session
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        
        # =====================================
        # SAVE MEMORY
        # =====================================
        
        save_memory("user", prompt)
        save_memory("assistant", response)
        
        try:
            save_message("user", prompt)
            save_message("assistant", response)
        except Exception as e:
            st.warning(f"Could not save message: {str(e)}")

# =========================================
# DASHBOARD PAGE
# =========================================

elif selected == "Dashboard":
    
    st.subheader("📊 AI Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Conversations", len(st.session_state.messages) // 2)
    
    with col2:
        st.metric("AI Chat Usage", "90%")
    
    with col3:
        st.metric("Memory Usage", "80%")
    
    with col4:
        st.metric("System Status", "✅ Active")
    
    # Dashboard chart
    data = pd.DataFrame({
        "Features": [
            "AI Chat",
            "Memory",
            "Search",
            "Dashboard"
        ],
        "Usage": [90, 80, 70, 85]
    })
    
    fig = px.bar(
        data,
        x="Features",
        y="Usage",
        title="JARVIS SYSTEM STATUS",
        color_discrete_sequence=["#00D9FF"]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("✅ All systems operational.")

# =========================================
# SYSTEM PAGE
# =========================================

elif selected == "System":
    
    st.subheader("⚡ System Monitor")
    
    col1, col2, col3 = st.columns(3)
    
    # Get system metrics
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    with col1:
        st.metric("CPU Usage", f"{cpu}%")
        st.progress(cpu / 100)
    
    with col2:
        st.metric("RAM Usage", f"{ram}%")
        st.progress(ram / 100)
    
    with col3:
        st.metric("Disk Usage", f"{disk}%")
        st.progress(disk / 100)
    
    st.info("☁️ Cloud systems active.")
    
    # System details
    st.subheader("System Information")
    system_info = {
        "Platform": f"{sys.platform}",
        "Python Version": f"{sys.version.split()[0]}",
        "Processor Count": f"{psutil.cpu_count()}",
        "Total Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    }
    
    st.json(system_info)
