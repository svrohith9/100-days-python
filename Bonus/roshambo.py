import random


class Player:
    def __init__(self, name, value=None, win_count=0, lose_count=0):
        self.name = name
        self.value = value
        self.win_count = win_count
        self.lose_count = lose_count

    def __str__(self):
        print(self.name+" : "+self.value)


class Bart(Player):
    def __init__(self, name="Bart", value=None, win_count=0, lose_count=0):
        super().__init__(name, value, win_count, lose_count)

    def generateRoshambo(self):
        self.value = "rock"


class Lisa(Player):
    def __init__(self, name="Lisa", value=None, win_count=0, lose_count=0):
        super().__init__(name, value, win_count, lose_count)

    def generateRoshambo(self):
        items = ["rock", "paper", "scissors"]
        name = random.choice(items)
        self.value = name


def main():
    print("Roshambo Game")
    print()
    name = input("Enter your name: ")
    print()
    print("Hint 1: Bart's Roshambo is always rock.")
    print("Hint 2: Lisa's Roshambo is selected by random")
    print()
    user_input = input(
        "Would you like to (play against Bart or Lisa? (b/B or l/L): ")
    game_running = True
    if user_input.lower() == "b":
        opponent = Bart()
    elif user_input.lower() == "l":
        opponent = Lisa()
    games_counter = 1
    gamer = Player(name)
    while game_running:
        print()
        rps = input("Rock, paper, or scissors?(r/p/s): ")
        print()
        try:
            if rps.lower() == "r":
                gamer.value = "rock"
                play(opponent, games_counter, gamer)
            elif rps.lower() == "p":
                gamer.value = "paper"
                play(opponent, games_counter, gamer)
            elif rps.lower() == "s":
                gamer.value = "scissors"
                play(opponent, games_counter, gamer)
            else:
                raise Exception("Invalid choice. Try again.")
        except Exception as ex:
            print(ex)
            continue
        again = input("Play again? (y/n): ")
        if again.lower() == "y":
            games_counter += 1
        else:  # any character except 'Y' or 'y' exits the game
            game_running = False
            print()
            print("Thanks for playing!")
            break


def play(opponent, games_counter, gamer):
    opponent.generateRoshambo()
    gamer.__str__()
    opponent.__str__()
    if gamer.value.lower() == opponent.value:
        print("---> Draw!")
    elif (gamer.value.lower() == "rock" and opponent.value.lower() == "paper") or (gamer.value.lower() == "paper" and opponent.value.lower() == "scissors") or (gamer.value.lower() == "scissors" and opponent.value.lower() == "rock"):
        print("---> ", opponent.name, " wins!")
        opponent.win_count += 1
        gamer.lose_count += 1
    else:
        print("---> ", gamer.name, " wins!")
        gamer.win_count += 1
        opponent.lose_count += 1
    print(f"{gamer.name} total wins: {gamer.win_count}/{games_counter}, total lose: {gamer.lose_count}/{games_counter}")
    print(
        f"{opponent.name} total wins: {opponent.win_count}/{games_counter}, total lose: {opponent.lose_count}/{games_counter}")
    print()


if __name__ == "__main__":
    main()
