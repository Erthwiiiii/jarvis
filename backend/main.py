# =========================================================
# 🤖 ULTRA JARVIS MAIN AI SYSTEM
# =========================================================

import google.generativeai as genai
import random
import string
from duckduckgo_search import DDGS
import streamlit as st

# =========================================================
# GEMINI API
# =========================================================

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

# =========================================================
# PASSWORD GENERATOR
# =========================================================

def generate_password(length=16):

    chars = string.ascii_letters + string.digits

    return ''.join(
        random.choice(chars)
        for _ in range(length)
    )

# =========================================================
# INTERNET SEARCH
# =========================================================

def web_search(query):

    results = []

    try:

        with DDGS() as ddgs:

            for r in ddgs.text(query, max_results=5):

                results.append(r["body"])

        return "\n".join(results)

    except Exception as e:

        return f"Search Error: {e}"

# =========================================================
# AI CHAT
# =========================================================

def ai_chat(prompt):

    final_prompt = f"""

    You are ULTRA JARVIS AI.

    You are:
    - futuristic
    - intelligent
    - cinematic like Iron Man
    - expert programmer
    - expert AI engineer
    - expert cybersecurity assistant

    User:
    {prompt}

    JARVIS:
    """

    response = model.generate_content(
        final_prompt
    )

    return response.text

# =========================================================
# COMMAND PROCESSOR
# =========================================================

def process_command(prompt):

    # =====================================================
    # PASSWORD
    # =====================================================

    if prompt == "/password":

        return f"""

🔐 SECURE PASSWORD

{generate_password()}
"""

    # =====================================================
    # SEARCH
    # =====================================================

    elif prompt.startswith("/search"):

        query = prompt.replace("/search","")

        return web_search(query)

    # =====================================================
    # NORMAL AI
    # =====================================================

    else:

        return ai_chat(prompt)