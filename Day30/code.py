# try, except, else, finally, raise


def sample():
    try:
        file = open("xyz.txt")
        sample_dic = {"a": "A"}
        print(sample_dic["b"])

    # If both cases fail first would trigger and next execution second would trigger
    except FileNotFoundError:
        # will create a file due to FileNotFoundError
        file = open("xyz.txt", "w")
    except KeyError as e:
        # Custom exception handling
        print(f"Key {e} not found")


fruits = ["Apple", "banana", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(f"{fruit} pie")
    except IndexError:
        print("fruit pie")


# 1
make_pie(5)


facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]

total_likes = 0

# 2
for post in facebook_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        continue


print(total_likes)
