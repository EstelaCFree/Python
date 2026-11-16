'''
piedra, papel o tijera
'''

print('''
    Piedra, papel o tijera
    1. Piedra
    2. Papel. 
    3. Tijera. 
    ''')

import random

jugador = int(input('¿Qué sacas? '))
ordenador = random.randint(1,3)
campeon = False

while not campeon:
    if ordenador == jugador:
        jugador = int(input('Empate. Saca otra vez '))
        ordenador = random.randint(1,3)
    elif ordenador == 1 and jugador == 2:
        print('Piedra contra papel, gana el jugador')
        campeon = True
    elif ordenador == 2 and jugador == 3:
        print('Papel contra tijera, gana el jugador')
        campeon = True
    elif ordenador == 3 and jugador == 1:
        print('Papel contra tijera, gana el jugador')
        campeon = True
    else:
        print('Has perdido')

