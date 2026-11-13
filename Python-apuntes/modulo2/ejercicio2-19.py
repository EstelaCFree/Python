'''
solicitar un num y mostrar su factorial
5
5*4*3*2*1
'''

numero = int(input('introduce un número: '))
resultado = 1

for num in range(numero, 0, -1):
    resultado *= num
print(resultado)

