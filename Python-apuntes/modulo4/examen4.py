'''
Se requiere un programa que divida dos números introducidos por el usuario, evitando que el programa se detenga si se introduce texto o un cero.
Requerimientos de Ejecución:
1. Solicitar dos números al usuario.
2. Implementar un bloque try-except.
3. Capturar la excepción ValueError (por si introducen caracteres no numéricos).
4. Capturar la excepción ZeroDivisionError (por si dividen entre cero).
5. Mostrar el resultado o un mensaje de error amigable y descriptivo.
Evidencias Obligatorias a Entregar: Archivo .py y captura de pantalla provocando un error de división por cero manejado.
'''


try:
    numero1 = int(input('Dame un número: '))
    numero2 = int(input('Ahora dame otro para dividir por él: '))
    division = numero1/numero2
    print(f'El resultado es {division}')
except ValueError as error:
    print('Sólo se admiten números', error)
except ZeroDivisionError as error:
    print('No se puede dividir por cero')
finally:
    print('Gracias')