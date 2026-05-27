import webbrowser
import datetime
import random
import wikipedia
from duckduckgo_search import DDGS


# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # GREETINGS
    # =====================================

    if any(word in prompt for word in [

        "hey jarvis",
        "hello",
        "hi",
        "jarvis"

    ]):

        replies = [

            "Hello sir, how can I help you?",

            "Yes sir, I am online and ready.",

            "Greetings sir. What can I do for you?",

            "JARVIS activated successfully sir.",

            "Always ready sir."

        ]

        return random.choice(replies)

    # =====================================
    # OPEN YOUTUBE
    # =====================================

    elif "open youtube" in prompt:

        webbrowser.open(
            "https://www.youtube.com"
        )

        return "Opening YouTube sir."

    # =====================================
    # PLAY VIDEO
    # =====================================

   elif "play" in prompt and "youtube" in prompt:

    search = prompt.replace(
        "play",
        ""
    ).replace(
        "on youtube",
        ""
    )

    youtube_url = (
        "https://www.youtube.com/results?search_query="
        + search.replace(" ", "+")
    )

    webbrowser.open(youtube_url)

    return f"Opening YouTube results for {search} sir."

    # =====================================
    # OPEN GOOGLE
    # =====================================

    elif "open google" in prompt:

        webbrowser.open(
            "https://www.google.com"
        )

        return "Opening Google sir."

    # =====================================
    # OPEN CHATGPT
    # =====================================

    elif "open chatgpt" in prompt:

        webbrowser.open(
            "https://chat.openai.com"
        )

        return "Opening ChatGPT sir."

    # =====================================
    # OPEN INSTAGRAM
    # =====================================

    elif "open instagram" in prompt:

        webbrowser.open(
            "https://instagram.com"
        )

        return "Opening Instagram sir."

    # =====================================
    # OPEN FACEBOOK
    # =====================================

    elif "open facebook" in prompt:

        webbrowser.open(
            "https://facebook.com"
        )

        return "Opening Facebook sir."

    # =====================================
    # TIME
    # =====================================

    elif "time" in prompt:

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        return f"The current time is {current_time}"

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

        jokes = [

            "Why did the AI cross the road? To optimize the chicken.",

            "Artificial intelligence is no match for natural stupidity.",

            "I would tell you a robot joke, but you may not process it.",

            "My intelligence is artificial, but my humor is real."

        ]

        return random.choice(jokes)

    # =====================================
    # WEATHER
    # =====================================

    elif "weather" in prompt:

        return "Weather system is currently under development sir."

    # =====================================
    # WIKIPEDIA SEARCH
    # =====================================

    elif "who is" in prompt or "what is" in prompt:

        try:

            result = wikipedia.summary(
                prompt,
                sentences=2
            )

            return result

        except:

            return "I could not find information sir."

    # =====================================
    # WEB SEARCH
    # =====================================

    elif "search" in prompt:

        try:

            query = prompt.replace(
                "search",
                ""
            )

            results = DDGS().text(
                query,
                max_results=3
            )

            final = []

            for r in results:

                final.append(
                    r["title"]
                )

            return "\n".join(final)

        except:

            return "Search failed sir."

    # =====================================
    # CALCULATOR
    # =====================================

    elif "calculate" in prompt:

        try:

            expression = prompt.replace(
                "calculate",
                ""
            )

            result = eval(expression)

            return f"The answer is {result}"

        except:

            return "Calculation failed sir."

    # =====================================
    # SYSTEM STATUS
    # =====================================

    elif "status" in prompt:

        return "All systems are operational sir."

    # =====================================
    # EXIT
    # =====================================

    elif "shutdown" in prompt:

        return "Shutdown command blocked for security reasons sir."

    # =====================================
    # DEFAULT RESPONSE
    # =====================================

    else:

        replies = [

            f"Sir, I received your command: {prompt}",

            "Can you explain more sir?",

            "I am processing your request sir.",

            "Interesting request sir.",

            "Working on it sir."

        ]

        return random.choice(replies)
