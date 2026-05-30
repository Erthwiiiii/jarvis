import os
import uuid
import requests

def generate_video(prompt, duration=5, output_dir="generated_videos"):
if not isinstance(prompt, str) or not prompt.strip():
raise ValueError("prompt must be a non-empty string")

if duration <= 0:
    raise ValueError("duration must be a positive number")

os.makedirs(output_dir, exist_ok=True)

payload = {
    "prompt": prompt,
    "duration": duration,
}

url = "https://video.pollinations.ai/generate"

try:
    response = requests.post(
        url,
        json=payload,
        timeout=300,
        stream=True
    )

    response.raise_for_status()

except requests.RequestException as exc:

    print("VIDEO ERROR:", exc)
    return None

filename = os.path.join(
    output_dir,
    f"{uuid.uuid4()}.mp4"
)

try:

    with open(filename, "wb") as f:

        for chunk in response.iter_content(
            chunk_size=8192
        ):

            if chunk:
                f.write(chunk)

except OSError as exc:

    print("VIDEO SAVE ERROR:", exc)
    return None

return filename
