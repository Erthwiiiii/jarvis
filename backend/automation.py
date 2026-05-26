import webbrowser

# ======================================

def execute_command(command):

    command = command.lower()

    # ======================================

    if "youtube" in command:

        return "Opening YouTube is disabled on Render server"

    # ======================================

    elif "google" in command:

        return "Opening Google is disabled on Render server"

    # ======================================

    elif "github" in command:

        return "Opening GitHub is disabled on Render server"

    # ======================================

    elif "screenshot" in command:

        return "Screenshot feature disabled on Render"

    # ======================================

    else:

        return "Command not recognized"