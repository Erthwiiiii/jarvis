import random
import urllib.parse

# ==========================================
# JARVIS GREETINGS
# ==========================================

greetings = [

    "Yes sir?",
    "How can I help you sir?",
    "Ready for your command sir.",
    "I'm listening sir.",
    "At your service sir."
]

# ==========================================
# MAIN AI ENGINE
# ==========================================

def process_command(prompt):

    prompt = prompt.lower().strip()

    # ======================================
    # GREETING
    # ======================================

    if "hey jarvis" in prompt or "hello jarvis" in prompt:

        return random.choice(greetings)

    # ======================================
    # YOUTUBE SEARCH
    # ======================================

    elif "youtube" in prompt:

        query = prompt

        query = query.replace("open youtube", "")
        query = query.replace("play", "")
        query = query.replace("on youtube", "")
        query = query.strip()

        # ----------------------------------

        if query:

            encoded = urllib.parse.quote(query)

            url = f"https://www.youtube.com/results?search_query={encoded}"

            return f"""
✅ Opening YouTube Search

🎬 Searching for:
{query}

🔗 Link:
{url}
"""

        # ----------------------------------

        else:

            return """
✅ Opening YouTube

🔗 Link:
https://youtube.com
"""

    # ======================================
    # GOOGLE SEARCH
    # ======================================

    elif "google" in prompt:

        query = prompt.replace("open google", "")
        query = query.strip()

        # ----------------------------------

        if query:

            encoded = urllib.parse.quote(query)

            url = f"https://www.google.com/search?q={encoded}"

            return f"""
✅ Google Search

🔍 Searching:
{query}

🔗 Link:
{url}
"""

        # ----------------------------------

        else:

            return """
✅ Opening Google

🔗 Link:
https://google.com
"""

    # ======================================
    # CHATGPT
    # ======================================

    elif "chatgpt" in prompt:

        return """
✅ Opening ChatGPT

🔗 Link:
https://chat.openai.com
"""

    # ======================================
    # INSTAGRAM
    # ======================================

    elif "instagram" in prompt:

        return """
✅ Opening Instagram

🔗 Link:
https://instagram.com
"""

    # ======================================
    # FACEBOOK
    # ======================================

    elif "facebook" in prompt:

        return """
✅ Opening Facebook

🔗 Link:
https://facebook.com
"""

    # ======================================
    # WHATSAPP
    # ======================================

    elif "whatsapp" in prompt:

        return """
✅ Opening WhatsApp

🔗 Link:
https://web.whatsapp.com
"""

    # ======================================
    # SPOTIFY
    # ======================================

    elif "spotify" in prompt:

        return """
✅ Opening Spotify

🔗 Link:
https://spotify.com
"""

    # ======================================
    # NETFLIX
    # ======================================

    elif "netflix" in prompt:

        return """
✅ Opening Netflix

🔗 Link:
https://netflix.com
"""

    # ======================================
    # WHO ARE YOU
    # ======================================

    elif "who are you" in prompt:

        return """
I am JARVIS,
your advanced AI assistant sir.
"""

    # ======================================
    # TIME
    # ======================================

    elif "time" in prompt:

        from datetime import datetime

        current = datetime.now().strftime("%I:%M %p")

        return f"""
🕒 Current Time

{current}
"""

    # ======================================
    # DATE
    # ======================================

    elif "date" in prompt:

        from datetime import datetime

        today = datetime.now().strftime("%d %B %Y")

        return f"""
📅 Today's Date

{today}
"""

    # ======================================
    # EXIT
    # ======================================

    elif "shutdown" in prompt or "exit" in prompt:

        return """
⚠️ Shutting down systems sir.
"""

    # ======================================
    # DEFAULT RESPONSE
    # ======================================

    else:

        return f"""
⚡ JARVIS RESPONSE ⚡

I heard:

'{prompt}'

But I do not fully understand that command yet sir.
"""
