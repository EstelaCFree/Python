'''
piscina permite entrada a mayores d 12 y menores de 65 años
'''

edad = int(input('Introduce tu edad: '))
if edad >= 12 and edad <= 65:
    print('acceso permitido')
elif edad < 12:
    print('lo siento, eres menor de 12 años')
else:
    print('lo siento, eres mayor de 65 años')
