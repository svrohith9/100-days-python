try:
    with open('../MyDataFiles/numbers.txt') as data_file:
        ans = 1
        line = ''
        try:
            for num in data_file:
                num = num.replace('\n', '')
                ans *= float(num)               #no more coding error, but ValueError is still possible
                line += '(' + num + ') '
            print('Multiplying', line, 'results', ans)
        except ValueError as ex:
            print('Error occurs:', type(ex), ex)
except FileNotFoundError:         #Can this handle file exception?
    print('Error occurs:', 'numbers.txt cannot be found in MyDataFiles')    


