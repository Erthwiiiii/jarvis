from PIL import Image, ImageDraw
import os
import time

def generate_image(prompt):

    os.makedirs(
        "generated_images",
        exist_ok=True
    )

    filename = f"image_{int(time.time())}.png"

    filepath = os.path.join(
        "generated_images",
        filename
    )

    img = Image.new(
        "RGB",
        (1024, 1024),
        color=(20, 20, 20)
    )

    draw = ImageDraw.Draw(img)

    draw.text(
        (100, 500),
        f"AI IMAGE:\n{prompt}",
        fill=(0, 255, 255)
    )

    img.save(filepath)

    return filepath
