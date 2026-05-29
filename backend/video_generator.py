import requests
import uuid
import os

# =========================================
# AI VIDEO GENERATOR
# =========================================

def generate_video(prompt):

    try:

        os.makedirs(
            "generated_videos",
            exist_ok=True
        )

        # CLEAN PROMPT

        clean_prompt = (
            prompt
            .replace("create video of", "")
            .replace("generate video of", "")
            .strip()
        )

        # AI VIDEO URL

        video_url = (
            "https://pollinations.ai/p/"
            + clean_prompt.replace(" ", "%20")
            + "?model=video"
        )

        # DOWNLOAD VIDEO

        response = requests.get(
            video_url,
            stream=True
        )

        # SAVE VIDEO

        filename = (
            f"generated_videos/{uuid.uuid4()}.mp4"
        )

        with open(filename, "wb") as file:

            for chunk in response.iter_content(
                chunk_size=1024
            ):

                if chunk:

                    file.write(chunk)

        return filename

    except Exception as e:

        print(f"Video Error: {e}")

        return None