#partimos de la base de no calcular si es bisiesto

mes = int(input('introduce un número de mes: '))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f'ese mes tiene {31*24} horas')
    case 2:
        print(f'ese mes tiene {28*24} si el año no es bisiesto, {29*24} si lo es.')
    case 4 | 6 | 9 | 11:
        print(f'ese mes tiene {30*24} horas.')
    case _:
        print('sólo hay 12 meses, tolai')

#con el cálculo de bisiesto:

mes = int(input('introduce un número de mes: '))

match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f'ese mes tiene {31*24} horas')
    case 2:
        anyo = int(input('de qué año?: '))
        if anyo % 400 == 0:
            print(f'ese mes tiene {29*24} porque es bisiesto')
        elif anyo % 4 == 0 and anyo % 100 != 0:
            print(f'ese mes tiene {29*24} porque es bisiesto')
        else:
            print(f'ese mes tiene {28*24} porque no es bisiesto')         
    case 4 | 6 | 9 | 11:
        print(f'ese mes tiene {30*24} horas.')
    case _:
        print('sólo hay 12 meses, tolai')