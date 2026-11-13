'''
Mostrar los numeros primos del 1 al 100
'''

for numero in range (1, 101):
    for div in range(2, numero): #no hace falta poner numero -1 porque ya lo es
        if numero % div == 0:
            break
        else:
            print(numero)

'''
está mal porque salen repetidos los números y no ha salido el dos'''


for numero in range (1, 101):
    esPrimo = True

    for div in range(2, numero): #no hace falta poner numero -1 porque ya lo es
        if numero % div == 0:
            esPrimo = False
            break
    if esPrimo:
            print(numero)