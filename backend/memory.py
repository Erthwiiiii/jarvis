import json
import os

# =========================================
# MEMORY FILE
# =========================================

MEMORY_FILE = "memory.json"

# =========================================
# CREATE FILE IF NOT EXISTS
# =========================================

if not os.path.exists(MEMORY_FILE):

    with open(MEMORY_FILE, "w") as file:

        json.dump([], file)

# =========================================
# SAVE MEMORY
# =========================================

def save_memory(role, content):

    try:

        # LOAD OLD MEMORY

        try:

            with open(MEMORY_FILE, "r") as file:

                data = json.load(file)

        except:

            data = []

        # APPEND NEW DATA

        data.append({

            "role": role,
            "content": content

        })

        # SAVE AGAIN

        with open(MEMORY_FILE, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    except Exception as e:

        print("MEMORY SAVE ERROR:", e)

# =========================================
# LOAD MEMORY
# =========================================

def load_memory():

    try:

        with open(MEMORY_FILE, "r") as file:

            return json.load(file)

    except:

        return []