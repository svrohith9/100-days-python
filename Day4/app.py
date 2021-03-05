import random
import my_module

print("***************************")
print("Welcome to Rock Paper Scissors")
print("***************************")

user = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors "))
machine = random.randint(0, 2)

if user < 0 or user > 2:
    print("Invalid Data")
else:
    print("You :", my_module.game_data[user])
    print("Machine :", my_module.game_data[machine])

    if user == machine:
        print("Draw")
    elif (user == 0 and machine == 1) or (user == 1 and machine == 2) or (user == 2 and machine == 0):
        print("You Lose")
    else:
        print("You Win")
