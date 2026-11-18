# crear una lista llamada colores con los valores rojo, verde y azul

colores = ['rojo', 'verde', 'azul']

# mostrar el tipo de dato de la coleccion

print(type(colores))

# mostrar el contenido de la lista

print(colores) 

# recorrer la lista con for in

for color in colores:
    print(color, sep=' - ') 

# recorrer la lista con for range

for color in range(len(colores)):
    print(color, sep=' - ') 

# recorrer la lista con while

idx = 0
while idx < len(colores):
    print(colores[idx], end=" ")
    idx += 1
print()

# mostrar el color verde (acceder por el indice)

print(colores[1]) 

# borrar el color azul

del colores[2] 

# crear una lista vacia mas_colores

mas_colores = [] 

# en la lista nueva unir el contenido de la lista colores con: blanco, negro, rosa, azul

mas_colores = colores + ['blanco', 'negro', 'rosa', 'azul']
print(mas_colores) 

# agregar el color naranja al final

mas_colores.append('maranja') 

# agregar el color marron al principio

mas_colores.insert(0, 'marron') 

# mostrar la longitud de la lista

print(len(mas_colores)) 

#ordenar la lista en orden ascendente

mas_colores.sort()

# mostrar el antepenultimo elemento

print(mas_colores[-3])

#Mostrar los dos últimos elementos

print(mas_colores)
print(len(mas_colores))
print(mas_colores[-2:])

#Desde el último al antepenúltimo

print(mas_colores[:-4:-1])

#Mostrar del segundo al cuarto elemento

print(mas_colores[1:4])

#mostrar del primero al penúltimo de 2 en 2

print(mas_colores[:-1:2])


