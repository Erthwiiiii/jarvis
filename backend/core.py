import wikipedia
import datetime
import webbrowser

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # TIME
    # =====================================

    if "time" in prompt:

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
    # YOUTUBE
    # =====================================

    elif "youtube" in prompt:

        search = (
            prompt.replace("play", "")
            .replace("on youtube", "")
            .strip()
        )

        youtube_url = (
            "https://www.youtube.com/results?search_query="
            + search.replace(" ", "+")
        )

        webbrowser.open(youtube_url)

        return f"Opening YouTube for {search}"

    # =====================================
    # GOOGLE
    # =====================================

    elif "google" in prompt:

        search = (
            prompt.replace("search", "")
            .replace("on google", "")
            .strip()
        )

        google_url = (
            "https://www.google.com/search?q="
            + search.replace(" ", "+")
        )

        webbrowser.open(google_url)

        return f"Searching Google for {search}"

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

        except Exception:

            return (
                "Sorry sir, I could not find information about that."
            )
