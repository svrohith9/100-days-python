counter_4 = 1
counter_5 = 1
for i in range(31, 150, 3):
    if counter_4 > 7 or counter_5 > 7:
        break
    elif i >= 60 and i <= 70:          # skip 60 to 70 inclusive
        continue
    elif i % 4 == 0 and i % 5 != 0:    # multiples of 4 and not 5
        print('\t', i, '(', counter_4, ')')
        counter_4 += 1
    elif i % 4 != 0 and i % 5 == 0:    # multiples of 5 and not 4
        print('\t\t', i, '(', counter_5, ')')
        counter_5 += 1
    elif i % 4 == 0 and i % 5 == 0:    # multiples of 4 and  5
        print('\t\t\t', i, '(', counter_4, ',', counter_5, ')')
        counter_4 += 1
        counter_5 += 1
    else:
        print(i)
