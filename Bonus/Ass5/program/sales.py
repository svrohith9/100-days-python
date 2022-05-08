import csv
file_path = '../data/monthly_sales.csv'

print("Monthly Sales Program\n")
print("COMMAND MENU")
print("monthly - View monthly sales")
print("yearly  - View yearly sumary")
print("edit    - Edit sales for a month")
print("exit    - Exit program\n")

command = input("Command :")
command = command.lower()

while True:
    if command == "monthly":
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], " - ", row[1])
    elif command == "yearly":
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            total = 0
            for row in reader:
                total += int(row[1])
            print("Yearly total: ", total)
            print("Monthly average: ", round((total/12), 2))
    elif command == "edit":
        month = input("Three-letter Month: ")
        amount = input("Sales Amount: ")
        months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                  "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
        if month not in months:
            print("Invalid three-letter month.")
        else:
            data = []
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
            for item in data:
                if item[0] == month:
                    item[1] = amount
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print("Sales amount for ", month, " was modified.")
    elif command == "exit":
        print("Bye!")
        exit()
    command = input("\nCommand :")
