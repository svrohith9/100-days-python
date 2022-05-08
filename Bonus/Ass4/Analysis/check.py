import random


test_data = [-99, 1, 1]
# test_data = [2, 2, -1, -71, 0, 0, 2, 2, 0, 0, 345, 678]


def makeTen(data):
    size = len(data)
    if size < 10:
        for i in range(10-size):
            data.append(random.randint(-5, 5))


def findUnique(data):
    unique_elements = []
    for item in data:
        if data.count(item) < 2:
            unique_elements.append(item)
    return unique_elements


if __name__ == "__main__":
    size = len(test_data)
    print(f"You entered {size} integers: ", test_data)
    if size < 10:
        makeTen(test_data)
        print(f"After {10-size} random integers are appended: ", test_data)
    else:
        print(test_data)
    print(f"These have no duplicates: ", findUnique(test_data))
