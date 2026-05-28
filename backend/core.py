import wikipedia
import pyjokes
import webbrowser
from datetime import datetime

# =========================================
# MAIN AI COMMAND PROCESSOR
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # GREETING
    # =====================================

    if (
        "hello" in prompt
        or "hey jarvis" in prompt
        or "hi" in prompt
    ):

        return "Hello sir, how can I help you?"

    # =====================================
    # TIME
    # =====================================

    elif "time" in prompt:

        current_time = datetime.now().strftime(
            "%I:%M %p"
        )

        return (
            f"Sir, current time is {current_time}"
        )

    # =====================================
    # DATE
    # =====================================

    elif "date" in prompt:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )

        return (
            f"Today's date is {current_date}"
        )

    # =====================================
    # JOKES
    # =====================================

    elif "joke" in prompt:

        return pyjokes.get_joke()

    # =====================================
    # OPEN YOUTUBE
    # =====================================

    elif "open youtube" in prompt:

        webbrowser.open(
            "https://youtube.com"
        )

        return "Opening YouTube sir."

    # =====================================
    # OPEN GOOGLE
    # =====================================

    elif "open google" in prompt:

        webbrowser.open(
            "https://google.com"
        )

        return "Opening Google sir."

    # =====================================
    # PLAY YOUTUBE VIDEO
    # =====================================

    elif (
        "play" in prompt
        and "youtube" in prompt
    ):

        search = (
            prompt
            .replace("play", "")
            .replace("on youtube", "")
            .replace("youtube", "")
            .strip()
        )

        youtube_url = (
            "https://www.youtube.com/results?search_query="
            + search.replace(" ", "+")
        )

        webbrowser.open(youtube_url)

        return (
            f"Playing {search} on YouTube sir."
        )

    # =====================================
    # WIKIPEDIA SEARCH
    # =====================================

    elif (
        "tell me about" in prompt
        or "who is" in prompt
        or "what is" in prompt
    ):

        topic = (
            prompt
            .replace("tell me about", "")
            .replace("who is", "")
            .replace("what is", "")
            .strip()
        )

        try:

            info = wikipedia.summary(
                topic,
                sentences=4
            )

            return info

        except Exception:

            return (
                f"Sorry sir, I could not find information about {topic}"
            )

    # =====================================
    # WEATHER
    # =====================================

    elif "weather" in prompt:

        return (
            "Sorry sir, weather API is not connected yet."
        )

    # =====================================
    # THANK YOU
    # =====================================

    elif (
        "thank you" in prompt
        or "thanks" in prompt
    ):

        return (
            "Always welcome sir."
        )

    # =====================================
    # EXIT
    # =====================================

    elif (
        "bye" in prompt
        or "exit" in prompt
    ):

        return (
            "Goodbye sir, have a great day."
        )

    # =====================================
    # DEFAULT RESPONSE
    # =====================================

    else:

        return (
            "Interesting request sir."
        )