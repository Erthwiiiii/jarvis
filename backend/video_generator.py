from moviepy.editor import ImageClip
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

        os.makedirs(
            "temp_images",
            exist_ok=True
        )

        # CLEAN PROMPT

        clean_prompt = (
            prompt.lower()
            .replace("create video of", "")
            .replace("generate video of", "")
            .replace("create video", "")
            .replace("generate video", "")
            .strip()
        )

        # IMAGE API

        image_url = (
            "https://image.pollinations.ai/prompt/"
            + clean_prompt.replace(" ", "%20")
        )

        response = requests.get(
            image_url,
            timeout=60
        )

        image = Image.open(
            BytesIO(response.content)
        )

        # SAVE IMAGE

        image_path = (
            f"temp_images/{uuid.uuid4()}.png"
        )

        image.save(image_path)

        # CREATE VIDEO

        clip = (
            ImageClip(image_path)
            .set_duration(duration)
        )

        output_path = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        clip.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio=False
        )

        return output_path

    except Exception as e:

        print("VIDEO ERROR:", e)

        return None
