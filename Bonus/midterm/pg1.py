import random
data = ['apple', 'mango', 'grape', 'strawberry', 'lemon']
for i in range(0, 3):
    print(f"{random.choice(data)} {random.choice(data)}")
    print(f"{random.choice(data)} {random.choice(data)}\n")
