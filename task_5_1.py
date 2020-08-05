while True:
    x = int(input('vvedite 1 znachenie:'))
    func = input('vvedite znak: ')
    while func not in ['+', '-', '/', '*']:
        func = input('vvedite verniy znak:')
    y = int(input('vvedite 2 znachenie:'))
    if func == '/' and y == 0:
        while y == 0:
            y = int(input('na 0 ne /,vvedite drugoe znachenie:'))
    if func == '+':
        print(f'{x} {func} {y}=', x + y)
    elif func == '-':
        print(f'{x} {func} {y}=', x - y)
    elif func == '/':
        print(f'{x} {func} {y}=', x / y)
    elif func == '*':
        print(f'{x} {func} {y}=', x * y)
    if func == 0:
        break
