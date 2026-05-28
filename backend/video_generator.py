from moviepy import ImageClip
import os
import uuid

from backend.image_generator import generate_image

# =========================================
# VIDEO GENERATOR
# =========================================

def generate_video(prompt):

    os.makedirs(
        "generated_videos",
        exist_ok=True
    )

    # GENERATE IMAGE

    image_path = generate_image(prompt)

    # CREATE VIDEO

    clip = (
        ImageClip(image_path)
        .with_duration(5)
    )

    # ADD ZOOM EFFECT

    clip = clip.resized(
        lambda t: 1 + 0.02 * t
    )

    video_path = (
        f"generated_videos/{uuid.uuid4()}.mp4"
    )

    clip.write_videofile(
        video_path,
        fps=24
    )

    return video_path