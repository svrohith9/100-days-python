def area(x, y):
    return x*y


def fetch_instructions():
    x = int(input("Enter the length of wall: "))
    y = int(input("Enter the width of wall: "))
    total = area(x, y)
    can = int(input("Enter coverage per can "))
    return total/can


print("Required cans :", round(fetch_instructions()))

print("***********************")


def prime_checker(x):
    counter = 0
    for i in range(1, x):
        if x % i == 0:
            counter += 1
    if counter > 1:
        return False
    else:
        return True


print(prime_checker(11))
