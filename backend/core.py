import wikipedia
import pyjokes
import datetime
import webbrowser
import random

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    try:

        prompt = prompt.lower()

        # =====================================
        # GREETINGS
        # =====================================

        if (
            "hey jarvis" in prompt
            or "hello" in prompt
            or "hi" in prompt
        ):

            replies = [

                "Yes sir, I am online and ready to help you.",

                "Hello sir, how can I help you today?",

                "JARVIS activated successfully sir.",

                "Always ready sir."

            ]

            return random.choice(replies)

        # =====================================
        # TIME
        # =====================================

        elif "time" in prompt:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return f"Current time is {current_time}"

        # =====================================
        # DATE
        # =====================================

        elif "date" in prompt:

            current_date = datetime.datetime.now().strftime(
                "%d %B %Y"
            )

            return f"Today's date is {current_date}"

        # =====================================
        # JOKES
        # =====================================

        elif "joke" in prompt:

            return pyjokes.get_joke()

        # =====================================
        # GOOGLE SEARCH
        # =====================================

        elif "search" in prompt:

            search = (
                prompt.replace("search", "")
                .strip()
            )

            url = (
                "https://www.google.com/search?q="
                + search.replace(" ", "+")
            )

            webbrowser.open(url)

            return f"Searching Google for {search}"

        # =====================================
        # YOUTUBE
        # =====================================

        elif (
            "youtube" in prompt
            or "play" in prompt
        ):

            search = (
                prompt.replace("play", "")
                .replace("youtube", "")
                .strip()
            )

            youtube_url = (
                "https://www.youtube.com/results?search_query="
                + search.replace(" ", "+")
            )

            webbrowser.open(youtube_url)

            return f"Opening YouTube results for {search}"

        # =====================================
        # WIKIPEDIA INFORMATION
        # =====================================

        elif (
            "tell me about" in prompt
            or "who is" in prompt
            or "what is" in prompt
        ):

            topic = (
                prompt.replace("tell me about", "")
                .replace("who is", "")
                .replace("what is", "")
                .strip()
            )

            try:

                info = wikipedia.summary(
                    topic,
                    sentences=5
                )

                return info

            except wikipedia.exceptions.DisambiguationError as e:

                return (
                    f"Multiple results found sir. "
                    f"Try being more specific."
                )

            except wikipedia.exceptions.PageError:

                return (
                    f"Sorry sir, I could not find information about {topic}."
                )

            except Exception as e:

                return (
                    f"Wikipedia Error: {e}"
                )

        # =====================================
        # MATH
        # =====================================

        elif (
            "+" in prompt
            or "-" in prompt
            or "*" in prompt
            or "/" in prompt
        ):

            try:

                result = eval(prompt)

                return f"The answer is {result}"

            except:

                pass

        # =====================================
        # DEFAULT
        # =====================================

        return (
            "Sorry sir, I did not understand that command."
        )

    except Exception as e:

        return f"Error occurred: {e}"