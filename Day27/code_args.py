# * Arguments
def add(*args):
    return sum([i for i in args])


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))

# ** Kwargs
def func(**kwargs):
    print(kwargs)


func(a=1, b="two", c="3")
