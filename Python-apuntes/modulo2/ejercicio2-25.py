'''
Solicitar numeros al usuario hasta que ponga fin
Vamos sumando los numeros y tas el fin que salga el rsultado'''

nums = input('introduzca números a sumar y para poniendo FIN :')

inicio = 0
while nums != 'FIN':
    n = int(nums)
    suma = inicio + n
print(suma)

#esto no funciona, porque se queda pillado porque la variable nums no cambia

nums = input('introduzca números a sumar y para poniendo FIN :')

inicio = 0
while nums != 'FIN':
    n = int(nums)
    inicio += n
    nums = input('introduzca números a sumar y para poniendo FIN :')
print(inicio)

#pero la solución de la profesora en ejercicio2 de ejemplo 5 es más limpia creo
#mete el input al principio del bucle en vez de antes
