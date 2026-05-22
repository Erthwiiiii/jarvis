from PIL import Image
import streamlit as st

def show_image(uploaded):

    image = Image.open(uploaded)

    st.image(
        image,
        use_container_width=True
    )