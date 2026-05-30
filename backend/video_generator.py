from moviepy.editor import ImageClip
from PIL import Image
from io import BytesIO
import requests
import uuid
import os

def generate_video(prompt, duration=10):

    try:

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

        image_url = (
            "https://image.pollinations.ai/prompt/"
            + prompt.replace(" ", "%20")
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

        clip = ImageClip(
            image_path
        ).set_duration(duration)

        output = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        clip.write_videofile(
            output,
            fps=24
        )

        return output

    except Exception as e:

        print(
            "VIDEO ERROR:",
            e
        )

        return None