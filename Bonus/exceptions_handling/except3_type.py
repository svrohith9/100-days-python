data = input("Enter three numbers (e.g., 5.9 -10 22.88): ").split()
try:
    ans = data[0] * data[1] * data[2]
    print(f'{data[0]} * {data[1]} * {data[2]} = {ans}')
except Exception as ex:
    print('Type of input data:', type(data[0]), type(data[1]), type(data[2]))
    print('Error:', type(ex), 'cannot multiply')
  

