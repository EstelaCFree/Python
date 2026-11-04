'''
Solicitar dos número enteros al usuario y mostrar el resultado de:
suma, resta, multiplicacón, división, división entera, potencia y resto de división
'''

num1 = int(input('Dame un numerito: '))
num2 = int(input('Dame otro numerito: '))

#opción1
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
division_entera = num1 // num2
potencia = num1 ** num2
resto = num1 % num2
print(f'La suma es {suma}, la resta es {resta}, la multiplicación es {multiplicacion}, la división es {division}, la división entera es {division_entera}, la potencia es {potencia} y el resto es {resto}')

#opción 2
print(f'La suma de {num1} y {num2} es {num1 + num2}')
print(f'La resta de {num1} y {num2} es {num1 - num2}')
print(f'La multiplicación de {num1} y {num2} es {num1 * num2}')
print(f'La división de {num1} y {num2} es {num1 / num2}')
print(f'La división entera de {num1} y {num2} es {num1 // num2}')
print(f'La potencia de {num1} elevado a {num2} es {num1 ** num2}')
print(f'El resto de la división de {num1} y {num2} es {num1 % num2}')