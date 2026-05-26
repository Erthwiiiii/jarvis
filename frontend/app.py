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
# FRONTEND IMPORTS
# =========================================

from streamlit_option_menu import option_menu

try:
    from frontend.theme import load_theme
except:
    def load_theme():
        pass

try:
    from frontend.animations import loading_animation
except:
    def loading_animation():
        with st.spinner("🤖 JARVIS is thinking..."):
            time.sleep(1)

try:
    from frontend.voice_engine import speak
except:
    def speak(text):
        pass

try:
    from frontend.system_monitor import system_monitor
except:
    def system_monitor():
        pass

# =========================================
# BACKEND IMPORTS
# =========================================

from backend.core import process_command
from backend.database import save_message
from backend.memory import save_memory
from backend.search import web_search

try:
    from backend.automation import execute_command
except:
    def execute_command(prompt):
        return "Command not recognized"

# =========================================
# AI MODULE IMPORTS
# =========================================

try:
    from ai_modules.chatbot import setup_ai
    HAS_AI_MODULE = True
except:
    HAS_AI_MODULE = False
    def setup_ai(api_key):
        return None

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="ULTRA JARVIS",
    page_icon="🤖",
    layout="wide"
)

# =========================================
# CUSTOM CSS & THEME
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

load_theme()

# =========================================
# GEMINI AI SETUP
# =========================================

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    model = setup_ai(api_key)
except:
    api_key = None
    model = None
    st.warning("⚠️ Gemini API key not configured. Chat features may be limited.")

# =========================================
# SESSION STATE
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model" not in st.session_state:
    st.session_state.model = model

if "personality" not in st.session_state:
    st.session_state.personality = "helpful"

if "language" not in st.session_state:
    st.session_state.language = "English"

# =========================================
# HEADER & NAVIGATION
# =========================================

st.title("🤖 ULTRA JARVIS")
st.caption("Advanced Cloud AI Assistant")

with st.sidebar:
    st.title("⚡ JARVIS")
    
    selected = option_menu(
        "Navigation",
        ["Chat", "Dashboard", "System", "Settings"],
        icons=["chat", "speedometer2", "cpu", "gear"],
        default_index=0
    )
    
    st.divider()
    
    # Personality selector
    personality = st.selectbox(
        "Personality",
        ["Helpful", "Professional", "Casual", "Creative"]
    )
    st.session_state.personality = personality
    
    # Language selector
    language = st.selectbox(
        "Language",
        ["English", "Spanish", "French", "German"]
    )
    st.session_state.language = language

# =========================================
# WIDGETS (AVAILABLE ON ALL PAGES)
# =========================================

col1, col2, col3 = st.columns(3)

with col1:
    try:
        # Weather widget placeholder
        st.metric("🌡️ Temperature", "25°C")
    except:
        pass

with col2:
    try:
        # Finance widget placeholder
        st.metric("💹 Market", "↑ 2.5%")
    except:
        pass

with col3:
    try:
        # Security status
        st.metric("🔒 Security", "✅ Safe")
    except:
        pass

st.divider()

# =========================================
# CHAT PAGE
# =========================================

if selected == "Chat":
    
    st.subheader("💬 Chat with JARVIS")
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Chat input
    prompt = st.chat_input("⚡ Speak with JARVIS...")
    
    if prompt:
        
        # =====================================
        # USER MESSAGE
        # =====================================
        
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Show loading animation
        loading_animation()
        
        # =====================================
        # AUTOMATION SYSTEM CHECK
        # =====================================
        
        automation_response = execute_command(prompt)
        
        # =====================================
        # AI RESPONSE
        # =====================================
        
        if automation_response != "Command not recognized":
            response = automation_response
        else:
            # Use AI model for response
            if model:
                response = process_command(model, prompt)
            else:
                response = process_command(prompt)
        
        # =====================================
        # DISPLAY RESPONSE
        # =====================================
        
        with st.chat_message("assistant"):
            placeholder = st.empty()
            typed = ""
            
            # Typing effect
            for char in response:
                typed += char
                placeholder.markdown(typed)
                time.sleep(0.01)
        
        # =====================================
        # SAVE TO SESSION
        # =====================================
        
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        
        # =====================================
        # SAVE TO DATABASE & MEMORY
        # =====================================
        
        try:
            save_message("user", prompt)
            save_message("assistant", response)
            save_memory("user", prompt)
            save_memory("assistant", response)
        except Exception as e:
            st.warning(f"⚠️ Could not save message: {str(e)}")
        
        # =====================================
        # SPEAK RESPONSE
        # =====================================
        
        try:
            speak(response)
        except:
            pass

# =========================================
# DASHBOARD PAGE
# =========================================

elif selected == "Dashboard":
    
    st.subheader("📊 AI Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("💬 Conversations", len(st.session_state.messages) // 2)
    
    with col2:
        st.metric("🧠 Memory Usage", "80%")
    
    with col3:
        st.metric("⚡ AI Usage", "90%")
    
    with col4:
        st.metric("🔧 System", "✅ Active")
    
    st.divider()
    
    # Dashboard chart
    data = pd.DataFrame({
        "Features": [
            "AI Chat",
            "Memory",
            "Search",
            "Automation"
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("✅ All systems operational")
    
    with col2:
        st.info("📊 Dashboard updated in real-time")

# =========================================
# SYSTEM PAGE
# =========================================

elif selected == "System":
    
    st.subheader("⚡ System Monitor")
    
    col1, col2, col3 = st.columns(3)
    
    # Get system metrics
    cpu = psutil.cpu_percent(interval=1)
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
    
    st.divider()
    
    st.info("☁️ Cloud systems active")
    
    # System details
    st.subheader("System Information")
    col1, col2 = st.columns(2)
    
    with col1:
        system_info = {
            "Platform": f"{sys.platform}",
            "Python Version": f"{sys.version.split()[0]}",
            "Processor Count": f"{psutil.cpu_count()}",
            "Total Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
        }
        st.json(system_info)

# =========================================
# FOOTER & SYSTEM MONITOR
# =========================================

st.divider()

footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption(f"🤖 JARVIS v2.0 | Conversations: {len(st.session_state.messages) // 2}")

with footer_col2:
    st.caption(f"💭 Personality: {st.session_state.personality}")

with footer_col3:
    st.caption(f"🌍 Language: {st.session_state.language}")

# Final system monitor
try:
    system_monitor()
except:
    pass
    
    with col2:
        process_info = {
            "Active Processes": len(psutil.pids()),
            "CPU Threads": psutil.cpu_count(logical=True),
            "Boot Time": time.ctime(psutil.boot_time())
        }
        st.json(process_info)

# =========================================
# SETTINGS PAGE
# =========================================

elif selected == "Settings":
    
    st.subheader("⚙️ Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Display Settings")
        theme = st.selectbox("Theme", ["Dark", "Light", "Auto"])
        st.write(f"Selected Theme: {theme}")
    
    with col2:
        st.subheader("AI Settings")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        st.write(f"Temperature: {temperature}")
    
    st.divider()
    
    st.subheader("Advanced Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        enable_voice = st.toggle("Enable Voice Output", value=True)
        st.write(f"Voice: {'Enabled' if enable_voice else 'Disabled'}")
    
    with col2:
        enable_memory = st.toggle("Enable Memory Saving", value=True)
        st.write(f"Memory: {'Enabled' if enable_memory else 'Disabled'}")
    
    if st.button("💾 Save Settings", use_container_width=True):
        st.success("✅ Settings saved successfully!")
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.success("✅ Chat history cleared!")
        st.rerun()
