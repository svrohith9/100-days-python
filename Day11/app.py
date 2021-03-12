# Building BlackJack
import random

print("*****************************")
print("     Welcome to BlackJack    ")
print("*****************************")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def default():
    player_cards.append(cards[random.randint(0, len(cards)-1)])
    computer_cards.append(cards[random.randint(0, len(cards)-1)])


def start():
    default()
    # print(f"computer_cards: {computer_cards}")
    is_player_safe = True
    is_computer_safe = True
    game_running = True
    while game_running:
        print(f"Your cards: {player_cards}")
        user_choice = input(
            "Do you want to pick another card? Y or N ").lower()
        if user_choice == "n":
            game_running = False
        else:
            is_player_safe = pick_Card_check(player_cards)
            if not is_player_safe:
                game_running = False
            is_computer_safe = pick_Card_check(computer_cards)
            if not is_computer_safe:
                game_running = False

    if not game_running:
        if (check_card_count(player_cards) < check_card_count(computer_cards) and check_card_count(computer_cards) <= 21) or (not is_player_safe):
            print("Computer Won !")
        elif (check_card_count(player_cards) > check_card_count(computer_cards) and check_card_count(player_cards) <= 21) or (not is_computer_safe):
            print("Player Won !")
        else:
            print("Drawn")
    print(f"Your cards: {player_cards}")
    print(f"Computer cards: {computer_cards}")


def pick_Card_check(card_list):
    card_list.append(cards[random.randint(0, len(cards)-1)])
    if check_card_count(card_list) <= 21:
        return True
    else:
        return False


def check_card_count(card_list):
    s = 0
    for i in card_list:
        if not (s + i <= 21) and i == 11:
            s += 1
        else:
            s += i
    # print(s)
    return s

#     Your cards: [2, 7, 2, 3, 10]
# Computer cards: [3, 11, 11, 6, 11]


start()
