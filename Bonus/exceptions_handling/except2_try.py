data = input("Enter three numbers (e.g., 5.9 -10 22.88): ").split()
try:
    ans = data[0] * data[1] * data[2]
    print(f'{data[0]} * {data[1]} * {data[2]} = {ans}')
except:
    print('TypeError: cannot multiply non-numeric data')    
    print('Goodbye1!!')
print('Goodbye2!!')
