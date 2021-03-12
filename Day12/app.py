# Guess the Number Game

import random

print("*********************************")
print("     Guess the Number(1 to 100)    ")
print("*********************************")

number = random.randint(1, 100)


def game(limit):
    guess = int(input("Guess the number: "))
    limit = limit-1
    if limit == 0:
        print(f"You Lost, Number: {number}")
        return
    if guess == number:
        print("You Win")
        return
    elif guess > number:
        print("Please guess something lower")
        print(f"You have only {limit} attempts left")
        return game(limit)
    else:
        print("Please guess something higher")
        print(f"You have only {limit} attempts left")
        return game(limit)


def start():
    limit = 0
    user_input = input(
        "Choose easy(10 attempts), medium(7 attempts), hard(5 attempts): ").lower()
    if user_input == "easy":
        limit = 10
    elif user_input == "medium":
        limit = 7
    elif user_input == "hard":
        limit = 5
    else:
        print("Bad Input")
        return
    return game(limit)


start()
