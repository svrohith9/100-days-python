start = 31
end = 150
counter_4 = 1
counter_5 = 1
for i in range(start-1, 150, 3):
    # skip 60 to 70 inclusive
    if i >= 60 and i <= 70:
        continue
    # multiples of 4 and not 5
    elif i % 4 == 0 and i % 5 != 0:
        print('\t', i, '(', counter_4, ')')
        counter_4 += 1
    # multiples of 5 and not 4
    elif i % 4 != 0 and i % 5 == 0:
        print('\t\t', i, '(', counter_5, ')')
        counter_5 += 1
    # multiples of 4 and  5
    elif i % 4 == 0 and i % 5 == 0:
        print('\t\t\t', i, '(', counter_4, ',', counter_5, ')')
        counter_4 += 1
        counter_5 += 1
    elif counter_4 == 7 or counter_5 == 7:
        break
