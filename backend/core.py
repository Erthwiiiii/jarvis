import wikipedia
import pyjokes
import datetime
import webbrowser
import random

try:
    from duckduckgo_search import DDGS
except:
    DDGS = None


def web_search(query):

    try:

        if DDGS is None:
            return None

        with DDGS() as ddgs:

            results = list(
                ddgs.text(
                    query,
                    max_results=3
                )
            )

        if results:

            return results[0]["body"]

        return None

    except:

        return None


def process_command(prompt):

    try:

        prompt_original = prompt

        prompt = prompt.lower().strip()

        greetings = [
            "hey jarvis",
            "hello jarvis",
            "hi jarvis",
            "jarvis"
        ]

        if prompt in greetings:

            return random.choice([
                "Yes sir, I am online and ready to help you.",
                "Hello sir, how can I help you today?",
                "JARVIS activated successfully sir.",
                "Always ready sir."
            ])

        elif "time" in prompt:

            return (
                "Current time is "
                + datetime.datetime.now().strftime("%I:%M %p")
            )

        elif "date" in prompt:

            return (
                "Today's date is "
                + datetime.datetime.now().strftime("%d %B %Y")
            )

        elif "joke" in prompt:

            return pyjokes.get_joke()

        elif prompt.startswith("search"):

            search_query = (
                prompt.replace("search", "")
                .strip()
            )

            webbrowser.open(
                "https://www.google.com/search?q="
                + search_query.replace(" ", "+")
            )

            return f"Searching Google for {search_query}"

        elif "play" in prompt or "youtube" in prompt:

            search = (
                prompt
                .replace("play", "")
                .replace("youtube", "")
                .replace("on youtube", "")
                .strip()
            )

            webbrowser.open(
                "https://www.youtube.com/results?search_query="
                + search.replace(" ", "+")
            )

            return f"Opening YouTube results for {search}"

        elif any(op in prompt for op in ["+", "-", "*", "/"]):

            try:

                result = eval(prompt)

                return f"The answer is {result}"

            except:

                pass

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

                wikipedia.set_lang("en")

                search_results = wikipedia.search(topic)

                if search_results:

                      info = wikipedia.summary(
                        search_results[0],
                        sentences=8
                    )

                return info

            except wikipedia.exceptions.DisambiguationError as e:

                return (
                    "Multiple results found sir. "
                    f"Try one of these: {e.options[:5]}"
                )

            except:

                web_info = web_search(topic)

                if web_info:

                    return web_info

                return (
                    f"Sorry sir, I could not find information about {topic}."
                )

        return "Sorry sir, I did not understand that command."

    except Exception as e:

        return f"Error occurred: {e}"
