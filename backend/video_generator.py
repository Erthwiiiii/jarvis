from moviepy.editor import ImageClip
from PIL import Image, ImageDraw
import os
import time

def generate_video(prompt):

    os.makedirs(
        "generated_videos",
        exist_ok=True
    )

    image_path = f"generated_videos/frame_{int(time.time())}.png"

    # CREATE IMAGE

    img = Image.new(
        "RGB",
        (1280, 720),
        color=(10, 10, 10)
    )

    draw = ImageDraw.Draw(img)

    draw.text(
        (150, 300),
        f"AI VIDEO\n{prompt}",
        fill=(0, 255, 255)
    )

    img.save(image_path)

    # CREATE VIDEO

    clip = ImageClip(image_path).set_duration(5)

    video_path = f"generated_videos/video_{int(time.time())}.mp4"

    clip.write_videofile(
        video_path,
        fps=24
    )

    return video_path
