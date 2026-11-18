# Módulo 3 · Funciones y colecciones

Apuntes ampliados a partir de la guía de Ana Isabel Vegas, `Ejemplo06_Funciones.zip`, las explicaciones de recuperación de clase y tus notas. Actualización: 18 de noviembre de 2026.

**Estado:** desarrollada la parte de funciones. La parte de colecciones queda pendiente de integrar a medida que avance la clase. Este documento no constituye todavía los apuntes completos del módulo 3.

**Alcance actual:** funciones del ZIP 06 y páginas 35–37 del PDF. La guía continúa con listas, tuplas, conjuntos y diccionarios en las páginas 38–43. Se añaden aplicaciones a automatización e IA sin introducir todavía llamadas a servicios, archivos ni gestión de excepciones.

**Cómo leerlo:** las notas **Aclaración** explican matices; las **Correcciones del material** identifican discrepancias; los **Complementos opcionales** amplían lo necesario para tus proyectos. El contenido de la guía que no aparece en el ZIP se identifica expresamente. No se presupone qué se explicó oralmente ni qué entrará en el examen.

Se conserva tu archivo [modulo3.md](modulo3.md), incluidos sus apuntes de listas. Los ejemplos se han adaptado para facilitar el estudio; no se han modificado los archivos de clase. Cada bloque Python de estos apuntes incluye lo necesario para ejecutarlo por separado.

## Índice de la parte de funciones

1. [Qué es una función y para qué sirve](#1-qué-es-una-función-y-para-qué-sirve)
2. [Definir, llamar y seguir la ejecución](#2-definir-llamar-y-seguir-la-ejecución)
3. [Parámetros, argumentos y anotaciones](#3-parámetros-argumentos-y-anotaciones)
4. [La diferencia entre print y return](#4-la-diferencia-entre-print-y-return)
5. [Variables locales y cambios de estado](#5-variables-locales-y-cambios-de-estado)
6. [Ejercicio 1: calculadora con cinco funciones](#6-ejercicio-1-calculadora-con-cinco-funciones)
7. [Ejercicio 2: precio con descuento](#7-ejercicio-2-precio-con-descuento)
8. [Ejercicio 3: contar vocales](#8-ejercicio-3-contar-vocales)
9. [Ejercicio 4: área de un triángulo](#9-ejercicio-4-área-de-un-triángulo)
10. [Dos ampliaciones de la guía: tuplas y argumentos variables](#10-dos-ampliaciones-de-la-guía-tuplas-y-argumentos-variables)
11. [Función y método: puente hacia las listas](#11-función-y-método-puente-hacia-las-listas)
12. [Funciones útiles para tu ámbito](#12-funciones-útiles-para-tu-ámbito)
13. [Cómo revisar funciones y comprobar resultados](#13-cómo-revisar-funciones-y-comprobar-resultados)
14. [Mapa del material y próximos pasos](#14-mapa-del-material-y-próximos-pasos)

## Parte I · Funciones

## 1. Qué es una función y para qué sirve

Una función agrupa instrucciones bajo un nombre. Podemos llamarla cuando necesitamos ejecutar esas instrucciones y, si corresponde, pasarle datos y recibir un resultado.

Hasta ahora escribías directamente los pasos de cada programa. Si querías repetir un cálculo en otro lugar, podías acabar copiando el código. Una función permite expresar ese cálculo una vez y reutilizarlo con datos diferentes.

```python
def saludar():
    print("Buenas tardes")

saludar()
saludar()
```

Muestra el saludo dos veces. La función contiene una sola instrucción, pero podría contener varias, incluidos condicionales y bucles como los del módulo 2.

| Elemento | Qué significa |
|---|---|
| `def` | Empieza la definición de una función. |
| `saludar` | Nombre elegido para identificarla. |
| `()` en la definición | Lugar donde se declaran sus parámetros; aquí no hay ninguno. |
| `:` | Inicia el bloque de instrucciones. |
| Indentación | Delimita qué instrucciones pertenecen a la función. |
| `saludar()` fuera de la definición | Llamada que ejecuta la función. |

Usa nombres que describan una acción: `calcular_precio`, `contar_vocales` o `validar_divisor`. La convención habitual es escribirlos en minúsculas y separar las palabras con guiones bajos. La guía usa algunos nombres con mayúscula inicial; eso no cambia la sintaxis ni el comportamiento.

### 1.1. Qué aporta a tus proyectos

En una automatización puedes reutilizar un cálculo de coste en una consola, un informe o una API. En tu pipeline editorial puedes separar operaciones pequeñas y comprobarlas de forma independiente. La utilidad no consiste solo en reducir líneas: permite explicar qué hace cada parte y detectar dónde aparece un fallo.

Una función de Python no es por sí sola un agente ni una herramienta conectada a un modelo. Más adelante podrá formar parte de una herramienta, pero habrá que definir cómo se invoca y qué entradas acepta.

## 2. Definir, llamar y seguir la ejecución

### 2.1. Definir no ejecuta el cuerpo

Al ejecutar una definición con `def`, Python crea la función y asocia su nombre. Las instrucciones de su cuerpo se ejecutan cuando se la llama.

```python
def saludar():
    print("Estoy dentro de la función")

print("Antes de llamar")
saludar()
print("Después de llamar")
```

Salida:

```text
Antes de llamar
Estoy dentro de la función
Después de llamar
```

La llamada hace que se ejecute el cuerpo y, cuando termina, el programa continúa después de esa llamada.

Escribir solo `saludar` permite referirse a la función; `saludar()` la ejecuta. En este módulo nos interesa la segunda forma. Pasar funciones como datos se puede estudiar después.

### 2.2. El ejemplo introductorio completo

Adaptado de `crear_funciones.py`:

```python
def saludar() -> None:
    print("Buenas tardes")

def despedir() -> str:
    mensaje = "Hasta mañana"
    return mensaje

def sumar(n1: int, n2: int) -> int:
    return n1 + n2

saludar()
msg = despedir()
print(despedir())
print(sumar(7, 2))
```

Salida:

```text
Buenas tardes
Hasta mañana
9
```

| Línea | Qué ocurre |
|---|---|
| `saludar()` | La función muestra el saludo y termina. |
| `msg = despedir()` | La función devuelve un texto que se guarda en `msg`; no se imprime. |
| `print(despedir())` | Se vuelve a llamar a `despedir` y se muestra su resultado. |
| `print(sumar(7, 2))` | Primero se calcula y devuelve nueve; después se imprime. |

En el archivo original, `despedir` se ejecuta dos veces. El primer resultado se guarda y el segundo se imprime. Si quisieras aprovechar el ya guardado, podrías usar `print(msg)`.

### 2.3. Cuándo debe existir una función

Cuando se ejecuta una llamada, el nombre de la función debe estar definido. En la calculadora, `dividir` puede escribirse antes que `validar_divisor` porque esa llamada interna no se ejecuta al definir `dividir`: se ejecuta después, cuando ambas funciones ya están definidas.

Para estos ejercicios resulta claro ordenar el archivo así: definiciones de funciones → lectura de entradas → llamadas y presentación de resultados.

## 3. Parámetros, argumentos y anotaciones

### 3.1. Recibir datos

Los **parámetros** son los nombres que aparecen en la definición. Los **argumentos** son los datos que entregas al llamar.

```python
def sumar(n1, n2):
    return n1 + n2

primero = 7
segundo = 2
resultado = sumar(primero, segundo)
print(resultado)  # 9
```

| Lugar | Nombre o valor |
|---|---|
| Programa principal | `primero` vale siete y `segundo` vale dos. |
| Llamada | Se pasan esos dos valores, en ese orden. |
| Dentro de la función | `n1` recibe siete y `n2` recibe dos. |
| Después de `return` | `resultado` recibe nueve. |

Los nombres de fuera y de dentro no tienen que coincidir. En las llamadas posicionales, la correspondencia depende del orden.

Una función con dos parámetros obligatorios necesita dos argumentos. Una llamada como `sumar()` o `sumar(7)` produce `TypeError`. Pasar más argumentos de los admitidos también puede producirlo; la excepción es cuando la función está definida para recibirlos, como veremos con `*valores`.

### 3.2. Anotaciones de tipo

La profesora utiliza esta forma:

```python
def sumar(n1: int, n2: int) -> int:
    return n1 + n2

print(sumar(7, 2))  # 9
```

- `n1: int` y `n2: int` indican que se esperan enteros.
- `-> int` indica que se espera devolver un entero.
- Las anotaciones son opcionales y facilitan la lectura y la revisión con herramientas.

**Aclaración:** las anotaciones no convierten entradas ni aplican automáticamente una validación en ejecución. Si un dato viene de `input()`, sigue siendo texto hasta convertirlo explícitamente. Este comportamiento está documentado en la [introducción de typing](https://docs.python.org/es/3.14/library/typing.html).

Anotar `dato: int = "7"` no transforma ese texto en un entero. Para convertirlo necesitas, por ejemplo, `int("7")`. No conviene escribir anotaciones que contradigan el código.

### 3.3. Argumentos por nombre y valores por defecto

**Complemento opcional de uso práctico.** No aparece desarrollado en los ejercicios del ZIP, pero ayuda a entender llamadas habituales en código generado por IA.

```python
def calcular_precio(precio: float, dto: float = 0) -> float:
    return precio - precio * dto / 100

print(calcular_precio(100))                  # 100.0
print(calcular_precio(100, 20))              # 80.0
print(calcular_precio(precio=100, dto=20))    # 80.0
print(calcular_precio(dto=20, precio=100))    # 80.0
```

`dto=0` en la definición proporciona un valor si se omite ese argumento. En una llamada como `calcular_precio(dto=20, precio=100)`, los nombres indican la correspondencia y permiten cambiar el orden de esos argumentos.

No confundas un valor por defecto con una asignación dentro del cuerpo. Si escribieras `dto = 0` dentro de la función antes del cálculo, sobrescribirías el descuento recibido en cada llamada.

## 4. La diferencia entre print y return

Esta distinción es el centro del ejemplo 06.

| Instrucción | Efecto |
|---|---|
| `print(valor)` | Muestra una representación del valor por pantalla. |
| `return valor` | Termina la función y entrega el valor al código que la llamó. |
| Terminar sin `return` con valor | Devuelve `None`. |
| `return` sin un valor detrás | Termina la función devolviendo `None`. |

### 4.1. Mostrar y calcular son comportamientos distintos

```python
def mostrar_suma(a, b):
    print(a + b)

def calcular_suma(a, b):
    return a + b

mostrado = mostrar_suma(3, 4)
calculado = calcular_suma(3, 4)

print("Valor de mostrado:", mostrado)
print("Valor de calculado:", calculado)
print("Doble:", calculado * 2)
```

Salida:

```text
7
Valor de mostrado: None
Valor de calculado: 7
Doble: 14
```

`mostrar_suma` imprime siete, pero no lo entrega como resultado de la llamada. `calcular_suma` lo devuelve y permite guardarlo, multiplicarlo o pasarlo a otra función.

`None` representa aquí la ausencia de un resultado útil. No equivale a cero ni a texto vacío. Intentar multiplicar `mostrado` por dos produciría `TypeError`.

Una función puede imprimir y devolver, pero ambas acciones deben estar escritas. Para cálculos que quieras reutilizar suele ser útil devolver el dato y decidir fuera cómo presentarlo.

### 4.2. return termina toda la función

```python
def validar_divisor(divisor: int) -> bool:
    if divisor == 0:
        return False
    return True

print(validar_divisor(0))  # False
print(validar_divisor(2))  # True
```

Con cero, se ejecuta el primer `return` y ya no se llega al segundo. Por eso la alternativa no necesita aquí un `else`, aunque escribirlo como hace la profesora también es correcto.

Dentro de un bucle, `break` termina ese bucle; `return` termina la función que lo contiene. No se pueden intercambiar sin pensar en ese alcance.

### 4.3. Todas las ramas deben tener el resultado que prometen

Si una función devuelve un número solo cuando se cumple un `if`, pero en los demás casos llega al final sin devolver nada, sus resultados serán unas veces números y otras `None`.

No es necesariamente ilegal, pero quien la llame debe conocerlo. Al revisar una función, recorre todas las ramas y pregunta qué recibe el programa en cada una. En este módulo mantendremos contratos sencillos: una función de validación devuelve un booleano y una de cálculo devuelve su resultado para entradas válidas.

## 5. Variables locales y cambios de estado

Los parámetros y las variables que asignas normalmente dentro de una función son locales a esa llamada. Un acumulador como `contador` vuelve a inicializarse cuando se ejecuta de nuevo su asignación.

```python
def duplicar(numero: int) -> int:
    resultado = numero * 2
    return resultado

primero = duplicar(3)
segundo = duplicar(5)
print(primero, segundo)  # 6 10
```

El `resultado` de una llamada no se utiliza automáticamente como punto de partida de la siguiente. Tampoco puedes acceder normalmente a esa variable local escribiendo `print(resultado)` fuera de la función: allí debes usar el valor que has recogido, como `primero`.

### 5.1. Reasignar un número dentro no cambia el nombre de fuera

```python
def aplicar_descuento(precio: float) -> float:
    precio = precio * 0.90
    return precio

precio = 100
nuevo_precio = aplicar_descuento(precio)

print(precio)        # 100
print(nuevo_precio)  # 90.0
```

La asignación interna asocia el parámetro local a otro valor. No reasigna la variable `precio` del programa principal.

**Puente hacia las colecciones:** una lista puede modificarse a través de una referencia compartida. Eso es distinto de reasignar un parámetro a un número y se desarrollará en la parte de listas. No generalices este ejemplo diciendo que «una función nunca puede cambiar un objeto recibido».

Por ahora, intenta que las funciones de cálculo reciban los datos necesarios por parámetros y devuelvan resultados. Así no dependen de que una variable global tenga cierto nombre o haya sido preparada antes.

## 6. Ejercicio 1: calculadora con cinco funciones

**Fuente:** `Ejemplo06_Funciones/ejercicio1.py` dentro del [ZIP de funciones](../../Ejemplo06_Funciones.zip).

El enunciado pide dos números y cinco funciones:

| Función | Qué recibe | Qué hace |
|---|---|---|
| `sumar` | Dos enteros. | Muestra la suma. |
| `restar` | Dos enteros. | Muestra la resta. |
| `multiplicar` | Dos enteros. | Muestra el producto. |
| `dividir` | Dos enteros. | Comprueba el divisor y muestra el cociente o un mensaje. |
| `validar_divisor` | El divisor. | Devuelve `True` o `False`. |

### 6.1. Versión adaptada con anotaciones coherentes

```python
def sumar(n1: int, n2: int) -> None:
    suma = n1 + n2
    print(f"{n1} + {n2} = {suma}")

def restar(n1: int, n2: int) -> None:
    resta = n1 - n2
    print(f"{n1} - {n2} = {resta}")

def multiplicar(n1: int, n2: int) -> None:
    multiplicacion = n1 * n2
    print(f"{n1} * {n2} = {multiplicacion}")

def validar_divisor(divisor: int) -> bool:
    return divisor != 0

def dividir(n1: int, n2: int) -> None:
    correcto = validar_divisor(n2)
    if correcto:
        division = n1 / n2
        print(f"{n1} / {n2} = {division}")
    else:
        print("Lo siento, no puedo hacer la división")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

sumar(numero1, numero2)
restar(numero1, numero2)
multiplicar(numero1, numero2)
dividir(numero1, numero2)
```

Con siete y dos:

```text
7 + 2 = 9
7 - 2 = 5
7 * 2 = 14
7 / 2 = 3.5
```

### 6.2. Una función llama a otra

Al ejecutar `dividir(7, 2)`:

1. Los parámetros `n1` y `n2` reciben siete y dos.
2. `validar_divisor(n2)` recibe dos y devuelve `True`.
3. Ese booleano se guarda en `correcto`.
4. El `if` permite calcular y mostrar la división.
5. `dividir` llega al final y devuelve `None`.

Con `dividir(7, 0)`, la validación devuelve `False` y se muestra el mensaje sin ejecutar la división.

`if correcto:` expresa la misma comprobación que `if correcto == True:` cuando `correcto` es ese booleano. La versión de clase usa la segunda forma; ambas funcionan aquí.

### 6.3. Correcciones y diferencias entre archivos

**Corrección del material:** en el archivo de la profesora, `sumar`, `restar` y `multiplicar` llevan `-> int`; `dividir` lleva `-> float`. Sin embargo, esas cuatro funciones solo imprimen y no devuelven los números calculados. Su resultado real es `None`. La versión anterior corrige sus anotaciones, conservando el comportamiento pedido.

En `crear_funciones.py`, la función llamada `sumar` sí contiene `return` y devuelve el número. En `ejercicio1.py`, otra función con ese mismo nombre imprime. El nombre no determina el comportamiento: hay que leer su cuerpo y el archivo en el que está definida.

También recuerda que `int(input(...))` puede fallar si introduces texto no convertible. Proteger la división por cero no resuelve los errores de formato. Aprenderás a gestionarlos con excepciones en el módulo 4.

## 7. Ejercicio 2: precio con descuento

**Fuente:** `Ejemplo06_Funciones/ejercicio2.py`.

La función recibe el precio y el descuento como porcentaje entero o decimal —por ejemplo, veinte para un veinte por ciento— y devuelve el precio final.

```python
def calcular_precio(precio, dto) -> float:
    importe_dto = precio * dto / 100
    nuevo_precio = precio - importe_dto
    return nuevo_precio

print(calcular_precio(24.56, 10))
print(calcular_precio(18, 5))
print(calcular_precio(100, 20))
print(calcular_precio(225, 25))
```

| Llamada | Descuento calculado | Precio final |
|---|---|---|
| `calcular_precio(24.56, 10)` | 2.456 | 22.104 |
| `calcular_precio(18, 5)` | 0.9 | 17.1 |
| `calcular_precio(100, 20)` | 20.0 | 80.0 |
| `calcular_precio(225, 25)` | 56.25 | 168.75 |

### 7.1. Separar cálculo y presentación

```python
def calcular_precio(precio, dto) -> float:
    return precio - precio * dto / 100

final = calcular_precio(24.56, 10)
print(f"Precio final: {final:.2f} €")  # 22.10 €
```

La función devuelve el número y el programa decide mostrar dos decimales. `:.2f` formatea el mensaje; no cambia la variable `final`.

### 7.2. Qué debemos aclarar antes de reutilizarla

- El descuento esperado es `20`, no `0.20`, porque dentro ya se divide entre cien.
- En este ejercicio se presupone un precio no negativo y un descuento entre cero y cien.
- La función original no valida esos límites: con un descuento de ciento veinte produciría un precio negativo.
- Las operaciones con `float` son adecuadas para practicar. Un programa que gestione dinero real deberá fijar reglas de precisión y redondeo; no basta con mostrar dos decimales.

De momento, podemos comprobar los límites antes de llamar o documentar esas condiciones de entrada. Más adelante veremos formas de comunicar y gestionar un error sin mezclar mensajes con resultados numéricos.

## 8. Ejercicio 3: contar vocales

**Fuente:** `Ejemplo06_Funciones/ejercicio3.py`.

La función combina un parámetro de texto, un recorrido, un contador y un resultado entero.

```python
def contar_vocales(palabra) -> int:
    contador = 0
    for letra in palabra.lower():
        if letra in "aeiou":
            contador += 1
    return contador

print(contar_vocales("Mesa"))         # 2
print(contar_vocales("frigorifico"))  # 5
print(contar_vocales("arbol"))        # 2
print(contar_vocales("codigo"))       # 3
print(contar_vocales("portatil"))     # 3
```

### 8.1. Leer cada pieza

| Fragmento | Función dentro del algoritmo |
|---|---|
| `contador = 0` | Inicializa la cuenta en cada llamada. |
| `palabra.lower()` | Obtiene una versión en minúsculas del texto. |
| `for letra in ...` | Recorre cada carácter. |
| `letra in "aeiou"` | Comprueba pertenencia al texto que contiene las vocales admitidas. |
| `contador += 1` | Cuenta una aparición, no una vocal distinta. |
| `return contador` | Entrega el total después de revisar el texto completo. |

Para `"Mesa"`:

| Letra revisada | ¿Cuenta? | Contador después |
|---|---|---|
| m | No. | 0 |
| e | Sí. | 1 |
| s | No. | 1 |
| a | Sí. | 2 |

`return` está fuera del `for`, aunque dentro de la función. Si lo metieras en el bucle, terminarías la función en la primera vuelta. Si el texto está vacío, no hay vueltas y se devuelve cero.

### 8.2. Qué hace y qué no hace lower

`lower` cambia mayúsculas a minúsculas. No elimina tildes: `"Á"` pasa a `"á"`, no a `"a"`.

Por tanto, la versión del ZIP cuenta una vocal en `"árbol"` —la o— y dos en `"código"` —la i y la o—. Las vocales acentuadas no pertenecen a `"aeiou"`.

**Ampliación pequeña para textos en español:**

```python
def contar_vocales_es(texto: str) -> int:
    contador = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóúü":
            contador += 1
    return contador

print(contar_vocales_es("Árbol"))     # 2
print(contar_vocales_es("código"))    # 3
print(contar_vocales_es("pingüino"))  # 4
```

Esta ampliación sirve para los textos habituales del ejemplo. La normalización de Unicode y el tratamiento detallado de idiomas se pueden estudiar después; no hacen falta para entender la función de clase.

### 8.3. Conexión con tu pipeline editorial

Aquí estás practicando la forma de una función que recibe texto y devuelve una medida. Más adelante podrás aplicar ese esquema a comprobaciones editoriales concretas. Un conteo de vocales no evalúa calidad literaria: primero hay que definir qué propiedad queremos medir y cómo comprobarla.

## 9. Ejercicio 4: área de un triángulo

**Fuente:** `Ejemplo06_Funciones/ejercicio4.py`.

```python
def area_triangulo(base, altura):
    return base * altura / 2

dato1 = float(input("Introduce la base del triángulo: "))
dato2 = float(input("Introduce la altura del triángulo: "))

print(f"{area_triangulo(dato1, dato2):.2f}")
```

Con base tres y altura cuatro, calcula `3 * 4 / 2`, devuelve `6.0` y muestra `6.00`.

El ejemplo deja bien separadas tres tareas:

1. Fuera de la función: recibir y convertir las entradas.
2. Dentro: calcular el resultado.
3. Fuera: presentar ese resultado con el formato deseado.

Que la función no tenga anotaciones no impide que reciba datos ni devuelva un valor. Podría anotarse como `def area_triangulo(base: float, altura: float) -> float:`.

La base y la altura deben estar expresadas en la misma unidad; el área resultará en esa unidad al cuadrado. Para un triángulo no degenerado se esperan dimensiones positivas. El código original calcula la fórmula sin validar ese requisito.

No hace falta repetir el `input` para usar la función en otro contexto: se puede llamar como `area_triangulo(10, 5)` y recoger `25.0` desde cualquier parte donde esté disponible.

## 10. Dos ampliaciones de la guía: tuplas y argumentos variables

**Origen y alcance:** estos dos temas están en las páginas 36–37 del PDF, pero no aparecen desarrollados en el ZIP 06. Se incluyen para recoger la parte de funciones de la guía. No se da por hecho que se explicaran durante la sesión a la que faltaste. La colección correspondiente se ampliará después.

### 10.1. Retornar más de un resultado

La guía utiliza una función que calcula suma y resta. Adaptando sus nombres:

```python
def sumar_restar(a: int, b: int):
    return a + b, a - b

suma, resta = sumar_restar(7, 2)
print("Suma:", suma)    # 9
print("Resta:", resta)  # 5
```

La coma permite agrupar los resultados. Técnicamente se devuelve **una tupla con dos elementos**; la asignación `suma, resta = ...` los desempaqueta en dos variables.

El orden cuenta: la primera variable recibe el primer elemento y la segunda el segundo. Si intentaras recoger dos elementos en tres variables, la asignación fallaría.

No conseguirías lo mismo poniendo dos `return` consecutivos: el primero terminaría la función y el segundo no se ejecutaría. En cambio, devolver ambos valores juntos conserva los dos resultados en una sola salida.

### 10.2. Recibir un número variable de argumentos posicionales

La guía añade un asterisco delante de un parámetro:

```python
def sumar_varios(*valores):
    resultado = 0
    for valor in valores:
        resultado += valor
    return resultado

print(sumar_varios(23, 56, 3, 89, 78, 455))  # 704
print(sumar_varios(3, 8))                   # 11
print(sumar_varios())                       # 0
```

`*valores` recoge los argumentos posicionales recibidos en una tupla que podemos recorrer. Podrás ver el nombre `*args` en otros programas: el nombre es convencional; el asterisco es lo que le da este comportamiento.

**Corrección del material:** el texto del PDF dice que esos parámetros se reciben «como una lista». En este caso se reciben como una **tupla**, aunque se recorran con un `for` de forma parecida.

Con cero argumentos, el recorrido está vacío y se conserva el acumulador inicial, cero. Con varios, se suman todos. Se esperan valores numéricos compatibles con la suma; el asterisco no valida su contenido.

No necesitamos introducir todavía `**kwargs`, desempaquetados más complejos ni combinaciones avanzadas de parámetros.

## 11. Función y método: puente hacia las listas

En tus notas de listas preguntas si es correcto distinguir `len(lista)` y `lista.append(...)`. Sí: la distinción básica va por ahí.

| Forma | Qué estás llamando |
|---|---|
| `len(lista)` | Una función incorporada a la que pasas un objeto. |
| `lista.append("x")` | Un método asociado al objeto lista, que añade un elemento. |
| `texto.lower()` | Un método del objeto de texto, que devuelve su versión en minúsculas. |

`append` está definido por el tipo `list`; `lower`, por el tipo `str`. No hace falta estudiar ahora cómo se implementan las clases: el módulo 5 desarrollará esa parte.

```python
nombres = ["Vera", "Noa"]

cantidad = len(nombres)
resultado_append = nombres.append("Laura")

print(cantidad)          # 2
print(nombres)           # ['Vera', 'Noa', 'Laura']
print(resultado_append)  # None
```

Este ejemplo conecta con `return`: `append` modifica la lista y devuelve `None`. Por eso no debes hacer `nombres = nombres.append("Laura")` esperando conservar la lista en `nombres`: guardarías `None` en ese nombre.

`cantidad` sigue valiendo dos porque se calculó antes de añadir el elemento. No se actualiza automáticamente al cambiar la lista; habría que volver a llamar a `len(nombres)`.

**Matiz:** no todo método modifica el objeto. `texto.lower()` devuelve otro texto y no modifica la cadena original. La operación concreta determina si devuelve un resultado, cambia un objeto o hace ambas cosas. Una expresión con punto también puede acceder a un atributo; no basta ver un punto para concluir que se está llamando a un método.

El comportamiento de `append`, índices y otras operaciones se desarrollará en la parte de colecciones, junto con tus apuntes actuales de listas.

## 12. Funciones útiles para tu ámbito

**Complemento opcional.** La formación de Python refuerza el módulo 3 de tu máster personalizado, «APIs, webhooks y Python práctico». Estas aplicaciones usan cálculos y reglas locales. No llaman a servicios ni realizan acciones externas.

### 12.1. Convertir un cálculo de coste en una función reutilizable

En el módulo 1 calculamos un coste de tokens con variables. Ahora podemos agrupar la operación y reutilizarla. Las tarifas son ficticias y están expresadas en euros por millón de tokens.

```python
def estimar_coste_tokens(
    tokens_entrada: int,
    tokens_salida: int,
    euros_millon_entrada: float,
    euros_millon_salida: float,
) -> float:
    """Calcula un coste simulado en euros con tarifas por millón."""
    coste_entrada = tokens_entrada * euros_millon_entrada / 1_000_000
    coste_salida = tokens_salida * euros_millon_salida / 1_000_000
    return coste_entrada + coste_salida

coste = estimar_coste_tokens(1200, 300, 0.50, 2.00)
print(f"Coste por llamada: {coste:.6f} €")
print(f"Mil llamadas iguales: {coste * 1000:.2f} €")
```

Salida:

```text
Coste por llamada: 0.001200 €
Mil llamadas iguales: 1.20 €
```

La función devuelve un número que puedes usar para un presupuesto o para una suma de consumos. Recibe las tarifas por parámetros para poder cambiar el supuesto sin reescribir la fórmula.

Las líneas de parámetros van entre paréntesis, lo que permite repartirlas entre varias líneas. La coma después del último parámetro es válida. La cadena entre comillas triples al principio del cuerpo es una **docstring**: documenta la función; no se imprime por sí sola.

Se presuponen cantidades y tarifas no negativas. Este modelo no incorpora caché, reintentos ni diferencias de facturación y no representa una cotización real. Lo que se estudia aquí es cómo encapsular una fórmula con unidades claras.

### 12.2. Comprobar requisitos antes de procesar una tarea

```python
def puede_procesarse(
    datos_completos: bool,
    permiso_valido: bool,
    coste_estimado: float,
    presupuesto: float,
) -> bool:
    return (
        datos_completos
        and permiso_valido
        and 0 <= coste_estimado <= presupuesto
    )

permitido = puede_procesarse(True, True, 0.03, 0.05)

if permitido:
    print("La tarea cumple los requisitos simulados")
else:
    print("La tarea necesita revisión")
```

La función concentra una regla y devuelve un booleano. El programa principal decide qué hacer con él. Puede usarse también en pruebas con combinaciones de datos diferentes.

En este ejemplo los booleanos y los importes son datos de simulación. En una aplicación real, el permiso debe proceder de una fuente válida y comprobarse donde se realiza la acción. Una función local que devuelve `True` no sustituye esos controles.

### 12.3. Preparar una pieza para un pipeline

En un pipeline editorial, la secuencia puede expresarse mediante funciones que reciben un dato y devuelven otro. Por ejemplo, separar la detección de una incidencia del mensaje que muestra la interfaz permite reutilizar la comprobación cuando cambies de consola a aplicación.

| Pieza | Qué conviene poder describir |
|---|---|
| Entradas | Datos necesarios y su significado. |
| Resultado | Qué devuelve en cada caso. |
| Reglas | Qué condiciones se consideran válidas. |
| Efectos | Si solo calcula o también modifica algo o llama a un sistema. |
| Comprobaciones | Casos con resultado esperado para detectar cambios indeseados. |

Ese esquema será útil cuando funciones de Python se utilicen como herramientas de un agente. El código debe seguir siendo comprobable aunque el modelo elija cuándo llamarlo.

Una función definida con `def` no conserva automáticamente una conversación ni su estado entre llamadas. Si el resultado depende de información previa, habrá que pasarla o gestionarla de forma explícita; las colecciones y, después, archivos y bases de datos ayudarán a hacerlo.

### 12.4. Qué reforzar ahora y qué posponer

Prioriza parámetros claros, diferencias entre mostrar y devolver, cobertura de ramas y funciones pequeñas que puedas explicar. Para tus proyectos, poder revisar estas piezas aporta más ahora que introducir un framework de agentes.

| Tema | Cuándo incorporarlo |
|---|---|
| Funciones que reciben listas o devuelven diccionarios | Al completar las colecciones de este módulo. |
| Limpieza y normalización de textos en detalle | Métodos de cadenas del módulo 4; `lower` se usa ahora porque aparece en clase. |
| Comunicar y recuperar errores | Excepciones del módulo 4. |
| Repartir funciones entre archivos e importarlas | Módulos e importaciones del módulo 4. |
| Leer y guardar resultados | Archivos del módulo 5; otras formas de persistencia se verán en proyectos. |
| API, JSON, autenticación, reintentos e idempotencia | Puente del máster después de estas bases. |
| Decoradores, recursividad, funciones asíncronas y tipado avanzado | Cuando un caso concreto los necesite. |

## 13. Cómo revisar funciones y comprobar resultados

### 13.1. Lista de preguntas para leer una función

1. ¿Qué recibe y qué significa cada parámetro?
2. ¿Usa esos datos o depende de variables externas?
3. ¿Qué devuelve en cada rama? ¿Puede acabar devolviendo `None` sin querer?
4. ¿Imprime, modifica objetos o realiza alguna otra acción?
5. ¿Las anotaciones coinciden con lo que hace el código?
6. ¿Los bucles terminan y los acumuladores se inicializan donde corresponde?
7. ¿Qué condiciones de entrada presupone y cuáles valida?

No hace falta extraer una función por cada línea. Es útil cuando nombra una operación con sentido, se reutiliza o permite probar una regla de forma separada.

### 13.2. Resultados de referencia

| Función o ejemplo | Entrada | Resultado o comportamiento |
|---|---|---|
| `sumar` de la introducción | 7 y 2 | Devuelve 9. |
| `sumar` de la calculadora | 7 y 2 | Imprime la suma y devuelve `None`. |
| `validar_divisor` | 0; 2; −3 | `False`; `True`; `True`. |
| `dividir` de la calculadora | 7 y 0 | Muestra el mensaje y evita la división. |
| `calcular_precio` | 100 y 20 | 80.0. |
| `calcular_precio` | 100 y 0 | 100.0. |
| `calcular_precio` | 100 y 100 | 0.0. |
| `contar_vocales` original | `"Mesa"`; `""`; `"AEIOU"` | 2; 0; 5. |
| `contar_vocales` original | `"árbol"` | 1, porque no incluye la vocal acentuada. |
| `contar_vocales_es` ampliada | `"Árbol"`; `"pingüino"` | 2; 4. |
| `area_triangulo` | Base 3 y altura 4 | 6.0; presentado con dos decimales, 6.00. |
| `sumar_restar` | 7 y 2 | Tupla con 9 y 5, desempaquetable. |
| `sumar_varios` | Sin argumentos | 0. |
| `sumar_varios` | 23, 56, 3, 89, 78 y 455 | 704. |
| Coste de tokens simulado | 1200, 300, 0.50 y 2.00 | 0.0012 euros. |
| Requisitos simulados | Datos y permiso válidos; coste 0.03; presupuesto 0.05 | `True`. |
| Requisitos simulados | Falta permiso; mismo coste y presupuesto | `False`. |
| Requisitos simulados | Coste 0.06 y presupuesto 0.05 | `False`. |

Estas comprobaciones sirven para contrastar resultados después de un cambio. En cálculos con decimales habrá que considerar su precisión al comparar valores; la presentación y el redondeo no sustituyen la definición de la regla.

### 13.3. Errores frecuentes

| Síntoma | Qué revisar |
|---|---|
| La función no hace nada visible | Puede que no se la esté llamando o que devuelva un dato que no se imprime. |
| Sale `None` al imprimir una llamada | Puede que la función solo imprima o que alguna rama no tenga `return` con valor. |
| `TypeError` por argumentos | Cantidad, nombres y tipos de los argumentos recibidos. |
| `NameError` al leer una variable | Puede ser local a otra función o no estar definida todavía. |
| Solo se revisa la primera letra | `return` puede estar dentro del bucle. |
| El resultado ignora un argumento | El cuerpo puede sobrescribir el parámetro con un valor fijo. |
| Una cuenta acumula resultados de llamadas anteriores | Puede depender de estado compartido; comprobar dónde se inicializa. |
| Una anotación promete un entero y aparece texto | Las anotaciones no validan ni convierten por sí solas. |
| La lista acaba siendo `None` | Puede haberse asignado el resultado de un método que modifica y no devuelve la lista. |

### 13.4. Cinco ideas para recordar

- `def` define; los paréntesis de la llamada ejecutan.
- Los parámetros reciben los argumentos de la llamada.
- `print` muestra; `return` entrega un valor y termina la función.
- Al terminar sin un resultado explícito se devuelve `None`.
- El contrato real se descubre leyendo todas las ramas, no solo el nombre o la anotación.

## 14. Mapa del material y próximos pasos

### 14.1. Qué aporta cada archivo del ZIP

| Archivo | Tema principal | Matiz relevante |
|---|---|---|
| `crear_funciones.py` | Definir y llamar; funciones con y sin resultado; parámetros y anotaciones. | `msg = despedir()` guarda sin imprimir. |
| `ejercicio1.py` | Composición de funciones y validación booleana. | Las anotaciones de las cuatro operaciones no coinciden con su retorno real. |
| `ejercicio2.py` | Cálculo reutilizable con dos parámetros y retorno numérico. | Expresar el porcentaje en la unidad esperada. |
| `ejercicio3.py` | Texto, bucle, contador y retorno. | `lower` no elimina tildes y el contador se devuelve al finalizar. |
| `ejercicio4.py` | Separación de entrada, cálculo y presentación. | `:.2f` es presentación; las unidades deben ser coherentes. |

### 14.2. Fuentes de estos apuntes

- [Guía IFCD0062 Fundamentos programacion Python.pdf](<../../IFCD0062 Fundamentos programacion Python.pdf>): funciones en pp. 35–37; se ha consultado la distribución posterior para delimitar ampliaciones.
- [Ejemplo06_Funciones.zip](../../Ejemplo06_Funciones.zip): introducción y cuatro ejercicios completos. Según lo indicado en clase, no se esperan ampliaciones de este ZIP.
- [modulo3.md](modulo3.md): tus notas actuales y el comienzo de colecciones. Se conservan para continuar integrando el módulo.
- [Apuntes ampliados del módulo 2](../modulo2/modulo2_apuntes_ampliados.md): control de flujo, estado y bucles que ahora se encapsulan en funciones.
- [MASTER-PERSONALIZADO-IA.md](../../../../MASTER-PERSONALIZADO-IA.md) y [ENCAJE-TECNOFOR-MASTER.md](../../../../ENCAJE-TECNOFOR-MASTER.md): orientación de las aplicaciones y de los temas que se posponen.

Apoyo para consultar matices, sin lectura adicional obligatoria:

- [Tutorial oficial: definición de funciones, parámetros y retornos](https://docs.python.org/es/3.14/tutorial/controlflow.html#defining-functions).
- [Documentación oficial: las anotaciones no se exigen en ejecución](https://docs.python.org/es/3.14/library/typing.html).

## Parte II · Colecciones — pendiente de integración

La clase ha empezado con listas. Esta parte se completará con las prácticas y tus comentarios cuando haya material suficiente para ordenar el conjunto.

Quedan por integrar las listas y sus operaciones, las tuplas, los conjuntos y los diccionarios de las páginas 38–43, junto con ejemplos de colecciones como entradas y salidas de funciones. El puente mínimo sobre `append`, `len`, tuplas y `*valores` de la parte I no sustituye ese desarrollo.

También queda anotada para el repaso de bucles tu duda sobre `else` en `for` y `while`. Al integrarla habrá que precisar que esa cláusula se ejecuta cuando el bucle termina sin un `break`, no simplemente por estar escrita después de un recorrido.

El PDF del módulo se preparará cuando estén desarrolladas e integradas ambas partes.
