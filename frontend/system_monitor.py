import streamlit as st
import psutil

def system_monitor():

    cpu = psutil.cpu_percent()

    ram = psutil.virtual_memory().percent

    st.sidebar.markdown(
        "## 💻 System Monitor"
    )

    st.sidebar.write(
        f"CPU Usage: {cpu}%"
    )

    st.sidebar.progress(
        cpu / 100
    )

    st.sidebar.write(
        f"RAM Usage: {ram}%"
    )

    st.sidebar.progress(
        ram / 100
    )