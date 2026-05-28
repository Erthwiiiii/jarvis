from PIL import Image
import requests
from io import BytesIO
import uuid
import os


# =========================================
# AI IMAGE GENERATOR
# =========================================

def generate_image(prompt):

    # Create folder

    os.makedirs(
        "generated_images",
        exist_ok=True
    )

    # Remove command words

    clean_prompt = (
        prompt
        .replace("create image of", "")
        .replace("generate image of", "")
        .strip()
    )

    # AI IMAGE URL

    image_url = (
        "https://image.pollinations.ai/prompt/"
        + clean_prompt.replace(" ", "%20")
    )

    # Download image

    response = requests.get(image_url)

    image = Image.open(
        BytesIO(response.content)
    )

    # Save image

    filename = (
        f"generated_images/{uuid.uuid4()}.png"
    )

    image.save(filename)

    return filename
