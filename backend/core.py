import datetime
import webbrowser
import wikipedia
import pyjokes
import random

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower().strip()

    # =====================================
    # GREETING
    # =====================================

    greetings = [
        "hello",
        "hi",
        "hey",
        "hey jarvis"
    ]

    if prompt in greetings:

        return random.choice([
            "Yes sir, I am online and ready to help you.",
            "Hello sir, how can I help you today?",
            "Jarvis online sir.",
            "Ready for your command sir."
        ])

    # =====================================
    # TIME
    # =====================================

    elif "time" in prompt:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        return f"Sir, the current time is {current_time}"

    # =====================================
    # DATE
    # =====================================

    elif "date" in prompt:

        today = datetime.datetime.now().strftime("%d %B %Y")

        return f"Sir, today's date is {today}"

    # =====================================
    # JOKE
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
    # PLAY VIDEO / SONG
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
    # MATHS
    # =====================================

    elif "whole square" in prompt:

        if "a+b" in prompt:

            return (
                "(A + B)² = A² + 2AB + B²"
            )

        elif "a-b" in prompt:

            return (
                "(A - B)² = A² - 2AB + B²"
            )

        else:

            return (
                "Sir, please specify the expression."
            )

    # =====================================
    # WIKIPEDIA SEARCH
    # =====================================

    else:

        try:

            result = wikipedia.summary(
                prompt,
                sentences=5
            )

            return result

        except wikipedia.exceptions.DisambiguationError as e:

            return (
                f"Sir, your query is too broad. Try something specific like: {e.options[0]}"
            )

        except wikipedia.exceptions.PageError:

            return (
                f"Sorry sir, I could not find information about {prompt}."
            )

        except Exception as e:

            return (
                f"Error occurred: {e}"
            )