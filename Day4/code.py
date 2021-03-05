import random
# custom module
import my_module
print(my_module.data)

# prints some random number
print(random.randint(1, 100))
print(random.random())

print("***************************")

print("Enter the names")
data = input().split(", ")

print("Random Name : "+data[random.randint(0, len(data)-1)])
