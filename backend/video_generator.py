from moviepy import (
    ImageClip,
    concatenate_videoclips
)

from PIL import Image
import requests
from io import BytesIO
import uuid
import os

# =========================================
# VIDEO GENERATOR
# =========================================

def generate_video(prompt, duration=10):

    try:

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

        # CLEAN PROMPT

        clean_prompt = (
            prompt.lower()
            .replace("create video of", "")
            .replace("generate video of", "")
            .replace("make video of", "")
            .strip()
        )

        clips = []

        # NUMBER OF SCENES

        total_scenes = max(1, duration // 3)

        for i in range(total_scenes):

            image_url = (
                "https://image.pollinations.ai/prompt/"
                + clean_prompt.replace(" ", "%20")
                + f"%20scene{i}"
            )

            response = requests.get(
                image_url,
                timeout=60
            )

            image = Image.open(
                BytesIO(response.content)
            )

            image_path = (
                f"generated_videos/{uuid.uuid4()}.png"
            )

            image.save(image_path)

            clip = (
                ImageClip(image_path)
                .with_duration(3)
            )

            clips.append(clip)

        # FINAL VIDEO

        final_clip = concatenate_videoclips(
            clips,
            method="compose"
        )

        video_path = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        final_clip.write_videofile(
            video_path,
            fps=24
        )

        return video_path

    except Exception as e:

        print("VIDEO ERROR:", e)

        return None