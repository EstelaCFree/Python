# Módulo 3 · Funciones y colecciones

Apuntes ampliados a partir de la guía de Ana Isabel Vegas, los ZIP 06–10, las explicaciones de recuperación de clase y tus notas. Actualización: 23 de noviembre de 2026.

**Estado:** módulo 3 integrado con todo el material disponible: ocho archivos de funciones y ocho de colecciones. Incluye las ampliaciones del ejemplo 06, listas, tuplas, conjuntos y diccionarios. Las explicaciones amplían los ejemplos para que puedas seguirlos sin haber asistido a todas las clases.

**Alcance:** módulo 3 del PDF, portada en p. 34 y contenido en pp. 35–43. Funciones: pp. 35–37 y ZIP 06; listas: pp. 38–40 y ZIP 07; tuplas: p. 41 y ZIP 08; conjuntos: p. 42 y ZIP 09; diccionarios: p. 43 y ZIP 10. El módulo 4 empieza en p. 44: excepciones, importaciones y paquetes quedan para después. Las ampliaciones de los ZIP, como las comprensiones de listas, se integran en su tema.

**Cómo leerlo:** las notas **Aclaración** explican matices; las **Correcciones del material** identifican discrepancias; los **Complementos opcionales** amplían lo necesario para tus proyectos. El contenido de la guía que no aparece en el ZIP se identifica expresamente. No se presupone qué se explicó oralmente ni qué entrará en el examen.

Se conserva tu archivo [modulo3.md](modulo3.md), incluidos sus apuntes de listas. Los ejemplos se han adaptado para facilitar el estudio; no se han modificado los archivos de clase. Cada bloque Python de estos apuntes incluye lo necesario para ejecutarlo por separado.

## Índice

