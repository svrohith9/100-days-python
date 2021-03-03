# Type Error, Type Checking and Type Conversion

a = 6
b = "Rohith"

print("Type of a ", type(a))
print("Type of b ", type(b))

a = str(a)
print("Type of a after conversion", type(a))

print(str(1)+str(2))

print("********************")

print("Enter a three digit number")
num = input()

print(int(num[0])+int(num[1])+int(num[2]))

print("********************")

print("******BMI CALCULATOR**************")


print("Enter your height in meters")
ht = input()
print("Enter your weight in kg")
wt = input()
print("BMI : ", round(float(wt)/(float(ht)**2)))


# f-String
f1 = True
f2 = 10
f3 = "abc"

print(f"Boolean: {f1}, Num : {f2}, Str: {f3}")

print("********************")
print("Enter your age")
age = input()
print(
    f"Age in days : {int(age)*365}\nAge in Months: {int(age)*12}\nAge in weeks: {int(age)*52}")
