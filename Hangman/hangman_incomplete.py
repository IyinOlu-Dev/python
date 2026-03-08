import random

words = [
    "apple", "banana", "computer", "python", "cloud", "engineer", "data", "learning", "project", "system",
    "network", "security", "analysis", "design", "development", "student", "teacher", "school", "university", "book",
    "music", "movie", "travel", "journey", "planet", "earth", "moon", "sun", "light", "energy",
    "power", "machine", "robot", "program", "algorithm", "function", "variable", "loop", "condition", "array",
    "list", "dictionary", "tuple", "string", "integer", "float", "boolean", "object", "class", "method"
]

print ("Welcome to guess the word or hangman game")
print("You have 5 lives")

chosen_word = random.choice(words)
lives = 5
tried_letters = ["d"]
display = ['_']*len(chosen_word)

guess = input("Guess a letter ").lower()


game_over = False

while not game_over:
    print(chosen_word)
    

    guess = input("Guess a letter ").lower()
    while True:
        guess = input("Enter a string: ").strip()
        if guess.isalpha():
            break
    print("Invalid input. Please enter letters only.")

    if guess not in chosen_word:
        live -=1
        print("That was a wrong choice\nBetter luck next time")
    elif guess in tried_letters:
        lives -= 1
        print("Sorry you've tried that one")
    else: 
        guess not in tried_letters
        tried_letters.append(guess)

    # if tried_letters == chosen_word


