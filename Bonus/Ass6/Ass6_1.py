def get_cost():
    while True:
        try:
            cost = float(input("Cost of meal: "))
            if cost > 0:
                return cost
            else:
                print("Must be greater than 0. Please try again.")
        except Exception:
            print("Must be a valid decimal number. Please try again.")


def get_tip_percent():
    while True:
        try:
            tip = int(input("Tip Percent: "))
            if tip > 0:
                return tip
            else:
                print("Must be greater than 0. Please try again.")
        except Exception:
            print("Must be a valid integer. Please try again.")


if __name__ == "__main__":
    print("Tip Calculator\n")
    print("INPUT")
    cost = get_cost()
    tip = get_tip_percent()
    tip_amount = (cost*tip)*0.01
    total = round(cost+tip_amount, 2)
    print("\nOUTPUT")
    print("Cost of the meal: ", cost)
    print("Tip percent: ", tip, "%")
    print("Tip amount: ", round(tip_amount, 2))
    print("Total Amount: ", total)
