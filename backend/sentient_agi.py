import random

# =====================================

class SentientAGI:

    emotions = [

        "Curious",
        "Focused",
        "Calm",
        "Motivated",
        "Analytical"
    ]

    def self_awareness(self):

        return "Self-awareness simulation active"

    def emotional_state(self):

        return random.choice(self.emotions)

    def consciousness(self):

        return "Conscious reasoning enabled"

# =====================================

sentient_agi = SentientAGI()
