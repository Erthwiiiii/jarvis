from moviepy.editor import ImageClip
from PIL import Image
from io import BytesIO
import requests
import uuid
import os

def generate_video(prompt, duration=10):

    try:

        print("VIDEO STARTED")

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

        clean_prompt = (
            prompt
            .replace("create video of", "")
            .replace("generate video of", "")
            .strip()
        )

        image_url = (
            "https://image.pollinations.ai/prompt/"
            + clean_prompt.replace(" ", "%20")
        )

        print("DOWNLOADING IMAGE")

        response = requests.get(
            image_url,
            timeout=60
        )

        response.raise_for_status()

        image = Image.open(
            BytesIO(response.content)
        )

        image_path = (
            f"generated_videos/{uuid.uuid4()}.png"
        )

        image.save(image_path)

        print("IMAGE SAVED")

        clip = (
            ImageClip(image_path)
            .set_duration(duration)
        )

        output_path = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        print("WRITING VIDEO")

        clip.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio=False,
            logger=None
        )

        print("VIDEO SAVED")

        return output_path

    except Exception as e:

        print("VIDEO ERROR:", str(e))

        return None
