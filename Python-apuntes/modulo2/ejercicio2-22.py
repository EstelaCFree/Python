'''
serie de fibonacci
sumas a un número el anterior de la serie
imprimir los 100 primeros términos de la serie de fibonacci,
no del 0 al 100 sino los 100 primeros números
'''
n1 = 0

n2 = 1

for n in range(1, 101):

    print(f"Término {n}: muestro {n1}")

    suma = n1 + n2

    n1 = n2

    n2 = suma

print()

'''
La versión de la profesora también está mu bien
'''