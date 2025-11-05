
from datetime import datetime
dt=datetime.now().date()
tt=datetime.now().time()
while True:
    user_input = input("You:").lower()
    if user_input in("hii","hiii","hello","kaisa h"):
        print("Bot: How Can I help you")
    elif user_input == "what is your name?":
        print("Bot:I'm Sora, I'm a chatbot to assist you")
    elif user_input == "help":
        print("Bot:what subject do you need help")
    elif user_input == "computer sci":
        print("Bot:for computer sci focus on progm basics and data structures")
    elif "math" in user_input:   
        print("for math understand the concept well and revise regularly")
        
    elif "exam help" in user_input:
        print("start early make study schedule,revise key topics & take breaks")
    elif "motivation" in user_input:
        print("you are doing great, keep pushing further.")
    elif "date" in user_input:
        print("Bot:",dt)
    elif "time" in user_input:
        print("Bot:",tt)   
    elif user_input == "bye":
        print("Bot:see you again")
        break
    else:
        print("I'm not sure try computer sci, math")
