##Tipos de datos
Entero (int)
Real (float)
Complejo (número con parte imaginaria, no lo tratan)
Cadena de texto (str)
Booleanos (Bool) = True/False (primera en mayúscula)
Colecciones de datos:
    - Conjunto: elementos no ordenados y no repetidos.
    - Lista: ector de elementos que pueden ser distintos tipos de datos, ordenado y puede haber repetidos.
    - Tupla: lista inmutable de elementos.No admite cambios.
    - Diccionario: lista de elementos con claves y valores.

##Conversión
Toda entrada del usuario se interpreta como string
Para convertir a número entero pondremos int()
Por ejemplo suman = int(input('...))
y así con todos los tipos

float()
Para redondear números reales usamos round:
round(numero, numero de decimales)
Por defecto si no pones número de decimales los quita

str()
Para convertir a texto
El texto va entre comillas simples o dobles
Se pueden usar distintos caracteres especiales:
    \n salto de línea dentro de la cadena
    \\ para que salga una \
    \' o \" para que salga una comilla
    \t para introducir una tabulación
Para imprimir cadenas de texto se usa print()
    print('blabla', 'blable')
    las comas meten por defecto un espacio
    si quiero que sea otra cosa puedo usar sep='-' por ejemplo
    y si quiero que añada un final end='.'



##Operadores
- Cálculo
- Asignación
= es el principal
Asignación y cálculo unidos: +=, -=, *=, /=, %= (resto), **=, //= (división entera)
- Relacionales
>, <, >=, <=, == (igual que), != (distinto que)
- Operadores lógicos
and: cumple todas
or: cumple una de las condiciones
not: no cumple la condición
Devuelve un booleano

