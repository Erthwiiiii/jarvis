import streamlit as st
from PIL import Image
import cv2


def camera_input_section():

    st.subheader("📷 Camera")

    image = st.camera_input(
        "Take a photo"
    )

    if image is not None:

        st.image(image)

        st.success(
            "Photo captured successfully!"
        )
