import myModules.dice as m


def display_title(title):
    print(title)


if __name__ == "__main__":
    display_title("Dice Roller\n")
    flag = False
    x = input("\nRoll the dice? (y/n):")
    if x.lower() == 'y':
        flag = True
    while flag:
        if x.lower() != 'y':
            flag = False
            break
        m.roll_dice()
        x = input("\nRoll again? (y/n):")
