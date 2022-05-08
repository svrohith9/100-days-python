import pickle


def save_bin(order_data):
    with open('../mid2data/myOrder.bin', 'wb') as file:
        pickle.dump(order_data, file)


if __name__ == "__main__":
    order = [["product code of item 1", 2.25, 4],
             ["product code of item 2", 9, 30],
             ["product code of item 3", 1.5, 6],
             ["product code of item 4", 50, 1]]
    save_bin(order)
    print("Write to myOrder.bin successfully!")
