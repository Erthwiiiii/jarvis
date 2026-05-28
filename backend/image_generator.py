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

    # =====================================
    # CLEAN PROMPT
    # =====================================

    clean_prompt = (
        prompt.lower()
        .replace("create image of", "")
        .replace("generate image of", "")
        .replace("make image of", "")
        .replace("draw", "")
        .strip()
    )

    # =====================================
    # IMAGE URL
    # =====================================

    image_url = (
        "https://image.pollinations.ai/prompt/"
        + clean_prompt.replace(" ", "%20")
    )

    # =====================================
    # DOWNLOAD IMAGE
    # =====================================

    response = requests.get(image_url)

    # =====================================
    # OPEN IMAGE
    # =====================================

    image = Image.open(
        BytesIO(response.content)
    )

    # =====================================
    # SAVE IMAGE
    # =====================================

    filename = (
        f"generated_images/{uuid.uuid4()}.png"
    )

    image.save(filename)

    # =====================================
    # RETURN PATH
    # =====================================

    return filename
