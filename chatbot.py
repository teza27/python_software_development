import random
responses = ["Hello", "Good morning", "Good afternoon", "Good evening", "Hi dear", "Happy weekend"]
greeting = input("Say your greetings to the chatbot\n")
greetings = random.choice(responses)
if greetings == greeting:
    responses_regen = random.choice(responses)
    print(f"{responses_regen}")
else:
    print(f"{greetings}")
your_name = input("What is your name?\n")
if " " not in your_name:
    print(f"{greetings} {your_name}")
else:
    print("Invalid entry, input just your name!")