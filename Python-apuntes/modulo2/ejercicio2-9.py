
dia = input('pon la inicial del día de la semana: ')
match dia:
    case 'l' | 'L' :
        print('Lunes')
    case 'm' | 'M' :
        print('Martes')
    case 'x' | 'X' :
        print('Miércoles')
    case 'j' | 'J' :
        print('Jueves')
    case 'v' | 'V' :
        print('Viernes')
    case 's' | 'S' :
        print('Sábado')
    case 'd' | 'D' :
        print('Domingo')
    case _:
        print('No es un día válido')