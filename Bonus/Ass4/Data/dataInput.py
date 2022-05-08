import sys


def getData(data):
    data.clear()
    for item in sys.argv[1:]:
        data.append(item)
    return data


if __name__ == "__main__":
    data = getData([])
    print(f"You entered {len(data)} integers: ", data)
