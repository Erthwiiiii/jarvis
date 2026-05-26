import webbrowser
import os

# ======================================

def execute_command(command):

    command = command.lower()

    # ======================================

    if "youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    # ======================================

    elif "google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google"

    # ======================================

    elif "github" in command:

        webbrowser.open("https://github.com")

        return "Opening GitHub"

    # ======================================

    elif "notepad" in command:

        os.system("notepad")

        return "Opening Notepad"

    # ======================================

    elif "cmd" in command:

        os.system("start cmd")

        return "Opening Command Prompt"

    # ======================================

    elif "shutdown" in command:

        os.system("shutdown /s /t 5")

        return "Shutting down system"

    # ======================================

    else:

        return "Command not recognized"