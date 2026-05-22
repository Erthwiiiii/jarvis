import streamlit as st

def loading_animation():

    st.markdown("""

    <div style='
    text-align:center;
    color:cyan;
    font-size:24px;
    animation: pulse 1s infinite;
    '>

    ⚡ JARVIS PROCESSING ⚡

    </div>

    """, unsafe_allow_html=True)