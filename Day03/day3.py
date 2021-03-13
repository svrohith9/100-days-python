# Conditional Statements

height = int(input("What is your height?"))

if height >= 120:
    print("You can ride in rollercoster")
    age = int(input("Enter your age?"))
    if(age > 18):
        print("$10 per person")
        bill = 10
    elif age > 12 and age <= 18:
        print("$8 per person")
        bill = 8
    else:
        print("$5 per person")
        bill = 5
    photo = input("Do you need photo?")
    if photo == "Yes":
        bill = bill+3
        print("Total bill $", bill)
else:
    print("Grow")
