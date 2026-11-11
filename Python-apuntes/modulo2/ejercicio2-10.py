mes = input('dime un número de mes.')

match int(mes):
    case 12 | 1 | 2:
        print(f'Winter is coming')
    case 3 | 4 | 5:
        print(f'qué bonita es la primavera')
    case 6 | 7 | 8:
        print(f'veranito, qué calor')
    case 9 | 10 | 11:
        print(f'la nostalgia del otoño')
    case _:
        print(f'tiene que ser un número del 1 al 12, duh')

#podría haber no usado el int y ponerlos todos como letras