'''
de la lista mostrar sólo las vocales
'''

datos = ['t', 'a', 'w', 'p', 'o', 'z', 'i']

'''
for letra in datos:
    match letra:
        case 'a'|'e'|'i'|'o'|'u':
            vocal = True
        case _:
            continue
if vocal:
    print(datos[letra])
mal: da error porque los índices tienen que ser enteros
corrección añadiendo que sólo se imprima si el índice es impar
'''

for index in range(len(datos)):
    if index % 2 != 0 and datos[index] in ['a','e','i','o','u']

#opcion 2

for index in range(len(datos)):
    if index % 2 != 0:
        match datos[index]:
            case 'a'|'e'|'i'|'o'|'u':
                print(datos[index])

#opcion 3

for index in range(len(datos)):
    if index % 2 != 0 and datos[index] == 'a' or datos[index] == 'e' or datos[index] == 'i' or datos[index] =='o' or datos[index] == 'u':
        print(datos[index])
