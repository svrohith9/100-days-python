import mid2Lib

if __name__ == "__main__":
    data = [[-3, 0, 8, 1, 70, -12],
            [-9.2, 11, "504", 0.88, 0],
            [100, "#66", 2]]
    for item in data:
        try:
            print(item)
            print("total of even numbers =", mid2Lib.countEvenNum(item))
        except Exception as ex:
            print("Execution fails due to an error below: ", type(ex), "", ex)
