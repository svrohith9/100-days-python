import csv
import readMyOrder
# make sure you run writeMyOrder.py alone to generate the bin file first


def newLine(order, item, pos):
    order.insert(pos-1, item)


def calculate(order_data):
    grand_total_item = ["---", "---", "---"]
    total = 0
    for item in order_data:
        total += item[1]*item[2]
        item.append(item[1]*item[2])
    grand_total_item.append(total)
    order_data.append(grand_total_item)


def save_csv(order):
    with open("../mid2data/myOrderWithTotal.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(order)


if __name__ == "__main__":
    order = readMyOrder.retrieve()
    readMyOrder.show(order)
    print()
    item = ['product code of item 5', 0.7, 10]
    newLine(order, item, 3)
    readMyOrder.show(order)
    calculate(order)
    save_csv(order)
