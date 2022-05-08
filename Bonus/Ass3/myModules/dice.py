from random import randrange


def roll_dice():
    num1 = roll()
    num2 = roll()
    print(f"\nDie 1: {num1}")
    print(f"Die 2: {num2}")
    print(f"Total: {num1+num2}")
    if num1 == 1 and num1 == num2:
        print("Snake eyes!")
    elif num1 == 6 and num1 == num2:
        print("Boxcars!")


def roll():
    return randrange(1, 7)


if __name__ == "__main__":
    print("Test roll_dice.....")
    roll_dice()
