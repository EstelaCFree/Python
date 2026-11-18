##FUNCIONES
No estuve, crear apuntes con pdf y ejercicios, y la explicación que puedas añadir

##COLECCIONES

#LISTAS
funciones != métodos.
por ejemplo, len() es una función, el argumento es una lista, una colección, un string. Se declara de forma independiente.
lista.append('x') es un método. Poniendo lista. nos va a dar opciones de métodos, que serían como funciones propias de esa lista o de una función. Se dclara dentro de la clase list.
No sé si esto está correcto, estuve en una llamada mientras lo explicaba.

Hay que tener en cuenta que los textos son listas, casi todo lo que se hace con listas se puede hacer con cadenas de texto

en ejemplo07_listas -> listas.py vienen ejemplos

- Métodos:
.append() agrega un elemento al final de la lista
.insert() agrega un elemento en una posición determinada. El primer argumento es la posición y el segundo lo que se inserta.
.extend() agrega varios elementos a la vez al final. irían entre corchetes: lista.extend([1, 2, 3])

- Borrar un elemento:
si es el último: del lista[-1]
si no se pone su posición como argumento
Cuando indicas un índice siempre va entre corchetes sea una lista o sea otra colección

- Modificar un elemento:
lista[-4] = 'x'
Cuenta 4 desde el último y cambia ese elemento por x

- Mostrar el índice donde está un elemento
lista.index('x')
Si no está nos devuelve un error de valor
puedes poner a partir de qué índice buscar, lo metes como segundo parámetro
lista.index('x', 3)

- Contar elementos repetidos
lista.count('x')

- Ordenar los elementos
lista.sort() 
Si no indico nada los ordena por orden ascendente
Si hay de distintos tipos de datos me va a dar TypeError
Si quiero ordenarla en orden descendente:
lista.sort(reverse:True)

- Eliminar todos los elementos de la lista
lista.clear()

- Quitar un valor pero el primero que encuentra
lista.remove()
Le pueds poner el parámetro que quieres quitar y quitará el primero
lista.remove('nombre')

- Recorrer la lista con bucle for in
for elemento in lista:
    print(elemento, end='-')
Ese ejemplo va a poner un guión entre cada elemento (y uno al final)

for elemento in lista:
    print(elemento, sep='-')
else:
    print('\n----)

¿Por qué lo del else si eso es de if?
Porque Python permite usarlo en un bucle for para indicar qué se hace cuando ya no hay más elementos sobre los que iterar. En este caso imprime un salto de línea y rayas.

- Recorrer la lista for range
for indice in range((len(lista))) #el rango incluye un número menos del que salga pero incluye el cero
    print(lista[indice], end='-')
else:
    print('\n----)

- Recorrer la lista while
idx = 0
while(idx < len(lista)):
    print(lista[idx], end='-')
    idx += 1
else:
    print('\n----)

Lo del else no es obligatorio ni nada, es para que veamos que se puede usar en cualquier bucle, pero quizá lo suyo es que ese tema del else como cierre opcional del bucle debería ir en el módulo 2 donde los bucles.

- Slices
Como filetear. 
slice(inicio:stop:step)
Pero incluye el 0 así que si vas por índice siempre es contando el 0 y cmo range, el último que pongas no sale

print('Todos', lista[:])
Porque el step es opcional, y al no dar argumentos es del principio al final: imprime todos.

print('últimos cuatro', lista[-4:])
Del -4 al final porque no has puesto ese argumento

print('5 primeros', lista[0:5]) #o lista[:5] que es lo mismo

print('del índice 3 al 6', lista[3:7])

print('del índice 6 al 3', lista[6:2:-1])

print('del índice 6 al 3 desde la derecha', lista[-6:-10:-1])
#este último sería también equivalente a lista[-6:2:-1], es decir se pueden combinar contando desde el final con desde el principio

print('todos al revés', lista[::-1])

print('todos al revés de 2 en 2', lista[::-2])

-Operadores de pertenencia
in y not in
print('medicina' in lista) -> True/False
Es decir, devuelve un booleano

#LISTAS MULTIDIMENSIONALES
Una lista de una sola dimensión es como un array. Se recorre con el índice y si quieres un bucle
Listas de dos dimensiones es como una matriz. Un ejemplo sería el hundir la flota o un excel.
matriz = [[2,7,4], [8,1,6], [3,9,5]]
Sería igual que
2 7 4 
8 1 6
3 9 5
Entonces para recorrerlo necesitas 2 índices y 2 bucles
Y si tuviera 3 dimensiones como un cubo de tubik, pues 3 índices y 3 bucles

en el ejemplo anterior, el 4 es el índice 0, 2 (fila cero, columna 2)

for fila in matriz:
    for columna in fila:
        print(columna, end='\t') #le pongo un tabulador detrás d cada uno
    else:
        print()

- Quiero buscar los índices o recorrerlos
for idx_fila in range(len(matriz)):
    for idx_columna in range(len(matriz(idx_fila))):
        print(matriz[idx_fila][idx_columna], end='\t')
    else:
        print()

- Imprimir un índice concreto
print(matriz[0][2])

Las matrices parece que no se va a usar mucho, pero sí se usa. Incluso en juegos, como https://www.pygame.org/docs/

#COMPRESIÓN DE LISTAS
lista palabras = ['casa', 'mesa', 'manzana', 'pijama']
longitud de palabras = []

for palabra in lista_palabras:
    longitud_palabras.append(len(palabra))
print(longitud_palabras)

longitud_palabras = [len(palabra) for palabra in lista palabras]

ambos ejemplos son lo mismo

ejemplo2

num_pares = []

for num in range[0,21]:
    if num % 2 == 0
        num_pares.append(num)
print(num_pares)

num_pares = [num for num in range[0,21]  if num % 2 == 0]
