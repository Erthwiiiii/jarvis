def process_command(prompt):

    prompt = prompt.lower().strip()

    # ===================================
    # BASIC COMMANDS
    # ===================================

    if "hello" in prompt or "hi" in prompt:

        return "Good day, sir. JARVIS is online and ready."

    elif "who are you" in prompt or "your name" in prompt:

        return "I am JARVIS, your advanced AI assistant."

    elif "time" in prompt:

        from datetime import datetime

        return datetime.now().strftime(
            "The current time is %I:%M %p"
        )

    elif "date" in prompt:

        from datetime import datetime

        return datetime.now().strftime(
            "Today is %A, %d %B %Y"
        )

    elif "status" in prompt or "system" in prompt:

        return "All systems are online and operating normally."

    elif "joke" in prompt:

        return "Why did the robot go on vacation? Because it needed to recharge its batteries."

    elif "weather" in prompt:

        return "Weather module active. Please provide a city name for a forecast."

    elif "what can you do" in prompt or "capabilities" in prompt:

        return (
            "I can chat, search the web, execute safe commands, "
            "monitor system health, and activate advanced AI modules."
        )

    elif "remember" in prompt or "memory" in prompt:

        return "Memory module online. I can save notes and recall your preferences."

    # ===================================
    # DEFAULT AI RESPONSE
    # ===================================

    return f"JARVIS received your request: '{prompt}'. I am processing it now."
