import datetime
import webbrowser
import wikipedia
import pyjokes
import requests

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # GREETINGS
    # =====================================

    if "hello" in prompt or "hey jarvis" in prompt:

        return "Hello sir, how can I help you?"

    # =====================================
    # TIME
    # =====================================

    elif "time" in prompt:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        return f"Sir, current time is {current_time}"

    # =====================================
    # DATE
    # =====================================

    elif "date" in prompt:

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}"

    # =====================================
    # JOKES
    # =====================================

    elif "joke" in prompt:

        return pyjokes.get_joke()

    # =====================================
    # OPEN YOUTUBE
    # =====================================

    elif "open youtube" in prompt:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube sir."

    # =====================================
    # OPEN GOOGLE
    # =====================================

    elif "open google" in prompt:

        webbrowser.open("https://google.com")

        return "Opening Google sir."

    # =====================================
    # SEARCH YOUTUBE
    # =====================================

    elif "play" in prompt and "youtube" in prompt:

        search = (
            prompt
            .replace("play", "")
            .replace("on youtube", "")
            .strip()
        )

        youtube_url = (
            "https://www.youtube.com/results?search_query="
            + search.replace(" ", "+")
        )

        webbrowser.open(youtube_url)

        return f"Playing {search} on YouTube sir."

    # =====================================
    # WIKIPEDIA SEARCH
    # =====================================

    elif (
        "tell me about" in prompt
        or "who is" in prompt
        or "what is" in prompt
    ):

        try:

            topic = (
                prompt
                .replace("tell me about", "")
                .replace("who is", "")
                .replace("what is", "")
                .strip()
            )

            info = wikipedia.summary(
                topic,
                sentences=3
            )

            return info

        except Exception as e:

            return "Sorry sir, I could not find information."

    # =====================================
    # WEATHER
    # =====================================

    elif "weather" in prompt:

        return "Sir, weather functionality is coming soon."

    # =====================================
    # THANK YOU
    # =====================================

    elif "thank you" in prompt:

        return "You're welcome sir."

    # =====================================
    # DEFAULT RESPONSE
    # =====================================

    else:

        return (
            "Sir, I understood your request but "
            "I do not have answer for that yet."
        )