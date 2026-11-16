
opcion = input('introduzca la opción deseada: \n Consultar saldo, marque 1. \n Ingresar dinero, marque 2. \n Retirar dinero, marque 3. \n Salir, marque 4.')


saldo = 996
while opcion != '4':
    match opcion:
        case '1':
            print(saldo)
            opcion = input('introduzca la opción deseada: \n Consultar saldo, marque 1. \n Ingresar dinero, marque 2. \n Retirar dinero, marque 3. \n Salir, marque 4.')
        case '2':
            ingreso = int(input('indique cantidad a ingresar: '))
            saldo += ingreso
            print(f'su saldo actual es {saldo}')
            opcion = input('introduzca la opción deseada: \n Consultar saldo, marque 1. \n Ingresar dinero, marque 2. \n Retirar dinero, marque 3. \n Salir, marque 4.')
        case '3':
            retiro = int(input('indique cantidad a ingresar: '))
            saldo -= retiro
            print(f'su saldo actual es {saldo}')
            opcion = input('introduzca la opción deseada: \n Consultar saldo, marque 1. \n Ingresar dinero, marque 2. \n Retirar dinero, marque 3. \n Salir, marque 4.')
        case _:
            print('opción incorrecta')
print('Gracias por su visita')

#profe, con ifs:

saldo = 0
opcion = 0
while opcion != 4:
    print('''
    1. Consultar saldo 
    2. Ingresar dinero. 
    3. Retirar dinero. 
    4. Salir.
    ''')
    opcion = input('introduce opción: ')

    if opcion == '1':
        print(f'tu saldo es {saldo}')
    elif opcion == '2':
        ingreso = float(input('indique cantidad a ingresar: '))
        saldo += ingreso
        print(f'su saldo actual es {saldo}')
    elif opcion == '3':
        retiro = int(input('indique cantidad a ingresar: '))
        if saldo >= retiro:
            saldo -= retiro
            print(f'su saldo actual es {saldo}')
        else:
            print('saldo insuficiente.')
    else:
        print('opción incorrecta')
print('Gracias por su visita')
        