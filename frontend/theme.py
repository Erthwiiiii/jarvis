import streamlit as st

def load_theme():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Orbitron', sans-serif;
        background-color: #020617;
        color: white;
    }

    .stApp{
        background:
        linear-gradient(
        135deg,
        #020617,
        #07111f,
        #000814
        );
    }

    h1,h2,h3{
        color:#00e5ff;
        text-shadow:
        0 0 10px #00e5ff,
        0 0 20px #00e5ff;
    }

    .jarvis-card{
        background:rgba(0,0,0,0.4);
        border:1px solid cyan;
        border-radius:15px;
        padding:20px;
        margin-bottom:10px;
        box-shadow:
        0 0 15px rgba(0,229,255,0.4);
    }

    .stButton>button{
        background:
        linear-gradient(
        90deg,
        #00e5ff,
        #0077ff
        );

        color:black;
        border:none;
        border-radius:10px;
        font-weight:bold;
    }

    </style>
    """, unsafe_allow_html=True)