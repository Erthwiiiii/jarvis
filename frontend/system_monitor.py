import streamlit as st
import psutil

# ======================================

def system_monitor():

    st.subheader("🖥️ System Monitor")

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    battery = psutil.sensors_battery()

    st.metric("CPU Usage", f"{cpu}%")

    st.metric("RAM Usage", f"{ram}%")

    if battery:

        st.metric(
            "Battery",
            f"{battery.percent}%"
        )