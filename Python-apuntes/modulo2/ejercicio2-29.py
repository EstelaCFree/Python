'''
Carrera de 10 km en la que se avanza con el dado
Juan y Miguel van a ir tirando el dado y cada número sube 1 km
Mostras quién gana o s hay empate
'''

Juan = 0
Miguel = 0

import random

while Juan < 10 and Miguel < 10:
    tirada = random.randint(1,6)
    Juan += tirada
    if Juan <= 10 and Miguel <= 10:
        print(f'Juan está en km {Juan}')
        tirada = random.randint(1,6)
        Miguel += tirada
        print(f'Miguel está en km {Miguel}')
        if Miguel >= 10:
            print('Miguel ha ganado')
    elif Juan >= 10 and Miguel < 10:
        print('Juan ha ganado')
    elif Juan == 10 and Miguel == 10:
        print('empate')

#la profe en ejercicio6 ha hecho algo diferente y quizá menos lioso