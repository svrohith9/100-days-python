try:
    with open('../MyDataFiles/numbers.txt') as data_file:
        ans = 1
        line = ''
        for num in data_file:
            num = num.replace('\n', '')
            ans *= float(num)               #no more coding error, but ValueError is still possible
            line += '(' + num + ') '
        print('Multiplying', line, 'results', ans)
except FileNotFoundError:         
    print('File Error occurs:', 'numbers.txt cannot be found in MyDataFiles')
except ValueError as ex:
    print('Value Error occurs:', type(ex), ex)
except Exception as ex:
    print('Some Error occurs:', type(ex), ex)

