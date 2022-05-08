def countEvenNum(data):
    count = 0
    try:
        for item in data:
            num = int(item)
            if num % 2 == 0:
                count += 1
        return count
    except Exception as ex:
        raise ex
