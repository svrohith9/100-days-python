while True:
    data = input("Enter three numbers (e.g., 5.9 -10 22.88): ").split()
    try:
        ans = float(data[0]) * float(data[1]) * float(data[2])  #bug fixed: strings are converted to float
        print(f'{data[0]} * {data[1]} * {data[2]} = {ans}')
        break
    except Exception as ex:  #Even the above bug is fixed, this except must stay for ValueError
                                          #that validates and ensure input data is convertable
        print('Type of input data:', type(data[0]), type(data[1]), type(data[2]))
        print('Error occurs:', type(ex), 'cannot multiply..... try again!')
   

