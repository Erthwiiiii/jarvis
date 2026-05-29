import json
import os

MEMORY_FILE = "memory.json"

def save_memory(role, content):

    data = []

    if os.path.exists(MEMORY_FILE):

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

        except:
            data = []

    data.append({
        "role": role,
        "content": content
    })

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_memory():

    if os.path.exists(MEMORY_FILE):

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except:
            return []

    return []