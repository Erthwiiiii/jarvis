import json
import os

MEMORY_FILE = "memory.json"

# ======================================

def load_memory():

    # Create file if not exists

    if not os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "w") as file:

            json.dump([], file)

    # Read safely

    try:

        with open(MEMORY_FILE, "r") as file:

            content = file.read().strip()

            if not content:

                return []

            return json.loads(content)

    except:

        return []

# ======================================

def save_memory(role, message):

    data = load_memory()

    data.append({

        "role": role,
        "message": message
    })

    with open(MEMORY_FILE, "w") as file:

        json.dump(data, file, indent=4)