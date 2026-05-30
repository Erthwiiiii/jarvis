import os
import uuid
import requests
from io import BytesIO
from PIL import Image

import imageio_ffmpeg

os.environ["IMAGEIO_FFMPEG_EXE"] = imageio_ffmpeg.get_ffmpeg_exe()

from moviepy.editor import ImageClip

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
            verbose=False
        )

        print("VIDEO SAVED")

        return output_path

    except Exception as e:

        print("VIDEO ERROR:", str(e))

        return None
