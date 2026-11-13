nombre = ['Luis', 'Jorge', 'Maria', 'Laura', 'Pedro']

#Si queremos recorrer la lista por índice
#len(nombres) es la longitud de la lista (nº de elementos)

for index in range(len(nombres)):
    print(nombres[index], end = ' ')
print()

#como nombres es 5 de largo muestra índice del 0 al 5

'''Mostrar sólo los nombres en índice par'''

for index in range(len(nombres)):
    if index % 2 == 0:
        print(nombres[index], end = ' ')
print()