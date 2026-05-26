import pyautogui
import webbrowser
import os

def execute_command(command):

    command = command.lower()

    if "youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    elif "google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google"

    elif "notepad" in command:

        os.system("notepad")

        return "Opening Notepad"

    elif "screenshot" in command:

        img = pyautogui.screenshot()

        img.save("screenshot.png")

        return "Screenshot taken"

    else:

        return "Command not recognized"