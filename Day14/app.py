from data import users_data
import random

print("********************************")
print(" Welcome to Higher Lower Game")
print("*******************************")

option_a = random.choice(users_data)
option_b = random.choice(users_data)
# print(option_a)


def start(option_a, option_b, score):
    print(
        f" {option_a['name']} Vs {option_b['name']}, Who has more Instagram Followers")
    user_input = input("Choose A or B who has more followers: ").lower()

    if option_a == option_b:
        option_b = random.choice(users_data)
    if user_input == "a":
        if option_a["follower_count"] >= option_b["follower_count"]:
            print(f"You're Right, Score: {score}")
            option_b = random.choice(users_data)
            start(option_a, option_b, score+1)
        else:
            print(f"You're Wrong, Score: {score-1}")
    else:
        if option_a["follower_count"] <= option_b["follower_count"]:
            print(f"You're Right, Score: {score}")
            option_a = random.choice(users_data)
            start(option_a, option_b, score+1)
        else:
            print(f"You're Wrong, Score: {score-1}")


start(option_a, option_b, score=1)
