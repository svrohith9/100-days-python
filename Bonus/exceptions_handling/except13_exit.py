import sys

try:
    with open('../MyDataFiles/number.txt') as data_file:
        ans = 1
        line = ''
        for num in data_file:
            num = num.replace('\n', '')
            ans *= float(num)               #no more coding error, but ValueError is still possible
            line += '(' + num + ') '

        if line == '':
            raise Warning('WARNING: file is empty!')  #Force an exception here,
                                                                             #but, who is going to handle it?
        elif ans < 0:
            raise Warning('WARNING: negative result!')  #Force an exception here,
                                                                                 #but, who is going to handle it?
        else:
            print('Multiplying', line, 'results', ans)
except FileNotFoundError:         
    print('File Error occurs:', 'numbers.txt cannot be found in MyDataFiles')
    sys.exit()
except ValueError as ex:
    print('Value Error occurs:', type(ex), ex)
    sys.exit()
except Exception as ex:
    print('Some Error occurs:', type(ex), ex)
    sys.exit()
finally:
    print('Multiplication is done!')

# When any of the above exceptions occurs, sys.exit() guarantees the code below
# won't be executed.
ans *= 2
print('double the result = ', ans)
