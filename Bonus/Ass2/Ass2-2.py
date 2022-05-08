print("Table of Powers\n")
while True:
    start = int(input('Start number: '))
    stop = int(input('Stop number: '))
    if start > stop:
        print('Start number must be less than stop number. Please try again.')
    else:
        break
print("\nNumber\tSquared\tCubed")
print("======\t=======\t=====")
for i in range(start, stop+1, 1):
    print(i, "\t", i**2, "\t", i**3)
