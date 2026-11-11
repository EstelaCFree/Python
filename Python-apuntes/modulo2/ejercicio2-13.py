nombres = ['Luis', 'Jorge', 'María', 'Laura', 'Pedro']
#como van entre corchetes es una lista
#queremos recorrer la lista y poner todos los nombres

for elemento in nombres:
    print(elemento)

#crear una lista de números y mostrar la suma de todos
#mi propuesta:

numeros = [3, 8, 1, 5, 9]

for num in numeros:
    anterior = num
    num = anterior + num
print(num)
#Está mal porque al principio ha sumado dos veces el 3

#la profesora:

resultado = 0

for num in numeros:
    resultado += num

