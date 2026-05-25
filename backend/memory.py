import json
import os

MEMORY_FILE = "database/memory.json"

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return []

    with open(MEMORY_FILE, "r") as file:

        return json.load(file)

def save_memory(role, message):

    data = load_memory()

    data.append({

        "role": role,
        "message": message
    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )