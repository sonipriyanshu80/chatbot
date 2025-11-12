import random
words = ['apple','mango','kiwi','cherry','banana']
word= random.choice(words)
guessed = []
tries = 6
print("Welcome to Hangman!")
print(" _ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed!")
        continue
    guessed.append(guess)

    if guess not in word:
        tries -=1
        print(f"Wrong! {tries} tries left")
    
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ " 
    print(display)

    if '_' not in display:
        print("You win!")
        break
else:
    print(f"You lose! The word was {word}.")
