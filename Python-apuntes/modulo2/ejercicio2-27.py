variable = 7

num = int(input('A ver si adivinas el número del 1 al 10 que estoy pensando. Di un número: '))

while num != variable:
    if num < variable:
        print('Nooooo, sube, sube')
        num = int(input('Vuelve a intentarlo: '))
    elif num > variable:
        print('Alaaaa, te has pasado')
        num = int(input('Vuelve a intentarlo: '))
    elif num < 0 or num > 10:
        num = int(input('Te he dicho del 1 a 10. Di otro: '))
print(f'Siiiii, era el {variable}')

#profesora, incorporando el random:

import random
numero = random.randint(1,10)

adivinar = 0
while adivinar != numero:
    adivinar = int(input('adivina el numero: '))
    if adivinar < numero:
        print('Nooooo, sube, sube')
    elif adivinar > numero:
        print('Alaaaa, te has pasado')

print(f'Siiiii, era el {variable}')