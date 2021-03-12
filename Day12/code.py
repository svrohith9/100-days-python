# scope
value = 10


def func():
    value = 20
    print(f"value : {value}")

    def func1():
        value = 30
        print(f"value: {value}")
    func1()


# All the values are in different due to different level of scope
func()
print(f"value : {value}")
