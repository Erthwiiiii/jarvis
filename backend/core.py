def process_command(prompt):

    prompt = prompt.lower()

    # ===================================
    # BASIC COMMANDS
    # ===================================

    if "hello" in prompt:

        return "Hello sir, JARVIS online."

    elif "who are you" in prompt:

        return "I am JARVIS, your advanced AI assistant."

    elif "time" in prompt:

        from datetime import datetime

        return datetime.now().strftime(
            "Current time is %I:%M %p"
        )

    elif "date" in prompt:

        from datetime import datetime

        return datetime.now().strftime(
            "Today's date is %d %B %Y"
        )

    elif "status" in prompt:

        return "All systems are operational."

    # ===================================
    # DEFAULT AI RESPONSE
    # ===================================

    return f"JARVIS received: {prompt}"
