import webbrowser
import datetime
import wikipedia

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    try:

        prompt = prompt.lower().strip()

        # =====================================
        # GREETING
        # =====================================

        if (
            "hey jarvis" in prompt
            or "hello jarvis" in prompt
        ):

            return (
                "Yes sir, I am online and ready to help you."
            )

        # =====================================
        # TIME
        # =====================================

        elif "time" in prompt:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return (
                f"The current time is {current_time}"
            )

        # =====================================
        # DATE
        # =====================================

        elif "date" in prompt:

            current_date = datetime.datetime.now().strftime(
                "%d %B %Y"
            )

            return (
                f"Today's date is {current_date}"
            )

        # =====================================
        # OPEN YOUTUBE
        # =====================================

        elif "open youtube" in prompt:

            webbrowser.open(
                "https://youtube.com"
            )

            return (
                "Opening YouTube sir."
            )

        # =====================================
        # OPEN GOOGLE
        # =====================================

        elif "open google" in prompt:

            webbrowser.open(
                "https://google.com"
            )

            return (
                "Opening Google sir."
            )

        # =====================================
        # PLAY VIDEO
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

            return (
                f"Playing {search} on YouTube."
            )

        # =====================================
        # KNOWLEDGE AI
        # =====================================

        else:

            try:

                result = wikipedia.summary(
                    prompt,
                    sentences=5
                )

                return result

            except:

                return (
                    "Sorry sir, I could not find information about that."
                )

    except Exception as e:

        return f"Error: {e}"