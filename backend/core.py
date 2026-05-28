import random
import datetime
import webbrowser

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # GREETINGS
    # =====================================

    if (
        "hey jarvis" in prompt
        or "hello jarvis" in prompt
        or "hi jarvis" in prompt
    ):

        replies = [

            "Yes sir, I am online and ready.",

            "Always ready sir.",

            "JARVIS activated successfully sir.",

            "Hello sir, how can I help you today?"
        ]

        return random.choice(replies)

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
    # YOUTUBE
    # =====================================

    elif (
        "play" in prompt
        and "youtube" in prompt
    ):

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

        return f"Opening {search} on YouTube sir."

    # =====================================
    # GOOGLE SEARCH
    # =====================================

    elif "search" in prompt:

        search_query = (
            prompt
            .replace("search", "")
            .strip()
        )

        google_url = (
            "https://www.google.com/search?q="
            + search_query.replace(" ", "+")
        )

        webbrowser.open(google_url)

        return f"Searching Google for {search_query}"

    # =====================================
    # WEATHER
    # =====================================

    elif "weather" in prompt:

        return (
            "Weather service is currently unavailable sir."
        )

    # =====================================
    # DEFAULT AI RESPONSE
    # =====================================

    else:

        smart_replies = [

            "I understand sir.",

            "Interesting request sir.",

            "Working on it sir.",

            "Can you please explain more sir?",

            "I am ready to help sir.",

            "Command received successfully sir."
        ]

        return random.choice(smart_replies)