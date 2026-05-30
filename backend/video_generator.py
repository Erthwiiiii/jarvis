import os
import uuid
import requests
import imageio_ffmpeg

from io import BytesIO
from PIL import Image

os.environ["FFMPEG_BINARY"] = imageio_ffmpeg.get_ffmpeg_exe()

from moviepy.editor import ImageClip

def generate_video(prompt, duration=10):

try:

    print("VIDEO GENERATION STARTED")

    os.makedirs(
        "generated_videos",
        exist_ok=True
    )

    clean_prompt = (
        prompt
        .replace("create video of", "")
        .replace("generate video of", "")
        .replace("video of", "")
        .strip()
    )

    if not clean_prompt:
        clean_prompt = "lion in jungle"

    image_url = (
        "https://image.pollinations.ai/prompt/"
        + clean_prompt.replace(" ", "%20")
    )

    print("DOWNLOADING IMAGE")

    response = requests.get(
        image_url,
        timeout=120
    )

    response.raise_for_status()

    image = Image.open(
        BytesIO(response.content)
    ).convert("RGB")

    image_path = os.path.join(
        "generated_videos",
        f"{uuid.uuid4()}.png"
    )

    image.save(image_path)

    output_path = os.path.join(
        "generated_videos",
        f"{uuid.uuid4()}.mp4"
    )

    clip = ImageClip(image_path)

    clip = clip.set_duration(duration)

    clip.write_videofile(
        output_path,
        fps=24,
        codec="libx264",
        audio=False,
        logger=None
    )

    clip.close()

    print("VIDEO SAVED:", output_path)

    return output_path

except Exception as e:

    print("VIDEO ERROR:", str(e))

    return None
