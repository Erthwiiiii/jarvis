import streamlit as st


def video_uploader_section():

    st.subheader("🎥 Upload Video")

    uploaded_video = st.file_uploader(

        "Upload Video",

        type=[
            "mp4",
            "mov",
            "avi"
        ]
    )

    if uploaded_video is not None:

        st.video(uploaded_video)

        st.success(
            "Video uploaded successfully!"
        )
