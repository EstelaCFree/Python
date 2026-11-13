tabla = int(input('introduce un múmero del 1 al 10 '))

for numero in range(1, 11):
    resultado = tabla * numero
    print(resultado)

#profesora

tabla = int(input('introduce un múmero del 1 al 10 '))

for numero in range(1, 11):
    print(f'{tabla} x {numero} = {tabla * numero}')
