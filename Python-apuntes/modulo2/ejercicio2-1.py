'''mostrar si un numero es par'''

numero = input('Introduce un número: ')

if int(numero) % 2 == 0:
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')

'''
si es par y múltiplo de 3
'''

if numero % 2 == 0:
    if numero % 3 == 0:
        print(f'El número {numero} es par y múltiplo de 3')
    else:
        print(f'El número {numero} es par pero no es múltiplo de 3')    
elif numero % 3 == 0:
    print(f'El número {numero} es impar pero es múltiplo de 3')
else:
    print(f'El número {numero} es impar y no es múltiplo de 3')

#la profesora lo ha hecho diferente:
#if numero % 2 == 0 and numero % 3 == 0:
#    print(f'El número {numero} es par y múltiplo de 3')
#elif numero % 2 == 0 and numero % 3 != 0:
#    print(f'El número {numero} es par pero no es múltiplo de 3')    
#elif numero % 2 != 0 and numero % 3 == 0:
#    print(f'El número {numero} es impar pero es múltiplo de 3')
#else:
#    print(f'El número {numero} es impar y no es múltiplo de 3')
