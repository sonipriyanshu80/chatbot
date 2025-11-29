print("Welcome to Advanced Quiz Chatbot!")
name = input("Enter your name: ")
print(f"Hello {name}! Let's start the quiz.\n")

score = 0

# List of questions
questions = [
    {
        "q": "1 Which language is used to create Android Apps?",
        "options": ["A. Java", "B. HTML", "C. CSS"],
        "answer": "a"
    },
    {
        "q": "2 What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Jaipur"],
        "answer": "b"
    },
    {
        "q": "3 Who is known as the Father of Computer?",
        "options": ["A. Elon Musk", "B. Bill Gates", "C. Charles Babbage"],
        "answer": "c"
    },
    {
        "q": "4 2 + 4 * 2 = ?",
        "options": ["A. 10", "B. 12", "C. 6"],
        "answer": "a"
    },
    {
        "q": "5 Which company created Python?",
        "options": ["A. Microsoft", "B. Google", "C. Guido van Rossum"],
        "answer": "c"
    }
]

# Asking Questions
for item in questions:
    print(item["q"])
    for opt in item["options"]:
        print(opt)

    user_ans = input("Your answer (A/B/C): ").lower()

    if user_ans == item["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")

# Final Score
print("Quiz Completed!")
print(f"{name}, Your Score: {score} / {len(questions)}")

if score == len(questions):
    print("Excellent! You got full marks!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep practicing!")

print("\nThanks for playing!")
