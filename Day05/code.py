# loops
fruits = ["apple", "mango", "orange"]
for fruit in fruits:
    print(fruit)

print("******************")

print("Enter number of students: ")
size = int(input())
print(f"Enter height of {size} students")
heights_list = input().split(" ")
avg_height = 0
for i in heights_list:
    avg_height = avg_height+int(i)
print("Avg height of each Student", round(avg_height/size))

print("******************")

print("Height Score in the Class")
print("Enter scores separating with comma(,)")
scores = input().split(",")
#print("Max score", max(scores))
maximum = int(scores[0])
for i in scores:
    if(maximum < int(i)):
        maximum = int(i)
print("Maximum Score: ", maximum)

print("******************")
print("Sum of all Even numbers from a to b")
a = int(input("Enter Value of a: "))
b = int(input("Enter value of b: "))
# check if starts with even or odd
if a % 2 != 0:
    a = a+1
sum = 0
for i in range(a, b+1, 2):
    sum = sum+i
print(f"Sum of all even from {a} to {b} is {sum}")
