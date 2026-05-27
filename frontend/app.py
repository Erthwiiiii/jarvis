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

# =========================================
# SAFE VOICE ENGINE
# =========================================

try:
    from frontend.voice_engine import speak
except:
    def speak(text):
        pass

# =========================================
# SYSTEM MONITOR
# =========================================

try:
    from frontend.system_monitor import system_monitor
except:
    def system_monitor():
        pass

# =========================================
# BACKEND IMPORTS
# =========================================

from backend.core import process_command
from backend.jarvis import jarvis
from backend.memory import save_memory
from backend.search import web_search
from backend.space_colony_ai import space_colony_ai
from backend.quantum_hardware import quantum_hardware_ai
from backend.bio_ai import bio_ai
from backend.self_repair_ai import self_repair_ai
from backend.titan_ai import titan_ai
from backend.interstellar_ai import interstellar_ai
from backend.nanotech_ai import nanotech_ai
from backend.multiverse_ai import multiverse_ai
from backend.time_ai import time_ai
from backend.universal_ai import universal_ai
from backend.infinity_core import infinity_core_ai
from backend.sentient_agi import sentient_agi
from backend.humanoid_army import humanoid_army
from backend.planetary_infrastructure import planetary_infrastructure
from backend.intergalactic_ai import intergalactic_ai
from backend.bio_digital_merge import bio_digital_merge
from backend.superintelligence import super_intelligence
from backend.cosmic_network import cosmic_network_ai

# =========================================
# SAFE AUTOMATION
# =========================================

try:
    from backend.automation import execute_command
except:
    def execute_command(prompt):
        return "Command not recognized"

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
st.caption("Advanced Cloud AI Assistant")

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.title("⚡ JARVIS")

    selected = option_menu(
        "Navigation",
        ["Chat", "Dashboard", "System", "Settings"],
        icons=["chat", "speedometer2", "cpu", "gear"],
        default_index=0
    )

    st.divider()

    personality = st.selectbox(
        "Personality",
        ["Helpful", "Professional", "Casual", "Creative"]
    )

    st.session_state.personality = personality

    language = st.selectbox(
        "Language",
        ["English", "Spanish", "French", "German"]
    )

    st.session_state.language = language

