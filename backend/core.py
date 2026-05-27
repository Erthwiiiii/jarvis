import random
import webbrowser
from datetime import datetime

# ==========================================
# SMART JARVIS REPLIES
# ==========================================

greetings = [

    "Yes sir?",
    "I'm here sir.",
    "Ready for your command.",
    "At your service.",
    "How can I help you sir?"
]

# ==========================================
# MAIN AI ENGINE
# ==========================================

def process_command(prompt):

    prompt = prompt.lower()

    # ======================================
    # GREETINGS
    # ======================================

    if "hey jarvis" in prompt or "hello jarvis" in prompt:

        return random.choice(greetings)

    # ======================================
    # OPEN YOUTUBE
    # ======================================

    elif "open youtube" in prompt:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube sir."

    # ======================================
    # OPEN GOOGLE
    # ======================================

    elif "open google" in prompt:

        webbrowser.open("https://google.com")

        return "Opening Google sir."

    # ======================================
    # OPEN CHATGPT
    # ======================================

    elif "open chatgpt" in prompt:

        webbrowser.open("https://chat.openai.com")

        return "Opening ChatGPT."

    # ======================================
    # TIME
    # ======================================

    elif "time" in prompt:

        current = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current}"

    # ======================================
    # DATE
    # ======================================

    elif "date" in prompt:

        today = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {today}"

    # ======================================
    # WHO ARE YOU
    # ======================================

    elif "who are you" in prompt:

        return "I am JARVIS, your advanced AI assistant."

    # ======================================
    # EXIT
    # ======================================

    elif "shutdown" in prompt or "exit" in prompt:

        return "Shutting down systems sir."

    # ======================================
    # DEFAULT AI RESPONSE
    # ======================================

    else:

        return f"I understood your command: {prompt}"
