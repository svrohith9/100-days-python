# Hangman game
import random
print("**************************")
print("Welcome to Hangman Game")
print("**************************")

words = ["rabbit", "pig", "lion", "horse", "tiger", "gorilla"]

# choose random word
word = random.choice(words)
print(f"Its a {len(word)} letter word")

final = list(word)
choice = 0
alive = True
while alive:
    # take user intput
    user_letter = input("Guess a Letter: ").lower()
    choice += 1
    for i in range(0, len(word)):
        if user_letter == word[i]:
            final[i] = word[i]
        elif choice == 1:
            final[i] = "_"
    print(final)
    if(choice > 5):
        alive = False
    elif("".join(final) == word):
        break
if(alive):
    print("You Won!")
else:
    print("You Lost")
    print(f"Correct word {list(word)}")
