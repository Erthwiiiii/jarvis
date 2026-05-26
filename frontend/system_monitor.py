import psutil
import streamlit as st

def system_monitor():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    st.sidebar.markdown("## 💻 System Monitor")

    st.sidebar.write(f"CPU Usage: {cpu}%")

    st.sidebar.write(f"RAM Usage: {ram}%")

    st.sidebar.write(f"Disk Usage: {disk}%")