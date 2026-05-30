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

        prompt_original = prompt

        prompt = prompt.lower().strip()

        # =====================================
        # GREETINGS
        # =====================================

        greetings = [
            "hey jarvis",
            "hello jarvis",
            "hi jarvis",
            "jarvis"
        ]

        if any(word in prompt for word in greetings):

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
        # JOKE
        # =====================================

        elif "joke" in prompt:

            return pyjokes.get_joke()

        # =====================================
        # GOOGLE SEARCH
        # =====================================

        elif prompt.startswith("search"):

            search_query = (
                prompt.replace("search", "")
                .strip()
            )

            url = (
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            webbrowser.open(url)

            return f"Searching Google for {search_query}"

        # =====================================
        # YOUTUBE
        # =====================================

        elif (
            "play" in prompt
            or "youtube" in prompt
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

            return f"Opening YouTube results for {search}"

        # =====================================
        # MATH
        # =====================================

        elif any(op in prompt for op in ["+", "-", "*", "/"]):

            try:

                result = eval(prompt)

                return f"The answer is {result}"

            except:

                pass

        # =====================================
        # INFORMATION
        # =====================================

        topic = (
            prompt_original
            .replace("Tell me about", "")
            .replace("tell me about", "")
            .replace("Who is", "")
            .replace("who is", "")
            .replace("What is", "")
            .replace("what is", "")
            .strip()
        )

        if len(topic) > 0:

            try:

                info = wikipedia.summary(
                    topic,
                    sentences=8,
                    auto_suggest=True
                )

                return info

            except wikipedia.exceptions.DisambiguationError as e:

                return (
                    "Multiple results found sir. "
                    f"Try one of these: {e.options[:5]}"
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
        # DEFAULT
        # =====================================

        return (
            "Sorry sir, I did not understand that command."
        )

    except Exception as e:

        return f"Error occurred: {e}"
