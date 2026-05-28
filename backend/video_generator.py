from moviepy import ImageClip
from backend.image_generator import generate_image
import uuid
import os


# =========================================
# VIDEO GENERATOR
# =========================================

def generate_video(prompt):

    # =====================================
    # CREATE OUTPUT FOLDER
    # =====================================

    os.makedirs(
        "generated_videos",
        exist_ok=True
    )

    # =====================================
    # GENERATE AI IMAGE
    # =====================================

    image_path = generate_image(prompt)

    # =====================================
    # CREATE VIDEO CLIP
    # =====================================

    clip = ImageClip(
        image_path
    ).with_duration(5)

    # =====================================
    # OUTPUT FILE
    # =====================================

    filename = (
        f"generated_videos/{uuid.uuid4()}.mp4"
    )

    # =====================================
    # EXPORT VIDEO
    # =====================================

    clip.write_videofile(

        filename,

        fps=24,

        codec="libx264",

        audio=False
    )

    # =====================================
    # RETURN VIDEO PATH
    # =====================================

    return filename
