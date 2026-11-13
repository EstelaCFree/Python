##Bloques e indentación
las indentaciones con tabuladores son una buena práctica y una forma de hacer visibles los bloques dentro del código. Puedes anidar bloques dentro de otros haciendo más indentaciones, y así quedan como capas.


##Condicionales - If, elif, else
if condicion:
    bloquedeintrucciones
elif condicion:
    bloquedeinstrucciones2
else:
    que pasa si no se cumplen ninguna

Siempre tiene que ser una condición que devuelva True o False, como los operadores de comparación.
Se indenta con una tabulación y eso permite leerlo mejor: son buenas prácticas.
No se necesitan los tres. la versión mínima es sólo el if.

ejercicio2-1 a 2-7

##Estructura Match_Case

match expresion: (expresión es todo lo que te da un resultado)
    case valor1:
        código
    case valor2:
        código
    case _: (cuando no han sido los otros, opcional como el else)
        código

Básicamente es como sustituir los condicionales por esto y que quede "más limpio".
Pero case tiene que ser un valor, no una condición

Ejercicio 2-8 es muy buen ejemplo porque convierte el 2-6 en un case. Ahí la expresión es una variable, pero por ejemplo el de par e impar:

match numero % 2:
    case 0:
        print(f'el número es par')
    case 1: 
        print(f'el número es impar')

Case 1 podría usarse case _

Para poner varias opciones en un case se pone | (alt-gr +1) entre ambas opciones. Se ve en el ejercicio2.9

ejercicio2-12: len() para medir la longitud de texto

##Bucles
Se ejecutan en bucle haciendo todo el rato x instrucciones hasta que se acabe la condición o la lista o lo que sea.
    - Bucle determinado: sabes qué cantidad de iteraciones se van a hacer. Suele usarse el bucle for.
    - Bucle indeterminado: no se sabe qué cantidad de veces se va a repetir el bucle.
Los bucles se ejecutan sobre elementos iterables como las colecciones (listas, tuplas, conjuntos o diccionatios) y cadenas de texto.
Como Python es un lenguaje de inferencia, es capaz de adivinar cosas como el tipo de dato, o por ejemplo al poner valores entre corchetes ya sabe que es una lista.
LISTAS
    Están ordenadas, con un índice que empieza por 0
    al declarar una variable que es una lista, estoy dclarando un puntero que apunta a la lista.
BUCLE FOR
    for (variable unitaria) in (lista)
        instrucción

la variable unitaria se le llama variable auxiliar y te inventas esa variable, puede ser pepito, pero es la que va a ir cambiando de valor en el bucle, como si fuera ese puntero que va avanzando en la lista por orden.

ver ejercicio 2-13

#RANGOS - eange

Es un generador de números
range(inicio, final, salto)
El número final no está incluido.
Si sólo pones el final, empezará en cero y saltará de uno en uno
Si queremos mostrar los números del 0 al 9:

for numero in range(10):
    print(numero)

esto va a poner un número dbajo del otro, con saltos de líneas.

Mirar ejercicio2-14 al 16 (que se van anidando bucles o se unen a condicionales)

BREAK
Ejemplo de un break rompiendo un bucle en ejercicio 2-17 
CONTINUE
Rompe la iteración actual pero sigue con la siguiente iteración del bucle, más inmediato





