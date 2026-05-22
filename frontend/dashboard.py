import streamlit as st
import pandas as pd
import random
import plotly.express as px

def render_dashboard():

    st.subheader("📊 JARVIS ANALYTICS")

    cpu = random.randint(20,90)
    ram = random.randint(20,90)
    ai = random.randint(80,100)

    df = pd.DataFrame({

        "System":[
            "CPU",
            "RAM",
            "AI"
        ],

        "Usage":[
            cpu,
            ram,
            ai
        ]
    })

    fig = px.bar(
        df,
        x="System",
        y="Usage",
        title="LIVE SYSTEM STATUS"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )