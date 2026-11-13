#Si queremos mostrar los números del 0 al 9:

for numero in range(10):
    print(numero)

#esto va a poner un número dbajo del otro, con saltos de líneas.
#por qué? porque el valor por defecto en el print de una separación,
#es un espacio. Y el final de caa print es un salto de línea.
#Si quiero que los ponga en una línea cambio ese final por el espacio:

for numero in range(10):
    print(numero, end=' ')
print()

#del 1 al 10

for numero in range(1, 11):
    print(numero, end=' ')
print()

#del 0 al 10 de 2 en 2

for numero in range(0, 11, 2):
    print(numero, end=' ')
print()

#del 10 al 1 en modo decreciente

for numero in range(10, 0, -1):
    print(numero, end=' ')
print()

#del 10 al 0 en modo decreciente de 2 en 2

for numero in range(10, -1, -2):
    print(numero, end=' ')
print()

