import streamlit as st
import time

def render_chat(role, text):

    with st.chat_message(role):

        stream = st.empty()

        final = ""

        for word in text.split():

            final += word + " "

            stream.markdown(final + "▌")

            time.sleep(0.01)

        stream.markdown(final)