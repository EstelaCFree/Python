password = input('introduce una contraseña: ')
longitud = len(password)

match longitud: 
    case num if num < 6:
        print('demasiado corta')
    case num if 6 <= num <=8:
        print('contraseña débil')
    case num if 9 <= num <=12:
        print('aceptable')
    case num if num > 12:
        print('muy buena')

#por qué ese num?

numero = 9
if numero % 3 == 0:
    divisor3 = numero
else:
    divisor3 = 0

#se puede decir todo eso es una sola frase:

divisor3 = numero if numero % 3 == 0 else 0

#Python entiende cosas por inferencia. 
#Si tú estás valorando la variable longitud, al nombrar otra variable en el case entiende que se refiere a esa