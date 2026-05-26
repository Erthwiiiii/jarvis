def detect_wake_word(text):

    wake_words = [

        "jarvis",
        "hey jarvis",
        "ok jarvis"
    ]

    for word in wake_words:

        if word in text.lower():

            return True

    return False