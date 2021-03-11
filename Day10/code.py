# combine dic and functions


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enter number a :"))
num2 = float(input("Enter number b :"))

symbol = input("Enter the operation: ")
print(f"{num1} {symbol} {num2} = {operations[symbol](num1,num2)}")
