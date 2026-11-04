'''
    Solicitar al usuario nombre, apellido y edad
    Mostrar un mensaje de bienvenida con esos datos
'''

nombre = input('Pon tu nombre: ')
apellido = input('Escribe tu apellido: ')
edad = input('Dime tu edad: ')
print(str('Bienvenide, ' + nombre + ' ' + apellido + ' con ' + edad + ' años'))
#En realidad no hacía falta convertir a str porque lo que metes en terminal
#lo interpreta como string siempre
#valdría también

print('Bienvenide ', nombre, apellido, 'que tienes', edad, 'años')

#otra forma es con f'literal {variable}'
print(f'Bienvenide {nombre} {apellido} que tienes {edad} años') 
