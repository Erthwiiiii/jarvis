import wikipedia
import pyjokes
from duckduckgo_search import DDGS

# =========================================
# PROCESS COMMAND
# =========================================

def process_command(prompt):

    prompt = prompt.lower().strip()

    # =====================================
    # GREETINGS
    # =====================================

    if (
        "hey jarvis" in prompt
        or "hello" in prompt
        or "hi" in prompt
    ):

        return "Yes sir, I am online and ready to help you."

    # =====================================
    # JOKES
    # =====================================

    elif "joke" in prompt:

        return pyjokes.get_joke()

    # =====================================
    # MATHS
    # =====================================

    elif (
        "(a+b) whole square" in prompt
        or "(a+b)^2" in prompt
    ):

        return "(A + B)² = A² + 2AB + B²"

    elif (
        "(a-b) whole square" in prompt
        or "(a-b)^2" in prompt
    ):

        return "(A - B)² = A² - 2AB + B²"

    # =====================================
    # SEARCH
    # =====================================

    elif (
        "tell me about" in prompt
        or "who is" in prompt
        or "what is" in prompt
    ):

        try:

            query = (
                prompt.replace("tell me about", "")
                .replace("who is", "")
                .replace("what is", "")
                .strip()
            )

            # WIKIPEDIA

            try:

                return wikipedia.summary(
                    query,
                    sentences=5
                )

            except:

                pass

            # DUCKDUCKGO

            with DDGS() as ddgs:

                results = list(
                    ddgs.text(
                        query,
                        max_results=3
                    )
                )

                if results:

                    final = ""

                    for r in results:

                        final += (
                            r["title"]
                            + "\n"
                            + r["body"]
                            + "\n\n"
                        )

                    return final

            return (
                f"Sorry sir, I could not find information about {query}."
            )

        except Exception as e:

            return f"Search Error: {e}"

    # =====================================
    # RETRY
    # =====================================

    elif "retry" in prompt:

        return "Please repeat your request sir."

    # =====================================
    # DEFAULT
    # =====================================

    else:

        return (
            "Sorry sir, I did not understand that command."
        )
