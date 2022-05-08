# connect to the database and set the row factory
import sqlite3
from contextlib import closing


def connect_db(path):
    DB_FILE = "Sales.db"
    return sqlite3.connect(DB_FILE)


def view_orders_summary_by_country(connection):
    with closing(connection.cursor()) as c:
        query = '''SELECT Country, count(OrderID) as TotalNumberOfOrders, sum(Amount) as TotalOfOrderAmount, avg(Amount) as OrderAverage FROM Orders GROUP BY Country'''
        c.execute(query)
        summary = c.fetchall()

    return summary


def view_orders_by_date(connection):
    order_date = input("Date of orders: ")
    with closing(connection.cursor()) as c:
        query = '''SELECT * FROM Orders WHERE OrderDate = ?'''
        c.execute(query, (order_date,))
        summary = c.fetchall()
    return summary


def view_orders_by_salesperson(connection):
    salesperson = input("Name of sales person: ")
    with closing(connection.cursor()) as c:
        query = '''SELECT * FROM Orders WHERE Salesperson = ?'''
        c.execute(query, (salesperson,))
        summary = c.fetchall()
    return summary


def view_orders_by_salesperson_date(connection):
    salesperson = input("Name of sales person: ")
    order_date = input("Date of orders: ")
    with closing(connection.cursor()) as c:
        query = '''SELECT * FROM Orders WHERE Salesperson = ? and OrderDate = ?'''
        c.execute(query, (salesperson, order_date,))
        summary = c.fetchall()
    return summary


def view_orders_by_amount(connection):
    min_order = input("Minimum of order amount: ")
    max_order = input("Maximum of order amount: ")
    with closing(connection.cursor()) as c:
        query = '''SELECT * FROM Orders WHERE Amount between ? and ?'''
        c.execute(query, (min_order, max_order,))
        summary = c.fetchall()
    return summary


def update_orders(connection):
    print("Update order amount by entering sales person's name AND range of order amount: ")
    salesperson = input("--> Enter sales person's name: ")
    min_order = int(input("--> Enter minimum of order amount: "))
    max_order = int(input("--> Enter maximum of order amount: "))
    with closing(connection.cursor()) as c:
        query = '''SELECT * FROM Orders WHERE Salesperson = ? AND Amount between ? and ?'''
        c.execute(query, (salesperson, min_order, max_order,))
        summary = c.fetchall()

        display_orders(summary)
        print()
        amount = int(input("How much to update (e.g., +25, -100, etc.)? "))

        query = '''UPDATE Orders SET Amount = Amount + ? WHERE Salesperson = ? AND Amount between ? and ?'''
        c.execute(query, (amount, salesperson, min_order, max_order,))
        connection.commit()

        print("Updated.....")

        query = '''SELECT * FROM Orders WHERE Salesperson = ? AND Amount between ? and ?'''
        c.execute(query, (salesperson, min_order+amount, max_order+amount,))
        summary = c.fetchall()
    print()
    display_orders(summary)


def display_menu():
    print("COMMAND MENU")
    print("c - View order summary of a given country")
    print("d - View order details of a given date")
    print("s - View order details of a given sales person")
    print("sd - View order details of a given sales person and date")
    print("a - View order details of a given range of amounts")
    print("u - Update order amount of a sales person's orders")
    print("m - Display command menu")
    print("e - Exit program")
    print()


def display_summary(summary):
    for line in summary:
        print(line["Country"], "|", line["TotalNumberOfOrders"], "orders |",
              "${:,.2f}".format(line["TotalOfOrderAmount"]), "in total |", "average is ${:,.2f} per order".format(line["OrderAverage"]))
    print()


def display_orders(orders):
    if len(orders) > 0:
        count = 1
        for order in orders:
            print(str(count) + " -", order["Country"], "|", order["Salesperson"], "|",
                  order["OrderID"], "|", order["OrderDate"], "|", "${:,.2f}".format(order["Amount"]))
            count += 1
    else:
        print("No orders....")
    print()


def main():
    print("Sales Orders Program")
    print()

    conn = connect_db("Sales.db")
    conn.row_factory = sqlite3.Row

    display_menu()
    while True:
        command = input("Command: ")
        if command == "c":
            result = view_orders_summary_by_country(conn)
            display_summary(result)
        elif command == "d":
            result = view_orders_by_date(conn)
            display_orders(result)
        elif command == "s":
            result = view_orders_by_salesperson(conn)
            display_orders(result)
        elif command == "sd":
            result = view_orders_by_salesperson_date(conn)
            display_orders(result)
        elif command == "a":
            result = view_orders_by_amount(conn)
            display_orders(result)
        elif command == "u":
            update_orders(conn)
        elif command == "m":
            display_menu()
        elif command == "e":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()
