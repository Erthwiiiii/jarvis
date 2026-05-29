from PIL import Image
import requests
from io import BytesIO
import uuid
import os

# =========================================
# IMAGE GENERATOR
# =========================================

def generate_image(prompt):

    try:

        # CREATE FOLDER

        os.makedirs(
            "generated_images",
            exist_ok=True
        )

        # CLEAN PROMPT  
         
         clean_prompt = (
            prompt
           .replace("create image of", "")
           .replace("generate image of", "")
           .replace("image of", "")
           .strip()
      )

      # =========================================
      # ADD AI QUALITY BOOST
      # =========================================

      clean_prompt += (
           ", ultra realistic, cinematic lighting, "
           "high quality, detailed, 4k, masterpiece"
      )

        # IMAGE URL

        image_url = (
            "https://image.pollinations.ai/prompt/"
            + clean_prompt.replace(" ", "%20")
        )

        # DOWNLOAD IMAGE

        response = requests.get(
            image_url,
            timeout=60
        )

        # CHECK ERROR

        if response.status_code != 200:

            raise Exception(
                "Image API failed"
            )

        # OPEN IMAGE

        image = Image.open(
            BytesIO(response.content)
        )

        # SAVE IMAGE

        filename = (
            f"generated_images/{uuid.uuid4()}.png"
        )

        image.save(filename)

        return filename

    except Exception as e:

        print("IMAGE ERROR:", e)

        return None