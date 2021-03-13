print("****************************")
print("Welcome to Auction Program")
print("****************************")

bids = []


def get_quote():
    name = input("What is your name? ")
    quote = int(input("Enter your quote price :"))
    temp = {}
    temp["name"] = name
    temp["quote"] = quote
    bids.append(temp)
    print("Any other Bidders? Y or N")
    option = input().lower()
    add_another(option)


def add_another(option):
    if option == "y":
        get_quote()
        # print(bids)
    else:
        high_bid = 0
        name = ""
        for key in bids:
            if key["quote"] > high_bid:
                high_bid = key["quote"]
                name = key["name"]
        print(f"{name} got the bid with value ${high_bid}")


get_quote()
