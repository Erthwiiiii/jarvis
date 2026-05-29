from moviepy import (
    TextClip,
    ColorClip,
    CompositeVideoClip
)

import os
import uuid

# =========================================
# VIDEO GENERATOR
# =========================================

def generate_video(prompt):

    try:

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

        # CLEAN PROMPT

        text = (
            prompt
            .replace("create video of", "")
            .replace("generate video of", "")
            .strip()
        )

        # BACKGROUND

        background = ColorClip(
            size=(1280, 720),
            color=(0, 0, 0),
            duration=5
        )

        # TEXT

        txt_clip = TextClip(
            text=text,
            font_size=60,
            color="white",
            size=(1000, 500),
            method="caption"
        )

        txt_clip = txt_clip.with_position(
            "center"
        ).with_duration(5)

        # FINAL VIDEO

        final = CompositeVideoClip([
            background,
            txt_clip
        ])

        filename = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        final.write_videofile(
            filename,
            fps=24
        )

        return filename

    except Exception as e:

        print(f"Video Error: {e}")

        return None