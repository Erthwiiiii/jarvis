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
        # HELLO
        # =====================================

        if (
            "hey jarvis" in prompt
            or "hello jarvis" in prompt
            or "hi jarvis" in prompt
        ):

            return (
                "Yes sir, I am online and ready."
            )

        # =====================================
        # HOW ARE YOU
        # =====================================

        elif "how are you" in prompt:

            return (
                "I am functioning perfectly sir."
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
        # PLAY ON YOUTUBE
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
                f"Playing {search} on YouTube sir."
            )

        # =====================================
        # TIME
        # =====================================

        elif "time" in prompt:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            return (
                f"The time is {current_time}"
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
        # WHO IS / TELL ME ABOUT
        # =====================================

        elif (
            "who is" in prompt
            or "tell me about" in prompt
        ):

            topic = (
                prompt
                .replace("who is", "")
                .replace("tell me about", "")
                .strip()
            )

            try:

                result = wikipedia.summary(
                    topic,
                    sentences=2
                )

                return result

            except:

                return (
                    "Sorry sir, no information found."
                )

        # =====================================
        # DEFAULT AI RESPONSE
        # =====================================

        else:

            try:

                result = wikipedia.summary(
                    prompt,
                    sentences=2
                )

                return result

            except:

                return (
                    "Interesting request sir."
                )

    except Exception as e:

        return f"Error: {e}"