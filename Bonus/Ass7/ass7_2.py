# 1. define Customer class here
import csv


class Customer:
    def __init__(self, cust_id: str, first_name: str, last_name: str, company_name: str, address: str, city: str, state: str, zip: str):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def getFullName(self):
        return self.first_name+" "+self.last_name

    def getFullAddress(self):
        response = self.getFullName()
        if self.company_name != "":
            response += "\n"+self.company_name
        return response + "\n"+self.address+"\n"+self.city+", "+self.state+" "+self.zip


def get_customers():
    # 2. complete the definition of this function here
    customers = []
    with open("./customers.csv", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            temp = Customer(str(row[0]), str(row[1]), str(row[2]), str(row[3]),
                            str(row[4]), str(row[5]), str(row[6]), str(row[7]))
            customers.append(temp)
    return customers


def find_customer_by_id(customers, cust_id):
    # 3. complete the definition of this function here
    for item in customers:
        if cust_id == item.cust_id:
            return item
    return None


def main():
    # main is fully implemented with no modification expected
    print("Customer Viewer")
    print()

    customers = get_customers()
    while True:
        cust_id = input("Enter customer ID: ").strip()
        print()

        customer = find_customer_by_id(customers, cust_id)
        if customer == None:
            print("No customer with that ID.")
            print()
        else:
            print(customer.getFullAddress())
            print()

        again = input("Continue? (y/n): ").lower()
        print()
        if again != "y":
            break

    print("Bye!")


if __name__ == "__main__":
    main()
