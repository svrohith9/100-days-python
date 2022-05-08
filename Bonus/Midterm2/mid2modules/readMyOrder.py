import pickle
# make sure you run writeMyOrder.py alone to generate the bin file first


def show(order_data):
    for item in order_data:
        print(item[0], " ", item[1], " ", item[2])


def retrieve():
    with open("../mid2data/myOrder.bin", "rb") as file:
        order = pickle.load(file)
    return order


if __name__ == "__main__":
    order = retrieve()
    print("Retrieve myOrder.bin successfully as below:")
    show(order)
