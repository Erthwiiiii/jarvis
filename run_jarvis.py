from frontend.voice_engine import speak
from backend.automation import execute_command

print("JARVIS online sir.")

while True:

    command = input("You: ")

    if command.lower() == "exit":
        speak("Goodbye sir.")
        break

    execute_command(command)