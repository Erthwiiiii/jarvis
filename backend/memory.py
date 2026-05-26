import json
import os

MEMORY_FILE = "memory.json"

# =====================================

def load_memory():

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:

            json.dump([], file)

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    except:

        return []

# =====================================

def save_memory(role, message):

    data = load_memory()

    data.append({

        "role": role,
        "message": message
    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)