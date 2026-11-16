'''
Tirar el dado hasta que salga el numero 6
generar un numero aleatorio entre 1 y 6
mostrar numero generado
'''



import random

print('Tiramos el dado')

dado = random.randint(1,6)
contador = 0
while dado != 6:
    print(f'Ha salido {dado}')
    contador += 1
    dado = random.randint(1,6)
print(f'6! Tardamos {contador} veces')


