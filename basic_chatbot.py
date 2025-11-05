while True:
    user_input = input("You:").lower()
    if user_input in ("hii","hiii","hello","hey"):
        print("Bot: Hello! How can I assist you today?")
    elif user_input == "what is your name":
        print("Bot: I am your friendly assistant bot.")
    elif user_input == "help":
        print("Bot: Sure you can ask me any questions")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: I'm sorry, I didn't understand that. Can you please rephrase?")
