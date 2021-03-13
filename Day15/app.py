from data import MENU
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def set_profit(x):
    global profit
    profit = profit + x


def final_choice():
    user_input = input(
        "Would you like to choose again? y or n : ").lower()
    if user_input == 'y':
        return start()
    else:
        print("Thank you ")


def check_availability(user_choice):
    items = {i: MENU[user_choice]["ingredients"][i]
             for i in MENU[user_choice]["ingredients"] if i in resources and (MENU[user_choice]["ingredients"][i] >= resources[i])}
    # print(items)
    if len(items) == 0:
        quarters = int(input("Please insert quarters: "))*0.25
        dime = int(input("Please insert dimes: "))*0.1
        nickle = int(input("Please insert nickles: "))*0.05
        penny = int(input("Please insert nickles: "))*0.01
        total = (quarters+dime+nickle+penny)
        if total >= MENU[user_choice]["cost"]:
            charge = total-MENU[user_choice]['cost']
            print("**************")
            print(f"Enjoy your {user_choice}")
            print(
                f"Here is your change ${round(charge,2)}")
            set_profit(MENU[user_choice]['cost'])
            for i in MENU[user_choice]["ingredients"]:
                if i in resources:
                    resources[i] = (
                        resources[i]-MENU[user_choice]["ingredients"][i])
            final_choice()
        else:
            print(f"Please provide ${MENU[user_choice]['cost']}")
            proceed = input("Y to continue, N to decline : ").lower()
            if proceed == "y":
                return check_availability(user_choice)
    else:
        print(f"Out of Resources")
        final_choice()


def proceed_making(user_choice):
    if user_choice in MENU:
        check_availability(user_choice)
    else:
        print("Invalid Input")
        start()


def proceed_report():
    print("Current Resourses")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${round(profit,2)}")
    start()


def start():
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino) : ").lower()
    if user_choice == "report":
        proceed_report()
    else:
        proceed_making(user_choice)


start()

# print(check_availability("cappuccino"))
