import webbrowser
import datetime
import wikipedia
from duckduckgo_search import DDGS

# =========================================
# MAIN AI FUNCTION
# =========================================

def process_command(prompt):

    prompt = prompt.lower()

    # =====================================
    # GREETINGS
    # =====================================

    if "hello" in prompt or "hi" in prompt:

        return "Hello sir, how can I help you?"

    # =====================================
    # YOUTUBE
    # =====================================

    elif "open youtube" in prompt:

        webbrowser.open(
            "https://youtube.com"
        )

        return "Opening YouTube sir."

    # =====================================
    # GOOGLE
    # =====================================

    elif "open google" in prompt:

        webbrowser.open(
            "https://google.com"
        )

        return "Opening Google sir."

    # =====================================
    # CHATGPT
    # =====================================

    elif "open chatgpt" in prompt:

        webbrowser.open(
            "https://chat.openai.com"
        )

        return "Opening ChatGPT sir."

    # =====================================
    # TIME
    # =====================================

    elif "time" in prompt:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        return f"The time is {current_time}"

    # =====================================
    # DATE
    # =====================================

    elif "date" in prompt:

        today = datetime.datetime.now().strftime("%d %B %Y")

        return f"Today's date is {today}"

    # =====================================
    # WIKIPEDIA
    # =====================================

    elif "who is" in prompt or "what is" in prompt:

        try:

            result = wikipedia.summary(
                prompt,
                sentences=2
            )

            return result

        except:

            return "Sorry sir, I could not find information."

    # =====================================
    # SEARCH
    # =====================================

    elif "search" in prompt:

        try:

            query = prompt.replace(
                "search",
                ""
            )

            results = DDGS().text(
                query,
                max_results=1
            )

            for r in results:

                return f"{r['title']} : {r['href']}"

        except:

            return "Search failed sir."

    # =====================================
    # PLAY YOUTUBE VIDEO
    # =====================================

    elif "play" in prompt:

        song = prompt.replace(
            "play",
            ""
        )

        search_url = f"https://www.youtube.com/results?search_query={song}"

        webbrowser.open(search_url)

        return f"Playing {song} on YouTube."

    # =====================================
    # DEFAULT RESPONSE
    # =====================================

    else:

        return f"I understood your command: {prompt}"
