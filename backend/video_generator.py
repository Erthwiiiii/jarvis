from moviepy import *
from PIL import Image, ImageDraw

def generate_video(prompt):

    prompt = prompt.replace(
        "create video of",
        ""
    )

    prompt = prompt.strip()

    image = Image.new(
        "RGB",
        (1280, 720),
        color=(15, 15, 15)
    )

    draw = ImageDraw.Draw(image)

    draw.text(
        (100, 300),
        prompt,
        fill=(255, 255, 255)
    )

    image_path = "video_frame.png"

    image.save(image_path)

    clip = ImageClip(image_path)

    clip = clip.with_duration(5)

    clip = clip.resized(width=1280)

    video_path = "generated_video.mp4"

    clip.write_videofile(
        video_path,
        fps=24
    )

    return video_path
