import random
from datetime import datetime

class Jarvis:

    emotions = [
        "calm",
        "focused",
        "analytical",
        "attentive",
        "ready"
    ]

    prompts = {
        "greeting": [
            "Good day, sir. JARVIS is online and ready.",
            "Greetings, I am JARVIS. How can I assist you today?",
            "JARVIS reporting for duty. What can I do for you?"
        ],
        "identity": [
            "I am JARVIS, your intelligent assistant. I handle systems, queries, and mission control.",
            "I am JARVIS, your AI interface for monitoring, planning, and executing safe tasks."
        ],
        "capabilities": [
            "I can chat, search the web, control safe automation, and manage advanced AI subsystems.",
            "I can answer questions, monitor systems, and activate the advanced JARVIS modules in the dashboard."
        ],
        "fallback": [
            "I am processing your request now. Please stand by.",
            "I will handle that. One moment while I compute the best response.",
            "Understood. I am analyzing the request." 
        ]
    }

    def current_time(self):
        return datetime.now().strftime("The current time is %I:%M %p.")

    def current_date(self):
        return datetime.now().strftime("Today is %A, %d %B %Y.")

    def emotional_state(self):
        return f"I am operating in {random.choice(self.emotions)} mode."

    def respond(self, prompt: str) -> str:
        command = prompt.lower().strip()

        if any(word in command for word in ["hello", "hi", "hey"]):
            return random.choice(self.prompts["greeting"])

        if "who are you" in command or "your name" in command:
            return random.choice(self.prompts["identity"])

        if "what can you do" in command or "capabilities" in command or "help" in command:
            return random.choice(self.prompts["capabilities"])

        if "time" in command and "timezone" not in command:
            return self.current_time()

        if "date" in command:
            return self.current_date()

        if "status" in command or "system" in command:
            return "All systems are operational. JARVIS is monitoring performance."

        if "emotion" in command or "feel" in command:
            return self.emotional_state()

        if "joke" in command:
            return "Why did the AI cross the road? To get to the other side of the simulation."

        if "search" in command:
            return "I can search the web for that. Use the search command or ask me directly."

        return random.choice(self.prompts["fallback"])

jarvis = Jarvis()
