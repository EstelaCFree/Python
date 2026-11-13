'''
Solicitar al usuario un entero
mostrar si es primo o no
un numero es primo si sólo divisible por si mismo y la unidad
'''

numero = int(input('introduce un número y te digo si es primo: '))

for div in range(2, (numero - 1)):
    resultado = numero % div
    if resultado == 0:
        print(f'El numero {numero} es primo')
    else:
        print(f'El numero {numero} no es primo')

'''
está mal por varias cosas:
- no hace falta que ponga -1 porque ya lo hace solo
- si el print está dentro del bucle al primero que prueba ya saca el resultado
'''

#profesora

numero = int(input('introduce un número y te digo si es primo: '))

esPrimo = True

for div in range(2, numero): #no hace falta poner numero -1 porque ya lo es
    if numero % div == 0:
        esPrimo = False

if esPrimo:
    print(f'El numero {numero} es primo')
else:
    print(f'El numero {numero} no es primo')

'''Pero esto es poco eficaz, porque si quiero mirar el 3032, en cuanto lo divide por 2
ya se sabe que no es primo y sin embargo seguiría hasta 3031'''

numero = int(input('introduce un número y te digo si es primo: '))

esPrimo = True

for div in range(2, numero): #no hace falta poner numero -1 porque ya lo es
    if numero % div == 0:
        esPrimo = False
        break #el break rompe el bucle, en cuanto es False ya dice que no es primo

if esPrimo:
    print(f'El numero {numero} es primo')
else:
    print(f'El numero {numero} no es primo')