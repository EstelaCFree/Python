'''
las 10 tablas de multiplicar
2 bucles: 1 recorre las tablas y otro recorre los números de la tabla
'''

for tabla in range(1, 11):
    print('Tabla del número', {tabla})
    
    for numero in range(1, 11):
        print(f'{tabla} x {numero} = {tabla * numero}')
    print()

#el primer bucle imprime eso, luego inicia el segundo bucle y hasta que no lo acaba no baja al print siguiente
#que pondrá un espacio
