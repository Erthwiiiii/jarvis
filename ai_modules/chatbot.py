from google import genai

# =======================================

def setup_ai(api_key):

    try:

        client = genai.Client(
            api_key=api_key
        )

        print("AI CONNECTED")

        return client

    except Exception as e:

        print("AI Setup Error:", e)

        return None

# =======================================

def ask_ai(model, prompt):

    try:

        response = model.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("AI Error:", e)
        return f"AI ERROR: {e}"