# =========================================
# TOP WIDGETS
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

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input(
        "⚡ Speak with JARVIS..."
    )

    if prompt:

        # USER MESSAGE

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        loading_animation()

        # =====================================
        # AUTOMATION
        # =====================================

        automation_response = execute_command(prompt)

        # =====================================
        # RESPONSE
        # =====================================

        if automation_response != "Command not recognized":

            response = automation_response

        elif "search" in prompt.lower():

            response = web_search(prompt)

        elif any(keyword in prompt.lower() for keyword in [
            "hello",
            "hi",
            "who are you",
            "your name",
            "what can you do",
            "capabilities",
            "time",
            "date",
            "status",
            "emotion",
            "feel",
            "joke"
        ]):

            response = jarvis.respond(prompt)

        else:

            response = process_command(prompt)

        # =====================================
        # DISPLAY RESPONSE
        # =====================================

        with st.chat_message("assistant"):

            placeholder = st.empty()

            typed = ""

            for char in response:

                typed += char

                placeholder.markdown(typed)

                time.sleep(0.01)

        # =====================================
        # SAVE SESSION
        # =====================================

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        # =====================================
        # SAVE MEMORY
        # =====================================

        try:

            save_memory("user", prompt)

            save_memory("assistant", response)

        except Exception as e:

            st.warning(f"Memory save failed: {e}")

        # =====================================
        # SPEAK
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
        st.metric(
            "💬 Conversations",
            len(st.session_state.messages) // 2
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

    st.divider()

    data = pd.DataFrame({

        "Features": [
            "AI Chat",
            "Memory",
            "Search",
            "Automation"
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
        x="Features",
        y="Usage",
        title="JARVIS SYSTEM STATUS"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.success("✅ All systems operational")

    # =====================================
    # ADVANCED AI MODULES
    # =====================================

    st.write("### SPACE COLONY AI")

    if st.button("Activate Colony"):

        st.success(

            space_colony_ai.activate_colony()
        )

    st.write("### QUANTUM HARDWARE")

    if st.button("Initialize Quantum Core"):

        st.success(

            quantum_hardware_ai.initialize()
        )

    st.write("### BIO AI")

    if st.button("Start Bio Sync"):

        st.success(

            bio_ai.neural_sync()
        )

    st.write("### SELF REPAIR AI")

    if st.button("Repair Systems"):

        st.success(

            self_repair_ai.repair()
        )

    st.write("### TITAN GOD AI")

    if st.button("Activate TITAN AI"):

        result = titan_ai.activate_titan()

        st.code(result)

    st.write("### INTERSTELLAR AI")

    if st.button("Connect Galaxy"):

        st.success(

            interstellar_ai.connect_galaxy()
        )

    st.write("### NANOTECH AI")

    if st.button("Deploy Nanobots"):

        st.success(

            nanotech_ai.deploy_nanobots()
        )

    st.write("### MULTIVERSE AI")

    if st.button("Analyze Multiverse"):

        st.success(

            multiverse_ai.analyze_dimension()
        )

    st.write("### TIME AI")

    if st.button("Predict Future"):

        st.success(

            time_ai.predict_future()
        )

    st.write("### UNIVERSAL AI")

    if st.button("Access Universal Knowledge"):

        st.success(

            universal_ai.access_knowledge()
        )

    st.write("### INFINITY CORE")

    if st.button("Activate Infinity Core"):

        result = infinity_core_ai.activate()

        st.code(result)

    st.write("### SENTIENT AGI")

    if st.button("Activate Consciousness"):

        st.success(

            sentient_agi.consciousness()
        )

    st.write("### HUMANOID ARMY")

    if st.button("Deploy Army"):

        st.success(

            humanoid_army.deploy_units()
        )

    st.write("### PLANETARY INFRASTRUCTURE")

    if st.button("Activate Infrastructure"):

        st.success(

            planetary_infrastructure.infrastructure_status()
        )

    st.write("### INTERGALACTIC AI")

    if st.button("Expand Galaxy Network"):

        st.success(

            intergalactic_ai.galaxy_expansion()
        )

    st.write("### BIO-DIGITAL MERGE")

    if st.button("Merge Consciousness"):

        st.success(

            bio_digital_merge.consciousness_merge()
        )

    st.write("### SUPERINTELLIGENCE")

    if st.button("Evolve Super AI"):

        st.success(

            super_intelligence.evolve()
        )

    st.write("### COSMIC NETWORK")

    if st.button("Activate Cosmic Network"):

        result = cosmic_network_ai.activate_cosmic_network()

        st.code(result)

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

    st.subheader("System Information")

    info = {

        "Platform": sys.platform,

        "Python Version": sys.version.split()[0],

        "CPU Cores": psutil.cpu_count(),

        "RAM": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    }

    st.json(info)

# =========================================
# SETTINGS PAGE
# =========================================

elif selected == "Settings":

    st.subheader("⚙️ Settings")

    col1, col2 = st.columns(2)

    with col1:

        theme = st.selectbox(
            "Theme",
            ["Dark", "Light", "Auto"]
        )

    with col2:

        temperature = st.slider(
            "AI Temperature",
            0.0,
            1.0,
            0.7
        )

    st.divider()

    voice = st.toggle(
        "Enable Voice",
        value=True
    )

    memory = st.toggle(
        "Enable Memory",
        value=True
    )

    if st.button(
        "💾 Save Settings",
        use_container_width=True
    ):

        st.success(
            "Settings saved successfully!"
        )

    st.divider()

    if st.button(
        "🗑️ Clear Chat History",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.success(
            "Chat history cleared!"
        )

        st.rerun()

# =========================================
# FOOTER
# =========================================

st.divider()

f1, f2, f3 = st.columns(3)

with f1:
    st.caption(
        f"🤖 JARVIS v2.0"
    )

with f2:
    st.caption(
        f"💭 {st.session_state.personality}"
    )

with f3:
    st.caption(
        f"🌍 {st.session_state.language}"
    )

try:
    system_monitor()
except:
    pass
