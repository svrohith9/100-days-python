file = open(".\\100-days-python\\Day24\\data.txt")
print(file.read())

with open(".\\100-days-python\\Day24\\data.txt", mode='a') as file:
    file.write("\nHello world")
