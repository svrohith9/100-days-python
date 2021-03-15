# class with constructor and default values

class User:
    def __init__(self, name="", user_id=""):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        if self.id != user.id:
            user.followers += 1
            self.following += 1
        else:
            print(f"{user.name}, You cannot follow userself")


user_1 = User()
user_1.id = "1"
user_1.name = "A"

user_2 = User()
user_2.name = "B"
user_2.id = "2"

user_3 = User(name="C", user_id="3")

user_3.follow(user_1)
user_3.follow(user_2)
user_3.follow(user_3)

print("id - name - followers - following")
print(f"{user_1.id} - {user_1.name}-{user_1.followers}- {user_1.following}")
print(f"{user_2.id} - {user_2.name}-{user_2.followers}- {user_2.following}")
print(f"{user_3.id} - {user_3.name}-{user_3.followers}- {user_3.following}")
