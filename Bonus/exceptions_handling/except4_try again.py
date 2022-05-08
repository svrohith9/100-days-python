while True:
    data = input("Enter three numbers (e.g., 5.9 -10 22.88): ").split()
    try:
        ans = data[0] * data[1] * data[2]                     #Here string must be converted to float
                                                                               #   --> this is coding error
                                                                               #but what if '$234.99' or '(76.1)' is entered?
                                                                               #   --> run-time ValueError
        print(f'{data[0]} * {data[1]} * {data[2]} = {ans}')
        break
    except Exception as ex:
        print('Type of input data:', type(data[0]), type(data[1]), type(data[2]))
        print('Error occurs:', type(ex), 'cannot multiply..... try again!')
   

