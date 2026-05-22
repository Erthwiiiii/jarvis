from ai_modules.chatbot import ask_ai

# =======================================

def process_command(model, prompt):

    response = ask_ai(
        model,
        prompt
    )

    return response