1. [Qué es una función y para qué sirve](#1-qué-es-una-función-y-para-qué-sirve)
2. [Definir, llamar y seguir la ejecución](#2-definir-llamar-y-seguir-la-ejecución)
3. [Parámetros, argumentos y anotaciones](#3-parámetros-argumentos-y-anotaciones)
4. [La diferencia entre print y return](#4-la-diferencia-entre-print-y-return)
5. [Variables locales y cambios de estado](#5-variables-locales-y-cambios-de-estado)
6. [Ejercicio 1: calculadora con cinco funciones](#6-ejercicio-1-calculadora-con-cinco-funciones)
7. [Ejercicio 2: precio con descuento](#7-ejercicio-2-precio-con-descuento)
8. [Ejercicio 3: contar vocales](#8-ejercicio-3-contar-vocales)
9. [Ejercicio 4: área de un triángulo](#9-ejercicio-4-área-de-un-triángulo)
10. [Funciones ampliadas: varios retornos, argumentos variables y medias](#10-funciones-ampliadas-varios-retornos-argumentos-variables-y-medias)
11. [Función y método: puente hacia las listas](#11-función-y-método-puente-hacia-las-listas)
12. [Funciones útiles para tu ámbito](#12-funciones-útiles-para-tu-ámbito)
13. [Cómo revisar funciones y comprobar resultados](#13-cómo-revisar-funciones-y-comprobar-resultados)
14. [Mapa de funciones y conexión con colecciones](#14-mapa-de-funciones-y-conexión-con-colecciones)
15. [Elegir una colección](#15-elegir-una-colección)
16. [Listas: crear, consultar y modificar](#16-listas-crear-consultar-y-modificar)
17. [Recorridos y else en bucles](#17-recorridos-y-else-en-bucles)
18. [Slices: elegir fragmentos](#18-slices-elegir-fragmentos)
19. [Ejercicio completo de colores](#19-ejercicio-completo-de-colores)
20. [Listas multidimensionales](#20-listas-multidimensionales)
21. [Comprensiones de listas](#21-comprensiones-de-listas)
22. [Tuplas y operaciones compartidas](#22-tuplas-y-operaciones-compartidas)
23. [Conjuntos y operaciones de conjuntos](#23-conjuntos-y-operaciones-de-conjuntos)
24. [Diccionarios: registros con claves](#24-diccionarios-registros-con-claves)
25. [Funciones y objetos mutables](#25-funciones-y-objetos-mutables)
26. [Aplicaciones integradas a tus proyectos](#26-aplicaciones-integradas-a-tus-proyectos)
27. [Repaso, correcciones y fuentes](#27-repaso-correcciones-y-fuentes)

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

Una función con dos parámetros obligatorios necesita que se proporcionen ambos. Una llamada como `sumar()` o `sumar(7)` produce `TypeError`. Pasar más argumentos de los admitidos también puede producirlo; la excepción es cuando la función está definida para recibirlos, como veremos con `*valores`.

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

**Ahora también aparece en clase:** el ZIP actualizado incluye `args_defecto.py`. Esta forma ya no se trata solo como una ampliación opcional.

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

### 3.4. El nuevo ejemplo args_defecto.py

```python
def datos_trabajador(nombre, estado_civil="soltero", sueldo=21000):
    print(f"{nombre} esta {estado_civil} y gana {sueldo}")

datos_trabajador("Juan")
datos_trabajador("Maria", sueldo=25000)
datos_trabajador("Antonio", sueldo=30000)
datos_trabajador("Antonio", "casado", 30000)
```

| Llamada | nombre | estado_civil | sueldo |
|---|---|---|---|
| `datos_trabajador("Juan")` | Juan | soltero | 21000 |
| `datos_trabajador("Maria", sueldo=25000)` | Maria | soltero | 25000 |
| `datos_trabajador("Antonio", sueldo=30000)` | Antonio | soltero | 30000 |
| `datos_trabajador("Antonio", "casado", 30000)` | Antonio | casado | 30000 |

`nombre` es obligatorio; los otros dos parámetros tienen valores por defecto. Pasar `sueldo=25000` permite cambiar ese dato sin tener que pasar también el estado civil. En cambio, `datos_trabajador("Maria", 25000)` colocaría el número en `estado_civil`, porque ocupa la segunda posición.

**Aclaración al comentario del archivo:** «por kwargs» se refiere aquí a argumentos por nombre. La función no utiliza un parámetro `**kwargs` que recoja nombres arbitrarios. Solo acepta los parámetros declarados. No puedes pasar `edad=30` si no está previsto en su definición.

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

**Puente hacia las colecciones:** una lista puede modificarse a través de una referencia compartida. Eso es distinto de reasignar un parámetro a un número y se desarrolla en la sección 25. No generalices este ejemplo diciendo que «una función nunca puede cambiar un objeto recibido».

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

## 10. Funciones ampliadas: varios retornos, argumentos variables y medias

**Actualización:** las pp. 36–37 del PDF se desarrollan ahora también en `return_varios.py` y `numero_variable_args.py`. Este último incorpora un ejercicio de medias que combina parámetros obligatorios, argumentos variables, llamadas entre funciones y retorno de una tupla.

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

El archivo actualizado utiliza también el desempaquetado en una llamada, `sumar(*notas)`, que se explica a continuación. `**kwargs` y otras combinaciones avanzadas no son necesarios para estos ejemplos.

### 10.3. El nuevo return_varios.py: procesar un texto

```python
def procesar_texto(texto: str) -> tuple:
    return texto.upper(), texto.lower(), len(texto)

mayusculas, minusculas, longitud = procesar_texto("Hola, que tal?")
print(mayusculas)  # HOLA, QUE TAL?
print(minusculas)  # hola, que tal?
print(longitud)    # 14

resultado = procesar_texto("Hola, que tal?")
print(resultado[0])
print(resultado[1])
print(resultado[2])

for elemento in resultado:
    print(elemento)
```

La función devuelve una tupla de tres elementos: texto en mayúsculas, texto en minúsculas y longitud. Los espacios y signos también cuentan en `len`, por eso la longitud es catorce.

Hay dos formas de recoger exactamente la misma salida: desempaquetarla en tres nombres o guardarla en una variable y acceder por índices. El recorrido final visita los tres elementos completos, no las letras del texto original. La tupla puede contener elementos de tipos distintos: dos cadenas y un entero.

### 10.4. Asterisco en la definición y en la llamada

| Forma | Qué hace |
|---|---|
| `def sumar(*numeros):` | Recoge los argumentos posicionales en una tupla. |
| `sumar(*notas)` | Desempaqueta un iterable para entregar sus elementos como argumentos separados. |
| `sumar(notas)` | Entrega un único argumento: la tupla completa. No equivale al anterior. |

Si `notas` contiene `(6, 9)`, `sumar(*notas)` equivale a `sumar(6, 9)`. En la versión sumadora de clase, `sumar(notas)` intentaría sumar cero y una tupla, lo que produce `TypeError`.

### 10.5. Ejercicio nuevo: nombre y media de notas

Versión adaptada del archivo, quitando solo la impresión de diagnóstico de `sumar`:

```python
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

def calcular_media(nombre: str, *notas) -> tuple:
    if len(notas) > 0:
        nota_media = sumar(*notas) / len(notas)
    else:
        nota_media = 0
    return nombre.upper(), nota_media

print(calcular_media("Jorge"))
print(calcular_media("Jorge", 6))
print(calcular_media("Jorge", 6, 9))
print(calcular_media("Jorge", 6, 9, 7, 8, 5, 8))
```

| Llamada | Tupla notas | Resultado |
|---|---|---|
| Sin notas | `()` | `('JORGE', 0)` |
| Una nota | `(6,)` | `('JORGE', 6.0)` |
| Dos notas | `(6, 9)` | `('JORGE', 7.5)` |
| Seis notas | `(6, 9, 7, 8, 5, 8)` | `('JORGE', 7.166666666666667)` |

En la llamada con dos notas, `nombre` recibe `"Jorge"`, `notas` recibe `(6, 9)`, `sumar(*notas)` devuelve quince y `len(notas)` devuelve dos. Después se retorna la tupla con el nombre en mayúsculas y la media.

La rama sin notas evita dividir entre cero. **Devolver cero es la política del ejercicio**, no una media calculada de observaciones existentes. En una aplicación convendría distinguir «sin notas» y «media cero», por ejemplo mediante un resultado estructurado; se retoma en la sección 26.

En el original, `sumar` contiene `print(type(numeros))`. Por eso aparecen mensajes `<class 'tuple'>` además de los resultados. Esos mensajes los imprime la función; no son parte de la tupla que devuelve `calcular_media`.

**Matiz al enunciado:** en las firmas de este ejercicio, `*notas` va después del nombre obligatorio. Python admite parámetros posteriores que deben pasarse por nombre; decir que el asterisco «siempre tiene que ir al final» no es una regla general del lenguaje. No hace falta ampliar esas firmas para resolver este caso.

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

El comportamiento de `append`, índices y otras operaciones se desarrolla en las secciones 16–21, junto con tus apuntes de listas.

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
| Funciones que reciben listas o devuelven diccionarios | Ya se practica en las secciones 25–26 de este módulo. |
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

## 14. Mapa de funciones y conexión con colecciones

### 14.1. Qué aporta cada archivo del ZIP

| Archivo | Tema principal | Matiz relevante |
|---|---|---|
| `crear_funciones.py` | Definir y llamar; funciones con y sin resultado; parámetros y anotaciones. | `msg = despedir()` guarda sin imprimir. |
| `ejercicio1.py` | Composición de funciones y validación booleana. | Las anotaciones de las cuatro operaciones no coinciden con su retorno real. |
| `ejercicio2.py` | Cálculo reutilizable con dos parámetros y retorno numérico. | Expresar el porcentaje en la unidad esperada. |
| `ejercicio3.py` | Texto, bucle, contador y retorno. | `lower` no elimina tildes y el contador se devuelve al finalizar. |
| `ejercicio4.py` | Separación de entrada, cálculo y presentación. | `:.2f` es presentación; las unidades deben ser coherentes. |
| `args_defecto.py` | Valores por defecto y argumentos por nombre. | Argumentos por nombre no significa que se haya definido `**kwargs`. |
| `return_varios.py` | Tupla con mayúsculas, minúsculas y longitud. | Se puede desempaquetar o conservar la tupla. |
| `numero_variable_args.py` | `*numeros`, `*notas`, desempaquetado y media. | Distinguir notas vacías, retorno y mensajes de diagnóstico. |

### 14.2. Lo que añade la segunda parte

Las colecciones permiten recibir y devolver grupos de datos: listas de tareas, tuplas de resultados, conjuntos de identificadores o diccionarios que representan registros. Las funciones ya explicadas se reutilizan con esas estructuras. El mapa de todos los archivos y las fuentes está al final del documento.

## Parte II · Colecciones

## 15. Elegir una colección

Una colección agrupa datos. Elegir el tipo determina cómo accedemos a ellos, si conservan un orden y qué cambios permiten.

| Tipo | Ejemplo | Acceso | ¿Mutable? | Repeticiones |
|---|---|---|---|---|
| Lista, `list` | `["Vera", "Noa"]` | Índices y slices. | Sí. | Permite elementos repetidos. |
| Tupla, `tuple` | `("lunes", "martes")` | Índices y slices. | No se reasignan sus posiciones. | Permite elementos repetidos. |
| Conjunto, `set` | `{"a", "b"}` | Pertenencia y recorrido, sin índice. | Sí. | Conserva elementos únicos. |
| Diccionario, `dict` | `{"nombre": "Vera", "nota": 8}` | Claves. | Sí. | Claves únicas; valores repetidos permitidos. |

**Ordenada no significa ordenada alfabéticamente.** En una lista o tupla, los elementos tienen posiciones. Un diccionario conserva el orden de inserción de las claves en Python 3.7 y posteriores. Un conjunto no ofrece un orden de recorrido garantizado.

| Vacío que necesitas | Cómo crearlo |
|---|---|
| Lista | `[]` o `list()` |
| Tupla | `()` o `tuple()` |
| Conjunto | `set()` |
| Diccionario | `{}` o `dict()` |

`{}` crea un diccionario, no un conjunto vacío. En un literal de diccionario se separan claves y valores con `:`; las llaves de un conjunto contienen solo elementos.

### 15.1. Los textos no son listas

**Corrección de tus notas:** una cadena `str` es una secuencia de texto, no una lista. Comparte operaciones como `len`, índices, slices y recorridos, pero es inmutable y no tiene los mismos métodos.

```python
texto = "mesa"
letras = ["m", "e", "s", "a"]

print(texto[0])    # m
print(letras[0])   # m
print(texto[1:3])  # es

letras[0] = "p"
print(letras)      # ['p', 'e', 's', 'a']
print(texto)       # mesa
```

Puedes hacer `letras[0] = "p"`, pero no `texto[0] = "p"`. Para producir un texto distinto construyes otro. La similitud de algunas operaciones no convierte ambos tipos en el mismo.

## 16. Listas: crear, consultar y modificar

**Fuentes:** PDF, pp. 38–39, y `Ejemplo07_Listas/listas.py`. Una lista mantiene una secuencia de elementos, permite duplicados y puede modificarse. Sus elementos pueden ser de tipos distintos.

```python
datos = ["Maria", "Perez", 30, "soltera", "sin hijos"]
estudios = ["estudiante", "medicina", 28010]

primera = datos + estudios
segunda = estudios + datos

print(type(datos))      # <class 'list'>
print(len(datos))       # 5
print(segunda[2])       # 28010
print(segunda[-2])      # soltera
print(primera == segunda)  # False
```

`+` concatena y produce otra lista: el orden de los operandos importa. Para añadir mediante `+` una sola palabra necesitas una lista de un elemento, por ejemplo `datos + ["morena"]`; `datos + "morena"` no concatena una lista con texto.

### 16.1. Índices positivos y negativos

Con ocho elementos, los índices positivos van de cero a siete. `-1` designa el último y `-2` el penúltimo. `lista[len(lista) - 2]` y `lista[-2]` acceden al mismo elemento si existen al menos dos.

Un índice individual inexistente produce `IndexError`. Un slice que excede los límites, en cambio, se ajusta a lo disponible. La longitud es una cantidad, no el último índice.

### 16.2. Añadir: append, insert y extend

```python
colores = ["rojo", "verde"]
colores.append("azul")
colores.insert(0, "blanco")
colores.extend(["negro", "rosa"])

print(colores)
# ['blanco', 'rojo', 'verde', 'azul', 'negro', 'rosa']
```

| Operación | Efecto |
|---|---|
| `lista.append(valor)` | Añade un elemento al final. |
| `lista.insert(indice, valor)` | Inserta antes de la posición indicada. |
| `lista.extend(iterable)` | Añade los elementos del iterable, uno a uno. |

`append([1, 2])` añade una lista como un único elemento; `extend([1, 2])` añade dos enteros. `extend` no exige que el argumento sea una lista: también admite otros iterables. Si le pasas `"azul"`, añadirá sus cuatro letras. Es importante saber qué estructura quieres obtener.

Estos tres métodos modifican la lista y devuelven `None`; no guardes su retorno esperando obtener la lista modificada.

### 16.3. Borrar y sustituir

```python
nombres = ["Ana", "Luis", "Ana", "Noa"]
del nombres[-1]
nombres.remove("Ana")
nombres[0] = "Vera"
print(nombres)  # ['Vera', 'Ana']

nombres.clear()
print(nombres)  # []
```

| Operación | Qué selecciona | Matiz |
|---|---|---|
| `del lista[indice]` | Posición. | El índice debe existir. |
| `lista.remove(valor)` | Primer valor coincidente. | Si no existe, produce `ValueError`. |
| `lista[indice] = nuevo` | Posición existente. | Sustituye un elemento. |
| `lista.clear()` | Todos los elementos. | Deja la misma lista vacía. |

`remove` necesita el valor que quieres eliminar: `lista.remove()` no cumple la firma. `del` es una instrucción, no un método exclusivo de listas; en diccionarios se utiliza con una clave.

**Complemento breve:** `lista.pop()` elimina y devuelve el último elemento; `lista.pop(indice)` hace lo mismo con una posición. A diferencia de `remove`, aquí recibes el elemento retirado. Se necesita una posición válida en una lista no vacía.

### 16.4. Encontrar y contar

```python
asignaturas = ["medicina", "python", "medicina", "datos"]
print(asignaturas.index("medicina"))     # 0
print(asignaturas.index("medicina", 1))  # 2
print(asignaturas.count("medicina"))     # 2
print(asignaturas.count("arte"))         # 0

if "arte" in asignaturas:
    print(asignaturas.index("arte"))
else:
    print("No está en la lista")
```

`index(valor, inicio)` busca desde ese índice incluido y devuelve una posición referida a la lista completa. Si no encuentra el valor, produce `ValueError`. `count`, en cambio, devuelve cero si no lo encuentra.

`in` y `not in` permiten comprobar presencia o ausencia antes de una operación. No indican el índice ni cuántas veces aparece el dato.

### 16.5. Ordenar: sort frente a sorted

```python
colores = ["rojo", "azul", "verde"]
ordenados = sorted(colores)
print(ordenados)  # ['azul', 'rojo', 'verde']
print(colores)    # ['rojo', 'azul', 'verde']

retorno = colores.sort(reverse=True)
print(colores)    # ['verde', 'rojo', 'azul']
print(retorno)    # None
```

`sort` modifica la lista; `sorted` crea una lista nueva a partir de un iterable. `reverse=True` pide orden descendente. En tus notas aparece `reverse:True`; en una llamada se escribe con **igual**, `reverse=True`.

**Matiz:** tener tipos distintos no impide siempre ordenar: enteros y decimales reales pueden compararse entre sí. Mezclar textos y números normalmente no tiene un orden definido en Python y produce `TypeError`. Para texto, el orden por defecto distingue mayúsculas, minúsculas y caracteres acentuados; no aplica automáticamente las reglas de ordenación de un diccionario español.

## 17. Recorridos y else en bucles

Las listas pueden recorrerse por elemento o por índice. Elige el índice cuando necesites la posición; si solo necesitas cada valor, el recorrido directo es más sencillo.

```python
colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color, end=" ")
print()

for indice in range(len(colores)):
    print(colores[indice], end=" ")
print()

indice = 0
while indice < len(colores):
    print(colores[indice], end=" ")
    indice += 1
print()
```

Cada recorrido muestra los tres colores. Si en el segundo escribes `print(indice)`, obtendrás cero, uno y dos: eso ocurre en tu `ejercicio3-1.py`, aunque la variable de índice se llame `color`.

`print(color, sep=" - ")` recibe un solo argumento y no tiene dos valores entre los que insertar ese separador. Para separar llamadas sucesivas usa `end=" - "`; se añadirá también después del último elemento. Para cambiar la separación dentro de una misma llamada con varios argumentos sí sirve `sep`.

### 17.1. Qué significa else después de for o while

La cláusula `else` pertenece al bucle cuando está alineada con su encabezado. Se ejecuta si el `for` agota su iterable o si el `while` termina porque su condición es falsa, **sin ejecutar un `break` que salga de ese bucle**.

No es obligatoria. Si solo quieres escribir una línea después de cualquier finalización normal del recorrido, puede bastar un `print()` fuera.

```python
buscado = "azul"
colores = ["rojo", "verde", "azul"]

for color in colores:
    if color == buscado:
        print("Encontrado")
        break
else:
    print("No encontrado")
```

Con `"azul"`, se imprime «Encontrado» y no se ejecuta el `else`. Con `"negro"`, se agotaría la lista y se imprimiría «No encontrado». Con una lista vacía también se ejecutaría el `else`: no hubo un `break`.

En un bucle anidado, cada `else` corresponde a su propio bucle según la indentación. La explicación «se ejecuta cuando ya no hay elementos» es útil para el recorrido habitual, pero incompleta si omitimos el efecto de `break`. Un `return` o una excepción también pueden interrumpir la ejecución antes de llegar al `else`.

## 18. Slices: elegir fragmentos

Un slice extrae una parte de una secuencia:

`secuencia[inicio:fin:paso]`

El inicio se incluye y el fin se excluye. Por defecto, el paso es uno. Si faltan los extremos, Python elige los adecuados al sentido del paso. Un paso cero no es válido.

**Corrección de sintaxis:** no se escribe `slice(inicio:stop:step)` en estos ejemplos. La notación utilizada es la de corchetes después de la secuencia.

### 18.1. Una secuencia estable para practicar

Los resultados de esta tabla usan exactamente doce letras, de la a a la l:

```python
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"]

print(letras[3:7])    # ['d', 'e', 'f', 'g']
print(letras[6:2:-1]) # ['g', 'f', 'e', 'd']
print(letras[::-1])   # Todas al revés.
```

| Slice | Resultado con esa lista |
|---|---|
| `letras[:]` | Todos los elementos, en una lista nueva. |
| `letras[-4:]` | i, j, k, l. |
| `letras[:5]` | a, b, c, d, e. |
| `letras[3:7]` | d, e, f, g. |
| `letras[6:2]` | Lista vacía: paso positivo hacia un fin situado antes. |
| `letras[6:2:-1]` | g, f, e, d. |
| `letras[-6:-10:-1]` | g, f, e, d. |
| `letras[::-1]` | l, k, j, i, h, g, f, e, d, c, b, a. |
| `letras[::-2]` | l, j, h, f, d, b. |
| `letras[::2]` | a, c, e, g, i, k. |
| `letras[-2:]` | k, l. |
| `letras[-1:-4:-1]` | l, k, j. |
| `letras[:-1:2]` | a, c, e, g, i, k. |

Un índice negativo se interpreta con respecto a la longitud actual. No significa un número fijo desde el principio. Los slices devuelven los elementos según su posición, no según su valor.

### 18.2. La equivalencia de índices negativos depende de la longitud

En tus notas y en `listas.py` aparecen `lista[-6:-10:-1]` y `lista[-6:2:-1]` como si fueran siempre equivalentes. Lo serían para una lista de longitud doce, porque `-10` se corresponde con el índice dos.

Sin embargo, la lista de `listas.py` tiene **once elementos** en ese momento. Allí `-10` se corresponde con el índice uno y los dos slices son distintos:

| Slice en ese estado del archivo | Valores |
|---|---|
| `lista[-6:-10:-1]` | `['Perez', 'Maria', 28010, 'medicina']` |
| `lista[-6:2:-1]` | `['Perez', 'Maria', 28010]` |

No memorices equivalencias sin revisar primero la longitud. También recuerda que `-1` como fin de un slice es el índice del último elemento, no una instrucción para «incluir el último al bajar». Para invertir toda la secuencia, `[::-1]` evita ese problema.

## 19. Ejercicio completo de colores

**Fuente:** `Ejemplo07_Listas/ejercicio.py`, relacionado con tu `ejercicio3-1.py`. Se construye y modifica una lista; el resultado de cada consulta depende de las operaciones anteriores.

```python
colores = ["rojo", "verde", "azul"]
print(type(colores))
print(colores)

for color in colores:
    print(color, end=" ")
print()

for indice in range(len(colores)):
    print(colores[indice], end=" ")
print()

indice = 0
while indice < len(colores):
    print(colores[indice], end=" ")
    indice += 1
print()

print(colores[1])
del colores[2]
mas_colores = colores + ["blanco", "negro", "rosa", "azul"]
mas_colores.append("naranja")
mas_colores.insert(0, "marron")
print(len(mas_colores))
print(mas_colores[-3])

mas_colores.sort()
print(mas_colores)
mas_colores.sort(reverse=True)
print(mas_colores)

print(mas_colores[-2:])
print(mas_colores[-1:-4:-1])
print(mas_colores[:3])
print(mas_colores[1:4])
print(mas_colores[:-1:2])

mas_colores.clear()
print(mas_colores)
```

### 19.1. Seguir el estado

| Momento | Contenido relevante |
|---|---|
| Lista inicial | `['rojo', 'verde', 'azul']` |
| Después de borrar azul | `['rojo', 'verde']` |
| Después de unir cuatro colores | `['rojo', 'verde', 'blanco', 'negro', 'rosa', 'azul']` |
| Después de append e insert | `['marron', 'rojo', 'verde', 'blanco', 'negro', 'rosa', 'azul', 'naranja']` |
| Longitud | 8. |
| Antepenúltimo antes de ordenar | rosa. |
| Orden ascendente | `['azul', 'blanco', 'marron', 'naranja', 'negro', 'rojo', 'rosa', 'verde']` |
| Orden descendente | `['verde', 'rosa', 'rojo', 'negro', 'naranja', 'marron', 'blanco', 'azul']` |

Los slices del archivo de la profesora se hacen **después de ordenar en descendente**:

| Consulta | Resultado |
|---|---|
| Dos últimos | `['blanco', 'azul']` |
| Del último al antepenúltimo | `['azul', 'blanco', 'marron']` |
| Tres primeros | `['verde', 'rosa', 'rojo']` |
| Del segundo al cuarto | `['rosa', 'rojo', 'negro']` |
| Del primero al penúltimo, de dos en dos | `['verde', 'rojo', 'naranja', 'blanco']` |
| Después de clear | `[]` |

### 19.2. Diferencias en tu ejercicio

Tu versión añade `"maranja"`, con una errata, y solo ordena en ascendente antes de los slices. También consulta el antepenúltimo después de ordenar, mientras la profesora lo hace antes. Por tanto, algunas salidas serán distintas aunque la notación de los slices sea correcta.

Además, el recorrido con `range` imprime la variable que contiene el índice: muestra números, no colores. La forma corregida utiliza `colores[indice]`. Tus originales se conservan para que puedas comparar estas diferencias.

## 20. Listas multidimensionales

**Fuentes:** p. 40 del PDF y `listas_multidimensionales.py`. Una lista puede contener otras listas. Una matriz sencilla se representa como una lista de filas.

```python
matriz = [[2, 7, 4], [8, 1, 6], [3, 9, 5]]

print(matriz[0])     # [2, 7, 4]
print(matriz[0][2])  # 4
print(matriz[2][1])  # 9
print(matriz[1][0])  # 8

for fila in matriz:
    for numero in fila:
        print(numero, end="\t")
    print()

for indice_fila in range(len(matriz)):
    for indice_columna in range(len(matriz[indice_fila])):
        print(matriz[indice_fila][indice_columna], end="\t")
    print()
```

El primer índice selecciona la fila y el segundo un elemento de esa fila. La tabla representa los mismos datos:

| Fila / columna | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 2 | 7 | 4 |
| 1 | 8 | 1 | 6 |
| 2 | 3 | 9 | 5 |

La versión por valores necesita dos recorridos para visitar cada número; la de índices utiliza el tamaño de cada fila. Python también permite listas anidadas cuyas filas tienen tamaños distintos: no garantiza una matriz rectangular.

**Corrección de tus notas:** se escribe `matriz[indice_fila]`, no `matriz(indice_fila)`. Los corchetes acceden a un elemento; los paréntesis intentan llamar a un objeto como función.

En la p. 40 del PDF también hay una lista que mezcla textos y una sublista. No hace falta que todos los elementos tengan la misma profundidad. Por ejemplo, `equipos[3][1]` primero selecciona la sublista en el índice tres y luego su segundo elemento. Esto es una lista anidada, aunque no forme una tabla rectangular.

## 21. Comprensiones de listas

**Fuente:** `compresion_listas.py`. El nombre habitual es **comprensión de listas**. Es una forma de construir una lista mediante un recorrido y, opcionalmente, un filtro.

### 21.1. Transformar cada elemento

```python
palabras = ["casa", "mesa", "manzana", "pijama"]
longitudes = []

for palabra in palabras:
    longitudes.append(len(palabra))

por_comprension = [len(palabra) for palabra in palabras]
print(longitudes)       # [4, 4, 7, 6]
print(por_comprension)  # [4, 4, 7, 6]
```

En `[len(palabra) for palabra in palabras]`, lee primero el recorrido: «por cada palabra de palabras»; después la expresión de la izquierda: «guarda su longitud».

La lista de entrada no se modifica. Se construye otra con los resultados de la expresión.

### 21.2. Filtrar elementos

```python
pares = []
for numero in range(0, 21):
    if numero % 2 == 0:
        pares.append(numero)

por_comprension = [numero for numero in range(0, 21) if numero % 2 == 0]
print(pares)
print(por_comprension)
# Ambas: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

El `if` al final filtra qué elementos se incorporan. Si un elemento no cumple, no se añade nada por él. La longitud de la salida puede ser menor que la del recorrido.

**Correcciones de tus notas:** se llama a `range(0, 21)` con paréntesis, no con corchetes; las variables no pueden contener espacios; en la versión larga, el `if` necesita `:` y su bloque. La comprensión no lleva esos dos puntos.

Usa esta forma cuando la transformación sea breve y legible. Si necesitas varios pasos, diagnósticos o condiciones difíciles de leer, el bucle explícito sigue siendo una buena solución.

## 22. Tuplas y operaciones compartidas

**Fuentes:** p. 41 del PDF y `Ejemplo08_Tuplas/tuplas.py`. Una tupla es una secuencia ordenada que permite duplicados. No podemos reasignar, añadir o borrar sus posiciones como hacemos con una lista.

```python
dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")

print(type(dias))             # <class 'tuple'>
print(dias[0])                # lunes
print(len(dias))              # 7
print(dias.count("lunes"))    # 1
print(dias.index("viernes"))  # 4
print(dias.index("viernes", 2))  # 4
print(dias[:5])               # Los cinco días laborables.
print(dias[::-1])             # Los siete días al revés.
```

`dias.index("viernes", 5)` no encontraría la palabra desde ese punto y produciría `ValueError`. Como en listas, `count` cuenta apariciones e `index` busca una posición. Los slices funcionan igual, pero devuelven tuplas.

No existen operaciones válidas como `dias.append(...)`, `del dias[0]` o `dias[0] = ...`: o falta el método o se intenta modificar una posición inmutable.

### 22.1. Una tupla de un elemento necesita una coma

```python
texto = ("otro_sabado")
un_elemento = ("otro_sabado",)
print(type(texto))        # <class 'str'>
print(type(un_elemento))  # <class 'tuple'>

numeros = 1, 2, 3
print(type(numeros))      # <class 'tuple'>
```

Los paréntesis por sí solos también sirven para agrupar expresiones. La coma es la que forma la tupla no vacía en estos casos. No estamos «engañando al intérprete», como dice el comentario de clase: estamos usando la sintaxis prevista.

### 22.2. Concatenar, convertir y repetir

```python
dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
otra_tupla = dias + ("otro_sabado",)
print(otra_tupla)

con_repeticiones = dias + tuple(["sabado", "domingo"])
como_lista = list(con_repeticiones)
print(como_lista)

numeros = (1, 2, 3, 4, 5)
print(numeros * 2)
# (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print("-" * 5)  # -----
```

`+` crea otra tupla; no modifica las posiciones de la original. `* 2` repite la secuencia, no multiplica por dos cada número. El ejemplo del separador usa la misma idea con una cadena.

Convertir una tupla en lista permite operar sobre la lista creada, pero no cambia el tipo del objeto original. Si concatenas tuplas, el orden de los operandos también importa.

### 22.3. Funciones incorporadas sobre colecciones

```python
numeros = (1, 2, 3, 4, 5)
print(len(numeros))                  # 5
print(min(numeros))                  # 1
print(max(numeros))                  # 5
print(sum(numeros))                  # 15
print(sorted(numeros, reverse=True)) # [5, 4, 3, 2, 1]
print(numeros)                       # La tupla no ha cambiado.
```

Estas funciones no son métodos exclusivos de tuplas. Pueden recibir distintos iterables, siempre que sus elementos tengan sentido para la operación. `sorted` devuelve una lista aunque reciba una tupla o un conjunto; `sum` necesita datos que se puedan sumar; `min` y `max` necesitan comparaciones válidas y, en su forma sencilla, al menos un elemento.

**Matiz al comentario «funciones universales»:** no significa que cualquier operación sirva con cualquier contenido. `sum(["a", "b"])` no concatena esas cadenas. En un diccionario, el recorrido predeterminado proporciona claves; para sumar notas habrá que pasar sus valores.

Una tupla con un objeto mutable dentro puede contener cambios de ese objeto. Su inmutabilidad impide sustituir la posición de la tupla, no congela recursivamente todo lo que haya dentro. Se retoma la idea al hablar de referencias.

## 23. Conjuntos y operaciones de conjuntos

**Fuentes:** p. 42 del PDF y los dos archivos del ZIP 09. Un conjunto agrupa elementos únicos y sirve especialmente para comprobar pertenencia o comparar grupos.

```python
frutas = {"manzana", "naranja", "pera", "naranja", "platano"}
print(len(frutas))  # 4: naranja no se conserva dos veces.

vacio = set()
print(type(vacio))  # <class 'set'>
print(type({}))     # <class 'dict'>

frutas.add("fresas")
frutas.remove("platano")
print(len(frutas))  # 4

otro = frutas.copy()
resultado = frutas.union({"melon", "sandia"})
print(sorted(resultado))
print("fresas" in frutas)       # True
print("maracuya" in frutas)     # False
print("melocoton" not in frutas)  # True

for fruta in sorted(resultado):
    print(fruta, end=" ")
print()

como_tupla = tuple(resultado)
como_lista = list(resultado)
frutas.clear()
print(frutas)  # set()
print(len(otro))  # 4: la copia conserva sus elementos.
```

`sorted` se usa aquí para presentar un orden predecible, no porque el conjunto adquiera posiciones. El archivo original recorre el conjunto directamente: el orden que veas puede variar. Convertirlo con `list` o `tuple` tampoco garantiza recuperar el orden de inserción.

### 23.1. Qué cambia respecto a una lista

- No se accede por `frutas[0]` ni mediante slices.
- `add` incorpora un elemento; si ya está, no crea un duplicado.
- `remove` quita un elemento por su valor y produce `KeyError` si falta.
- **Complemento:** `discard(valor)` también quita un elemento, pero no falla si ya está ausente.
- No se utiliza `+` para unir conjuntos; se usa `union` o `|`.
- `clear` vacía el conjunto y `copy` crea una copia independiente de su contenedor.

Los conjuntos son mutables, pero no se «modifica el elemento de una posición». Para cambiar un valor se elimina uno y se añade otro.

**Restricción importante:** los elementos deben ser hashables, es decir, admitir el mecanismo que Python utiliza para identificarlos en esta estructura. Para este módulo basta recordar que números, textos y tuplas de elementos hashables sirven; listas, diccionarios y conjuntos mutables no pueden ser elementos de un conjunto. Por tanto, el comentario «pueden contener cualquier tipo» necesita ese matiz.

### 23.2. Intersección, diferencia, unión y diferencia simétrica

El archivo `operaciones_conjuntos.py` compara estos dos conjuntos:

```python
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {0, 2, 4, 6, 8, 10}

print(sorted(a.intersection(b)))         # [2, 4, 6, 8]
print(sorted(a & b))                     # Lo mismo.
print(sorted(a.difference(b)))           # [1, 3, 5, 7, 9]
print(sorted(a - b))                     # Lo mismo.
print(sorted(b - a))                     # [0, 10]
print(sorted(a.union(b)))                # [0, 1, ..., 10]
print(sorted(a | b))                     # Lo mismo.
print(sorted(a.symmetric_difference(b))) # [0, 1, 3, 5, 7, 9, 10]
print(sorted(a ^ b))                     # Lo mismo.
```

| Operación | Significado | ¿Importa invertir los operandos? |
|---|---|---|
| `a & b` | Elementos comunes. | No para el resultado de esta operación. |
| `a - b` | Elementos de a que no están en b. | Sí. |
| `a \| b` | Todos los elementos, sin duplicados. | No para el contenido. |
| `a ^ b` | Elementos presentes solo en uno de los dos. | No para el contenido. |

Los métodos utilizados aquí devuelven otros conjuntos y no vacían ni reescriben `a` o `b`. En tus proyectos, la diferencia permite localizar identificadores pendientes; la intersección permite comprobar coincidencias entre dos fuentes.

## 24. Diccionarios: registros con claves

**Fuentes:** p. 43 del PDF y `Ejemplo10_Diccionarios/diccionarios.py`. Un diccionario relaciona claves con valores. La clave describe cómo encontrar el dato: por ejemplo, el nombre de un alumno o el campo `"nota"` de un registro.

```python
alumnos = {"Juan": 6.4, "Maria": 8.3, "Luis": 6.4, "Adolfo": 7.1, "Maria": 9.3}
print(type(alumnos))     # <class 'dict'>
print(len(alumnos))      # 4, no 5.
print(alumnos["Maria"])  # 9.3: prevalece el último valor escrito.
print(alumnos["Luis"])   # 6.4

print(alumnos.keys())
print(alumnos.values())
print(alumnos.items())
```

Las claves no coexisten repetidas: la segunda entrada de `"Maria"` sustituye su valor. Juan y Luis sí pueden tener la misma nota. Sustituir el valor de una clave existente no la mueve al final del orden de inserción.

| Consulta | Qué proporciona |
|---|---|
| `alumnos.keys()` | Vista de las claves: Juan, Maria, Luis y Adolfo. |
| `alumnos.values()` | Vista de los valores: 6.4, 9.3, 6.4 y 7.1. |
| `alumnos.items()` | Vista de las parejas clave–valor. Cada pareja se recorre como una tupla. |

Estas vistas no son listas independientes. Si necesitas una lista, puedes construirla, por ejemplo, con `list(alumnos.keys())`. Los cambios del diccionario se reflejan en sus vistas.

**Matiz de acceso:** `alumnos[0]` buscaría la clave numérica cero; no significa «primer alumno». Un diccionario puede tener claves enteras, pero esas claves no son posiciones. Las claves deben ser hashables, como los elementos de un conjunto; sus valores sí pueden ser listas, diccionarios u otros objetos.

### 24.1. Acceso directo y get

```python
alumnos = {"Juan": 6.4, "Maria": 9.3, "Luis": 6.4}

print(alumnos["Luis"])                 # 6.4
print(alumnos.get("Luis"))            # 6.4
print(alumnos.get("Luissssss"))       # None
print(alumnos.get("Luissssss", "No registrado"))  # No registrado

if "Luis" in alumnos:
    print("Existe esa clave")
```

El acceso con una clave ausente entre corchetes produce `KeyError`. `get` devuelve `None` si falta, o el valor por defecto que indiques. Este segundo argumento es un complemento práctico a la versión de clase.

`in` comprueba **claves**, no valores. Para buscar una nota entre los valores podrías comprobar `6.4 in alumnos.values()`.

En datos reales, `None` también puede ser un valor existente. Si necesitas distinguir una clave ausente de una clave cuyo valor es `None`, comprueba la pertenencia de la clave.

### 24.2. Añadir, modificar, borrar y recuperar el último par

```python
alumnos = {"Juan": 6.4, "Maria": 9.3, "Luis": 6.4, "Adolfo": 7.1}
del alumnos["Adolfo"]

alumnos["Pepito"] = 3.5
alumnos["Pepito"] = 5
retirado = alumnos.popitem()
print(retirado)  # ('Pepito', 5)

alumnos.update({"Pepito": 5})
print(alumnos)
# {'Juan': 6.4, 'Maria': 9.3, 'Luis': 6.4, 'Pepito': 5}
```

La misma sintaxis `diccionario[clave] = valor` añade si la clave falta y modifica si ya existe. `update` incorpora varias parejas y sustituye los valores de las claves coincidentes; modifica el diccionario y devuelve `None`.

En Python actual, `popitem` elimina y devuelve la pareja insertada más recientemente. No elimina necesariamente el valor mayor ni la clave que modificaste más recientemente. Si está vacío, produce `KeyError`.

`del diccionario[clave]` elimina por clave; si falta, también produce `KeyError`. `clear()` elimina todas las parejas y deja `{}`.

### 24.3. Ordenar una presentación no ordena el objeto original

```python
alumnos = {"Juan": 6.4, "Maria": 9.3, "Luis": 6.4, "Pepito": 5}

print(sorted(alumnos))               # ['Juan', 'Luis', 'Maria', 'Pepito']
print(sorted(alumnos, reverse=True)) # ['Pepito', 'Maria', 'Luis', 'Juan']
print(sorted(alumnos.values()))      # [5, 6.4, 6.4, 9.3]
print(list(alumnos))                 # ['Juan', 'Maria', 'Luis', 'Pepito']

for nombre in sorted(alumnos):
    print(nombre, alumnos[nombre])
```

El comentario de clase dice «ordenar el diccionario», pero esas llamadas a `sorted` devuelven **listas**. El diccionario conserva su orden de inserción.

Ordenar solo los valores produce una lista de notas y no conserva por sí sola qué alumno corresponde a cada una. Para una presentación por nombre, el último recorrido conserva la relación porque sigue consultando cada clave en el diccionario.

### 24.4. Tres recorridos equivalentes en lo que muestran

```python
alumnos = {"Juan": 6.4, "Maria": 9.3, "Luis": 6.4}

for nombre in alumnos:
    print(nombre, alumnos[nombre])

for pareja in alumnos.items():
    print(pareja[0], pareja[1])

for nombre, nota in alumnos.items():
    print(nombre, nota)
```

El primero recorre claves. El segundo recibe cada tupla y la indexa. El tercero desempaqueta la pareja en dos variables, igual que desempaquetábamos los resultados de una función.

### 24.5. Otras formas de crearlos

```python
por_nombres = dict(Juan=6.4, Maria=8.3, Luis=6.4, Adolfo=7.1)
por_parejas = dict([("Juan", 6.4), ("Maria", 9.3), ("Luis", 6.4), ("Pepito", 5)])

print(por_nombres["Maria"])  # 8.3
print(por_parejas["Maria"])  # 9.3

por_nombres.clear()
print(por_nombres)           # {}
```

La primera forma usa argumentos por nombre y crea claves de texto. No puedes repetir un mismo argumento por nombre en esa llamada. La segunda construye el diccionario a partir de parejas; permite utilizar claves que no serían nombres válidos de parámetros.

La guía llama «corchetes» a `{}`: para distinguir la notación, aquí hablamos de **llaves** para conjuntos y diccionarios, **corchetes** para listas e índices y **paréntesis** para llamadas y agrupaciones.

## 25. Funciones y objetos mutables

Esta parte une las funciones con las colecciones. No es necesario modificar una variable global para que dos nombres permitan ver cambios en el mismo objeto.

### 25.1. Compartir una lista no equivale a copiarla

```python
original = ["Vera", "Noa"]
alias = original
copia = original.copy()

alias.append("Laura")
print(original)  # ['Vera', 'Noa', 'Laura']
print(alias)     # ['Vera', 'Noa', 'Laura']
print(copia)     # ['Vera', 'Noa']
```

La asignación `alias = original` no crea otra lista. Los dos nombres hacen referencia a la misma. `copy()` y el slice `[:]` crean otra lista superficial: un contenedor distinto con referencias a los mismos elementos.

### 25.2. Modificar el objeto recibido o devolver otra lista

```python
def anadir_en_la_misma(lista, elemento) -> None:
    lista.append(elemento)

def crear_con_elemento(lista, elemento) -> list:
    nueva = lista.copy()
    nueva.append(elemento)
    return nueva

tareas = ["leer"]
anadir_en_la_misma(tareas, "revisar")
otras_tareas = crear_con_elemento(tareas, "archivar")

print(tareas)        # ['leer', 'revisar']
print(otras_tareas)  # ['leer', 'revisar', 'archivar']
```

La primera modifica la lista recibida y devuelve `None`. La segunda crea otra y la devuelve. Ambas pueden ser correctas, pero el comportamiento debe quedar claro para quien utilice la función.

### 25.3. Las copias superficiales comparten elementos anidados

```python
matriz = [[1, 2], [3, 4]]
superficial = matriz.copy()
por_filas = [fila[:] for fila in matriz]

superficial[0][0] = 99
print(matriz)    # [[99, 2], [3, 4]]
print(por_filas) # [[1, 2], [3, 4]]
```

La copia superficial comparte las filas. En este ejemplo, copiar también cada fila separa las listas de esos dos niveles. No es una copia profunda universal para cualquier estructura: si dentro de cada fila hubiera otros objetos mutables, habría que considerar esos niveles también.

### 25.4. Precaución con listas como valor por defecto

**Complemento práctico para reutilizar funciones.** Un valor por defecto se prepara al ejecutar la definición, no de nuevo en cada llamada. Un parámetro definido como `tareas=[]` puede compartir esa lista entre llamadas.

Una forma de crear una lista nueva cuando el usuario no proporciona ninguna es:

```python
def anadir_tarea(tarea, tareas=None):
    if tareas is None:
        tareas = []
    tareas.append(tarea)
    return tareas

print(anadir_tarea("leer"))    # ['leer']
print(anadir_tarea("revisar")) # ['revisar']
```

`is None` comprueba si ese valor es precisamente `None`. Si pasas explícitamente una lista, esta función la modifica. El objetivo del ejemplo es evitar compartir por accidente una lista por defecto, no prometer que nunca modificará datos recibidos.

## 26. Aplicaciones integradas a tus proyectos

**Complementos opcionales con datos ficticios.** Reutilizan las estructuras del módulo sin conectar APIs, enviar mensajes ni guardar archivos.

### 26.1. Devolver un registro que distingue ausencia de datos y resultado cero

La media de clase devolvía cero cuando no había notas. Para un sistema de seguimiento o una evaluación puede interesar distinguir los dos casos:

```python
def resumir_notas(nombre: str, *notas) -> dict:
    if len(notas) == 0:
        return {"nombre": nombre.upper(), "cantidad": 0, "media": None}

    total = 0
    for nota in notas:
        total += nota

    return {
        "nombre": nombre.upper(),
        "cantidad": len(notas),
        "media": total / len(notas),
    }

sin_datos = resumir_notas("Jorge")
con_cero = resumir_notas("Jorge", 0)
con_notas = resumir_notas("Jorge", 6, 9)

print(sin_datos["media"])  # None
print(con_cero["media"])   # 0.0
print(con_notas["media"])  # 7.5
```

Los campos nombrados facilitan interpretar la salida sin memorizar que «la posición uno es la media». Se presuponen notas numéricas válidas. Un diccionario de Python no es todavía un texto JSON: la serialización se estudiará en el puente de integraciones.

### 26.2. Preparar un lote editorial con listas, conjuntos y diccionarios

```python
def preparar_lote(documentos: list, ids_ya_procesados: set) -> list:
    pendientes = []
    vistos = ids_ya_procesados.copy()

    for documento in documentos:
        identificador = documento["id"]
        if identificador in vistos:
            continue
        if documento["texto"] == "":
            continue
        pendientes.append(documento.copy())
        vistos.add(identificador)

    return pendientes

documentos = [
    {"id": "A", "texto": "Texto ya revisado"},
    {"id": "B", "texto": "Entrevista pendiente"},
    {"id": "B", "texto": "Otra entrada con el mismo identificador"},
    {"id": "C", "texto": ""},
]
procesados = {"A"}
lote = preparar_lote(documentos, procesados)

print(lote)        # [{'id': 'B', 'texto': 'Entrevista pendiente'}]
print(procesados)  # {'A'}: el conjunto recibido no se ha modificado.
```

La lista conserva el orden de entrada; los diccionarios identifican los campos de cada documento; el conjunto permite excluir identificadores repetidos. La copia del conjunto evita modificar el historial recibido.

El identificador B se incorpora una sola vez, también si está duplicado dentro de la misma tanda. El C se descarta porque su texto está vacío. La función presupone que existen `id` y `texto` y que sus tipos son los esperados. El texto formado solo por espacios no se considera vacío en esta regla; la limpieza detallada se añadirá con métodos de texto.

Esto prepara datos en memoria. Evitar duplicados en una operación real y persistente exige más controles, que se estudiarán con idempotencia, bases de datos y errores de integración.

### 26.3. Comparar resultados entre versiones

```python
antes = {"documento_1", "documento_2", "documento_3"}
despues = {"documento_2", "documento_3", "documento_4"}

print("Se mantienen:", sorted(antes & despues))
print("Desaparecen:", sorted(antes - despues))
print("Se añaden:", sorted(despues - antes))
```

Es una forma sencilla de revisar si un cambio en un pipeline pierde o incorpora registros. La comparación de identificadores no demuestra que su contenido sea correcto, pero sí permite detectar diferencias concretas para investigarlas.

Para tus automatizaciones, refuerza especialmente **listas de diccionarios, acceso a campos, pertenencia mediante conjuntos y funciones con entradas y salidas claras**. Serán bases directas para interpretar respuestas de servicios y trabajar con lotes.

## 27. Repaso, correcciones y fuentes

### 27.1. Ruta rápida para repasar el módulo

| Si necesitas recordar… | Ve a… |
|---|---|
| Qué imprime una función y qué devuelve | Sección 4. |
| Valores por defecto y argumentos por nombre | Secciones 3.3–3.4. |
| `*notas` en definición y llamada | Secciones 10.4–10.5. |
| Qué colección elegir | Sección 15. |
| Añadir, borrar, buscar y ordenar una lista | Sección 16. |
| Por qué aparece `else` después de un bucle | Sección 17.1. |
| Elegir índices y dirección de un slice | Sección 18. |
| Seguir el ejercicio de colores paso a paso | Sección 19. |
| Dos índices y dos recorridos | Sección 20. |
| Transformar o filtrar con una comprensión | Sección 21. |
| Coma de tupla, conversión y funciones incorporadas | Sección 22. |
| Elementos únicos y comparación de grupos | Sección 23. |
| Claves, `get`, `items` y actualizaciones | Sección 24. |
| Si se modifica el original o una copia | Sección 25. |

La ruta resume el material aportado, no predice preguntas del examen. Las aplicaciones a tu ámbito son complementos separados de los ejemplos de clase.

### 27.2. Correcciones que conviene conservar como aprendizaje

| Idea o detalle encontrado | Explicación correcta |
|---|---|
| Los textos son listas. | Son secuencias `str` inmutables; comparten algunas operaciones. |
| `len` es una propiedad de la colección. | En estos ejemplos es una función que se llama como `len(objeto)`. |
| `reverse:True` en la llamada. | Se escribe `reverse=True`. |
| Todas las mezclas de tipos impiden ordenar. | Depende de si sus elementos se pueden comparar; enteros y decimales reales sí son comparables. |
| `sep` separa las vueltas del bucle. | Separa argumentos de una llamada; `end` controla su final. |
| `else` del bucle se ejecuta siempre al terminar. | No se ejecuta si se sale de ese bucle con `break`; también puede haber otras interrupciones. |
| Dos slices con extremos negativos son siempre equivalentes. | Depende de la longitud actual. En `listas.py`, los dos ejemplos citados no coinciden. |
| `matriz(indice_fila)` accede a una fila. | Se necesita `matriz[indice_fila]`. |
| La coma de una tupla «engaña» al intérprete. | Es parte de la sintaxis que construye esa tupla. |
| `*args` recoge una lista. | Recoge una tupla de argumentos posicionales. |
| Los conjuntos admiten elementos de cualquier tipo. | Los elementos deben ser hashables. |
| `del` solo sirve para borrar índices. | También elimina entradas de diccionario por clave y tiene otros usos. |
| `sorted(alumnos)` ordena el diccionario. | Devuelve una lista de claves; no cambia el objeto original. |
| Copiar una lista copia profundamente sus elementos. | Las copias usadas aquí son superficiales. |
| Cualquier salida de una función coincide con su anotación. | Las anotaciones no validan el retorno en ejecución. |

Estas aclaraciones no implican que todos los ejemplos estén mal. Distinguen la operación real de comentarios simplificados o de apuntes tomados con rapidez.

### 27.3. Inventario de todos los ejemplos del módulo

Se han revisado los **16 archivos Python** de los ZIP 06–10. Cada archivo tiene desarrollo o explicación de sus operaciones en las secciones indicadas.

| ZIP | Archivo | Dónde se desarrolla |
|---|---|---|
| 06 | `crear_funciones.py` | Secciones 1–5. |
| 06 | `ejercicio1.py` | Sección 6. |
| 06 | `ejercicio2.py` | Sección 7. |
| 06 | `ejercicio3.py` | Sección 8. |
| 06 | `ejercicio4.py` | Sección 9. |
| 06 | `args_defecto.py` | Sección 3.4. |
| 06 | `return_varios.py` | Sección 10.3. |
| 06 | `numero_variable_args.py` | Secciones 10.2, 10.4 y 10.5. |
| 07 | `listas.py` | Secciones 15–18. |
| 07 | `ejercicio.py` | Sección 19. |
| 07 | `listas_multidimensionales.py` | Sección 20. |
| 07 | `compresion_listas.py` | Sección 21. |
| 08 | `tuplas.py` | Sección 22. |
| 09 | `conjuntos.py` | Secciones 23 y 23.1. |
| 09 | `operaciones_conjuntos.py` | Sección 23.2. |
| 10 | `diccionarios.py` | Sección 24. |

Los ocho archivos de funciones incluyen tres incorporaciones respecto a los apuntes del 18 de noviembre. No se presentan esas incorporaciones como meras previsiones del PDF: ya forman parte del ZIP actualizado.

### 27.4. Material utilizado

- [Guía IFCD0062 Fundamentos programacion Python.pdf](<../../IFCD0062 Fundamentos programacion Python.pdf>): módulo 3, pp. 34–43; se ha verificado que la p. 44 comienza el módulo 4.
- [Ejemplo06_Funciones.zip](../../Ejemplo06_Funciones.zip), versión local revisada el 23 de noviembre de 2026.
- [Ejemplo07_Listas.zip](../../Ejemplo07_Listas.zip).
- [Ejemplo08_Tuplas.zip](../../Ejemplo08_Tuplas.zip).
- [Ejemplo09_Conjuntos.zip](../../Ejemplo09_Conjuntos.zip).
- [Ejemplo10_Diccionarios.zip](../../Ejemplo10_Diccionarios.zip).
- [modulo3.md](modulo3.md) y [ejercicio3-1.py](ejercicio3-1.py): tus dudas, comentarios y práctica de listas.
- [Apuntes ampliados del módulo 2](../modulo2/modulo2_apuntes_ampliados.md): control de flujo y recorridos.
- [MASTER-PERSONALIZADO-IA.md](../../../../MASTER-PERSONALIZADO-IA.md) y [ENCAJE-TECNOFOR-MASTER.md](../../../../ENCAJE-TECNOFOR-MASTER.md): orientación de las aplicaciones prácticas.

Apoyo oficial para comprobar matices, sin lectura adicional obligatoria:

- [Tutorial: funciones y control de flujo](https://docs.python.org/es/3.14/tutorial/controlflow.html).
- [Tutorial: listas, comprensiones, tuplas, conjuntos y diccionarios](https://docs.python.org/es/3.14/tutorial/datastructures.html).
- [Referencia: secuencias, slices, conjuntos y diccionarios](https://docs.python.org/es/3.14/library/stdtypes.html).
- [Anotaciones de tipo y su alcance](https://docs.python.org/es/3.14/library/typing.html).

### 27.5. Qué queda para los módulos posteriores

El módulo 4 desarrolla excepciones, módulos, paquetes y métodos de texto; el 5, clases y archivos. Este documento reconoce los errores que pueden aparecer, pero no adelanta su tratamiento completo. APIs, JSON, autenticación y persistencia aplicada se incorporarán después en el puente del máster.

La actualización actual completa el Markdown del módulo 3. El PDF se preparará en una tarea posterior.

