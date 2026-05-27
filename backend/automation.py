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

        return "Notepad command received. This environment does not support opening local applications."

    # ======================================

    elif "cmd" in command or "command prompt" in command:

        return "Terminal access is restricted in this environment."

    # =====================================

    elif "shutdown" in command or "restart" in command:

        return "I cannot execute shutdown or restart commands here."

    # ======================================

    else:

        return "Command not recognized"