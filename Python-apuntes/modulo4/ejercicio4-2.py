datos = ['1', 'dos', '3', '4', '5']
suma = 0

for idx in range(len(datos)+1):
#+1 para que dé indexerror al buscar el índice
    try:
        dato = datos[idx]
        numero = int(dato)
    except IndexError as error:
        print('Índice fuera de rango')
    except ValueError as error:
        print('El valor no es numérico')
    except:
        print('Ha ocurrido un error', error)
    else:
        suma += numero

#no siempre hace falta el finally
print('Suma: ', suma)
