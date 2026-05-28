from moviepy import (
    TextClip,
    ColorClip,
    CompositeVideoClip
)

import uuid
import os

# =========================================
# VIDEO GENERATOR
# =========================================

def generate_video(prompt):

    os.makedirs(
        "generated_videos",
        exist_ok=True
    )

    text = (
        prompt
        .replace("create video", "")
        .replace("generate video", "")
        .strip()
    )

    background = ColorClip(
        size=(1280, 720),
        color=(20, 20, 20),
        duration=5
    )

    txt_clip = TextClip(
        text,
        fontsize=60,
        color="white",
        size=(1000, 500),
        method="caption"
    )

    txt_clip = txt_clip.set_position(
        "center"
    ).set_duration(5)

    final_video = CompositeVideoClip(
        [background, txt_clip]
    )

    filename = (
        f"generated_videos/{uuid.uuid4()}.mp4"
    )

    final_video.write_videofile(
        filename,
        fps=24
    )

    return filename