# Módulo 2 · Decisiones, bucles y control del programa

Apuntes integrados de la guía de Ana Isabel Vegas, tus notas y los ejercicios de clase. Revisión: 17 de noviembre de 2026.

**Alcance:** módulo 2 de la guía, páginas 29–33: bloques, condicionales y bucles. Se incorporan `match/case`, guardas, índices, `break`, `continue`, `pass` y números aleatorios porque aparecen en los ZIP y en tus prácticas de este módulo. El módulo 3 empieza en la página 34.

**Cómo utilizarlos:** cada explicación va acompañada de ejemplos adaptados de tus ejercicios. **Aclaración** precisa una idea de tus notas; **Corrección** explica un fallo del material; **Complemento opcional** conecta con tu máster. Los ejemplos corregidos están en este documento: tus archivos originales se conservan como material de aprendizaje.

Los ejemplos con `match` necesitan **Python 3.10 o posterior**. Cada bloque completo está pensado para ejecutarse por separado. Mientras no estudiemos excepciones, las entradas numéricas deben tener un formato convertible: por ejemplo, `3.5`, no `tres` ni `3,5`.

## Índice

1. [Bloques e indentación](#1-bloques-e-indentación)
2. [Elegir con if, elif y else](#2-elegir-con-if-elif-y-else)
3. [Límites, reglas y validación](#3-límites-reglas-y-validación)
4. [Seleccionar con match y case](#4-seleccionar-con-match-y-case)
5. [Iterables y bucle for](#5-iterables-y-bucle-for)
6. [Rangos y salida por pantalla](#6-rangos-y-salida-por-pantalla)
7. [Acumuladores, contadores y banderas](#7-acumuladores-contadores-y-banderas)
8. [Índices, pertenencia y continue](#8-índices-pertenencia-y-continue)
9. [Bucles anidados, números primos y break](#9-bucles-anidados-números-primos-y-break)
10. [Fibonacci y cambios de estado](#10-fibonacci-y-cambios-de-estado)
11. [Repetir con while](#11-repetir-con-while)
12. [Menús: integrar while, match e if](#12-menús-integrar-while-match-e-if)
13. [Aleatoriedad y juegos](#13-aleatoriedad-y-juegos)
14. [Aprendizajes y correcciones de tus archivos](#14-aprendizajes-y-correcciones-de-tus-archivos)
15. [Aplicaciones a tu máster](#15-aplicaciones-a-tu-máster)
16. [Repaso y resultados de referencia](#16-repaso-y-resultados-de-referencia)
17. [Fuentes y qué estudiar después](#17-fuentes-y-qué-estudiar-después)

## 1. Bloques e indentación

Un **bloque** agrupa instrucciones que pertenecen a una estructura. En Python, la indentación indica esa pertenencia: cambia lo que hace el programa.

```python
edad = 16

if edad >= 18:
    print("Puedes entrar")
    print("Presenta tu documento")

print("Comprobación terminada")
```

Las dos primeras llamadas a `print()` están dentro del `if`. La última está fuera y se ejecuta tanto si la edad cumple la condición como si no. Con `16`, solo aparece `Comprobación terminada`.

**Aclaración a tus notas:** indentar no es únicamente una buena práctica visual. Es parte de la sintaxis. La convención recomendada es **cuatro espacios por nivel**. La tecla Tab puede insertar esos espacios si así está configurado el editor; no conviene mezclar caracteres de tabulación y espacios. Consulta [PEP 8](https://peps.python.org/pep-0008/#indentation).

### 1.1. Anidar bloques

Un bloque puede contener otro. Adaptado de tu [calculadora](ejercicio2-6.py):

```python
operacion = "/"
divisor = 0

if operacion == "/":
    if divisor == 0:
        print("No se puede dividir entre cero")
    else:
        print("Se puede calcular la división")

print("Fin de la comprobación")
```

El segundo `if` y su `else` están al mismo nivel; por eso forman una pareja. Se revisa el divisor solo cuando la operación es una división.

### 1.2. Tres comprobaciones al escribir un bloque

1. El encabezado termina en `:`.
2. El contenido está un nivel más a la derecha.
3. Al terminar, vuelves al nivel de la estructura que corresponda.

Una línea en blanco no termina el bloque en un archivo `.py`; lo determina el regreso al nivel anterior. Una indentación incorrecta puede causar un error de sintaxis o, si sigue siendo válida, un comportamiento distinto del esperado.

## 2. Elegir con if, elif y else

`if` permite ejecutar instrucciones según una condición. `elif` añade alternativas y `else` cubre lo que no ha encajado antes.

```python
numero = int(input("Introduce un número entero: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")
```

Se comprueba de arriba abajo. En una misma cadena se ejecuta **solo el primer bloque cuya condición se cumple**. Si ninguno se cumple, se ejecuta `else`, cuando existe.

| Estructura | Cuándo sirve |
|---|---|
| Solo `if` | Hacer algo si se cumple un requisito. |
| `if` y `else` | Elegir entre dos alternativas. |
| `if`, uno o varios `elif`, y `else` | Elegir entre varias posibilidades. |
| Varios `if` independientes | Hacer varias comprobaciones que pueden cumplirse a la vez. |

### 2.1. Varios if no equivalen a una cadena

```python
numero = 6

if numero % 2 == 0:
    print("Es par")
if numero % 3 == 0:
    print("Es múltiplo de tres")
```

Se imprimen los dos mensajes. Si el segundo `if` fuera `elif`, no se comprobaría su condición después de entrar en el primero. Usa la cadena cuando quieras una clasificación excluyente; usa comprobaciones independientes cuando quieras informar de varias propiedades.

### 2.2. Ejemplo: paridad y divisibilidad

Adaptado de [ejercicio2-1.py](ejercicio2-1.py):

```python
numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    if numero % 3 == 0:
        print("Es par y múltiplo de tres")
    else:
        print("Es par y no es múltiplo de tres")
elif numero % 3 == 0:
    print("Es impar y múltiplo de tres")
else:
    print("Es impar y no es múltiplo de tres")
```

Para `6`, `4`, `9` y `5` se recorren, respectivamente, las cuatro alternativas.

**Corrección importante:** `int(numero)` usado dentro de una expresión no convierte permanentemente la variable. En tu archivo se convierte para la primera comprobación, pero después se intenta aplicar `%` al texto original. Convertir al leer, como en este ejemplo, permite reutilizar el entero.

### 2.3. Qué puede actuar como condición

En estos ejercicios usamos comparaciones que producen `True` o `False`, y banderas que ya son booleanas. Python también interpreta otros valores según su valor de verdad: `0`, `""` y `[]` cuentan como falsos; un texto no vacío cuenta como verdadero.

Por eso `if "False":` entra en el bloque: es texto no vacío. Para empezar, escribe condiciones explícitas y distingue `"False"` de `False`.

## 3. Límites, reglas y validación

Antes de programar una regla, aclara qué ocurre exactamente en sus límites. «Más de 100» corresponde a `> 100`; «100 o más», a `>= 100`.

### 3.1. Intervalos y operadores lógicos

En [ejercicio2-2.py](ejercicio2-2.py), el código admite edades de **12 a 65, ambas incluidas**:

```python
edad = int(input("Introduce tu edad: "))

if 12 <= edad <= 65:
    print("Acceso permitido")
elif edad < 12:
    print("Eres menor de 12 años")
else:
    print("Eres mayor de 65 años")
```

`12 <= edad <= 65` equivale aquí a `edad >= 12 and edad <= 65`. Tu comentario «mayores de 12 y menores de 65» sugeriría extremos excluidos; el enunciado del ZIP habla de estar entre ambas edades y la solución los incluye.

| Regla | Expresión |
|---|---|
| Dentro de un intervalo cerrado | `12 <= edad <= 65` |
| Fuera de ese intervalo | `edad < 12 or edad > 65` |
| Ambos requisitos | `usuario == "admin" and clave == "python123"` |
| Negar una bandera | `not terminado` |

Las credenciales literales de [ejercicio2-3.py](ejercicio2-3.py) sirven para practicar `and`; no constituyen un sistema de autenticación para una aplicación real.

### 3.2. Descuentos: ordenar y definir los tramos

En [ejercicio2-5.py](ejercicio2-5.py), el enunciado dice «mayor de 100», pero la solución de clase aplica el 20 % desde `100` incluido. Hay una discrepancia de límite, no un problema de Python.

Si seguimos **literalmente el enunciado** —más de 100: 20 %; más de 50 hasta 100: 10 %—:

```python
precio = float(input("Introduce el precio: "))

if precio < 0:
    print("El precio no puede ser negativo")
else:
    if precio > 100:
        porcentaje = 0.20
    elif precio > 50:
        porcentaje = 0.10
    else:
        porcentaje = 0

    descuento = precio * porcentaje
    print(f"Descuento: {descuento:.2f} €")
    print(f"Precio final: {precio - descuento:.2f} €")
```

Se evalúa primero el umbral mayor. Si empezaras con `if precio > 50`, una compra de `150` entraría ahí y no llegaría a un `elif precio > 100` posterior.

| Precio | Según el enunciado literal | Según el archivo de clase |
|---|---|---|
| 50 | Sin descuento | Sin descuento |
| 75 | 10 % | 10 % |
| 100 | 10 % | 20 % |
| 150 | 20 % | 20 % |

### 3.3. El ejercicio de examen

El [examen-modulo2.py](examen-modulo2.py) usa otra regla: **10 % solo si la compra supera 100 €**, y pide mostrar el importe final en todos los casos.

```python
compra = float(input("Importe de la compra: "))

if compra < 0:
    print("El importe no puede ser negativo")
else:
    precio_final = compra
    if compra > 100:
        precio_final = compra * 0.90
    print(f"Importe final a pagar: {precio_final:.2f} €")
```

Con `150`, muestra `135.00 €`. Con `100`, muestra `100.00 €`. Tu solución calcula bien la rama con descuento; en la otra informa de que no se aplica, pero falta mostrar el importe final solicitado. La comprobación de negativos es una mejora añadida, no un requisito explícito del examen.

### 3.4. Bisiestos y reglas compuestas

De [ejercicio2-4.py](ejercicio2-4.py): un año es bisiesto si es divisible entre 400, o si es divisible entre 4 y no entre 100.

```python
anyo = int(input("Introduce un año positivo: "))

if anyo <= 0:
    print("Para este ejercicio usa un año positivo")
elif anyo % 400 == 0 or (anyo % 4 == 0 and anyo % 100 != 0):
    print("Bisiesto")
else:
    print("No bisiesto")
```

`2000` y `2024` son bisiestos; `1900` y `2026`, no. La versión con dos ramas de tu archivo también expresa correctamente la regla para años positivos.

### 3.5. La nómina como ejercicio de programación

[ejercicio2-7.py](ejercicio2-7.py) combina actualización por IPC, tramos y porcentajes. Usa **reglas ficticias del ejercicio**, no normativa fiscal: el porcentaje seleccionado se aplica a todo el sueldo y se restan dos puntos porcentuales por hijo.

En el primer tramo, con tres hijos, la fórmula da `0.05 - 0.02 * 3 = -0.01`. Una retención negativa aumenta el neto. Si se decide que la retención mínima sea cero, hay que expresarlo como regla añadida: después de calcularla, `if irpf < 0:` seguido de `irpf = 0`.

Además, «descontar un 2 % del IRPF» puede interpretarse como una reducción relativa del impuesto, que no es lo mismo que restar dos puntos. Conviene aclarar el requisito. Con 14 pagas, el resultado representa el **importe de cada paga** si todas son iguales, no necesariamente el ingreso de cada mes natural.

## 4. Seleccionar con match y case

`match` evalúa una expresión e intenta encajar su resultado en los patrones de cada `case`. En clase se utiliza principalmente para seleccionar opciones por su valor.

### 4.1. Calculadora con protección de la división

Adaptada de [ejercicio2-8.py](ejercicio2-8.py):

```python
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

match operacion:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
            print("No se puede dividir entre cero")
        else:
            print(num1 / num2)
    case _:
        print("Operación no válida")
```

El caso `_` es el comodín y se coloca al final. No es obligatorio. Si ningún caso encaja y no hay comodín, se continúa después del `match` sin ejecutar ningún caso. No hace falta `break` entre casos: no se pasa automáticamente al siguiente.

En tu archivo conviven las versiones con `if` y con `match`; si lo ejecutas entero, ambas calculan e imprimen el resultado.

### 4.2. Agrupar alternativas con la barra vertical

De [ejercicio2-9.py](ejercicio2-9.py) y [ejercicio2-10.py](ejercicio2-10.py):

```python
mes = int(input("Mes del 1 al 12: "))

match mes:
    case 12 | 1 | 2:
        print("Invierno")
    case 3 | 4 | 5:
        print("Primavera")
    case 6 | 7 | 8:
        print("Verano")
    case 9 | 10 | 11:
        print("Otoño")
    case _:
        print("Mes no válido")
```

`|` significa alternativas de patrón en este contexto; no se sustituye por `or`. Los números son enteros porque hemos convertido la entrada. También podrías conservarla como texto y usar `case "12" | "1" | "2":`. Hay que mantener la coherencia de tipos.

La clasificación por estaciones es la convención simplificada del ejercicio. En [ejercicio2-11.py](ejercicio2-11.py) se añade un `if` dentro del caso de febrero para calcular sus horas según el año: 672 o 696; los meses de 30 y 31 días tienen 720 y 744 horas, respectivamente, en el cálculo simplificado de días por 24.

### 4.3. Tu duda: ¿por qué aparece num en case?

En [ejercicio2-12.py](ejercicio2-12.py), `case num if num < 6:` tiene dos partes:

1. `num` es un **patrón de captura**: asocia el valor examinado a ese nombre.
2. `if num < 6` es una **guarda**: una condición que debe cumplirse para ejecutar el caso.

```python
password = input("Introduce un texto para clasificar su longitud: ")
longitud = len(password)

match longitud:
    case num if num < 6:
        print("Menos de 6 caracteres")
    case num if 6 <= num <= 8:
        print("De 6 a 8 caracteres")
    case num if 9 <= num <= 12:
        print("De 9 a 12 caracteres")
    case _:
        print("Más de 12 caracteres")
```

Con un texto de nueve caracteres, el valor capturado es `9`. La tercera guarda se cumple. Podrías llamar al nombre `cantidad`; no existe nada especial en `num`.

**Aclaración:** no es que Python adivine por inferencia que dos variables significan lo mismo. Es una regla de la sintaxis de patrones. Un nombre simple sin comillas, como `case opcion:`, **captura** el valor; no lo compara con una variable previa. Para alternativas literales usa números o textos entre comillas.

Tampoco es exacto decir que `case` solo admite valores y nunca condiciones: el patrón puede llevar una guarda. Para clasificar intervalos sencillos, un `if/elif` suele resultar más directo. La documentación de [patrones y guardas](https://docs.python.org/es/3.14/reference/compound_stmts.html#the-match-statement) desarrolla estos matices.

Las etiquetas de fortaleza de contraseña del ejercicio son una simplificación: `len()` mide longitud, no demuestra seguridad. Aquí practicamos clasificación.

### 4.4. La expresión condicional de una línea

También aparece en el ejercicio 12:

```python
numero = 9
divisor3 = numero if numero % 3 == 0 else 0
print(divisor3)
```

Se lee: «asigna `numero` si es múltiplo de tres; en caso contrario, asigna cero». Primero se evalúa la condición y después solo la alternativa elegida. Para `9`, resulta `9`; para `10`, resultaría `0`.

Esta forma produce un valor y puede usarse en una asignación. Un bloque `if` organiza instrucciones. Usa la expresión de una línea cuando la elección sea breve y clara.

## 5. Iterables y bucle for

Un **iterable** permite obtener sus elementos uno tras otro. En este módulo recorres listas, textos y rangos; las colecciones se desarrollarán en el módulo 3.

```python
nombres = ["Luis", "Jorge", "María", "Laura", "Pedro"]

for nombre in nombres:
    print(nombre)
```

La variable `nombre` recibe cada elemento por turno: primero `"Luis"`, luego `"Jorge"`, etc. Es el papel de la «variable auxiliar» de tus notas. Puedes escoger su nombre, pero conviene que describa el elemento.

**Aclaración:** no es un puntero que avanza dentro de la lista. Es un nombre al que el bucle va asignando el elemento actual. Python trabaja con objetos y referencias; no necesitas gestionar punteros para resolver estos ejercicios.

Los corchetes crean una lista porque esa es su sintaxis, no porque el lenguaje adivine nuestra intención. La propiedad relevante de Python aquí es el **tipado dinámico**.

### 5.1. for no significa necesariamente contar

El `for` recorre elementos; `range()` permite que esos elementos sean una progresión de enteros. En una lista conocida puedes prever cuántas iteraciones habrá si no interrumpes el recorrido. Otros iterables no tienen por qué tener una longitud conocida de antemano.

```python
for letra in "Python":
    print(letra, end=" ")
print()
```

Muestra `P y t h o n`. Si el iterable está vacío, el cuerpo no se ejecuta ninguna vez.

### 5.2. Cambiar la variable no cambia automáticamente la lista

```python
numeros = [3, 8, 1]

for numero in numeros:
    numero = numero * 2

print(numeros)
```

La lista sigue siendo `[3, 8, 1]`. En este caso reasignas la variable del bucle a otro entero, pero no asignas nada a las posiciones de la lista. Esta distinción ayuda a entender por qué el primer intento de suma del ejercicio 13 no acumula un total.

## 6. Rangos y salida por pantalla

`range(inicio, fin, paso)` representa una secuencia de enteros. El inicio se incluye y el final se excluye.

| Expresión | Valores recorridos |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 |
| `range(10, 0, -1)` | 10, 9, 8, …, 1 |
| `range(10, -1, -2)` | 10, 8, 6, 4, 2, 0 |
| `range(2, 2)` | Ninguno: rango vacío. |
| `range(1, 5, -1)` | Ninguno: el paso va en sentido contrario. |

Si omites el inicio, es cero; si omites el paso, es uno. El paso no puede ser cero. Técnicamente, `range` es un tipo de secuencia inmutable, no una lista ni una función generadora; conserva una representación compacta del rango sin construir una lista con todos los enteros.

### 6.1. Incluir o excluir el último número

Para recorrer del 1 al 10, ambos incluidos:

```python
for numero in range(1, 11):
    print(numero, end=" ")
print()
```

Piensa en el primer valor que queda fuera: `11`. Para incluir el cero al bajar desde diez, puedes usar `range(10, -1, -1)`.

En `range(2, numero)`, el último posible divisor es `numero - 1`. En cambio, `range(2, numero - 1)` terminaría antes: su último posible valor sería `numero - 2`.

### 6.2. sep y end hacen cosas diferentes

Tu comentario en [ejercicio2-14.py](ejercicio2-14.py) distingue bien ambos conceptos:

| Parámetro | Qué controla | Valor habitual por defecto |
|---|---|---|
| `sep` | Separación entre argumentos de una misma llamada. | Un espacio. |
| `end` | Qué se escribe al terminar esa llamada. | Un salto de línea. |

`print(numero)` dentro del bucle coloca cada número en una línea porque cada llamada termina con salto de línea. `print(numero, end=" ")` los deja en una misma línea. El `print()` final introduce un salto, no una línea de espacios.

### 6.3. Tabla de multiplicar

Adaptada de [ejercicio2-15.py](ejercicio2-15.py):

```python
tabla = int(input("Número de tabla del 1 al 10: "))

if 1 <= tabla <= 10:
    for numero in range(1, 11):
        print(f"{tabla} x {numero} = {tabla * numero}")
else:
    print("Elige un número del 1 al 10")
```

Pedir un dato «del 1 al 10» en el mensaje no impide introducir otro: la validación necesita código. Guardar el producto en una variable, como haces en tu primera versión, también es correcto.

## 7. Acumuladores, contadores y banderas

Estas variables conservan información entre iteraciones. Sus nombres describen su función en el algoritmo, no tipos especiales de Python.

| Papel | Qué guarda | Ejemplo |
|---|---|---|
| Acumulador | Un resultado que se construye progresivamente. | Suma de cantidades. |
| Contador | Cuántas veces ha ocurrido algo. | Número de tiradas. |
| Bandera | Un estado verdadero o falso. | Si se ha encontrado un divisor. |
| Variable de recorrido | El elemento o número actual. | `num` en `for num in numeros`. |

### 7.1. Acumular una suma

De [ejercicio2-13.py](ejercicio2-13.py):

```python
numeros = [3, 8, 1, 5, 9]
resultado = 0

for num in numeros:
    resultado += num

print("Resultado:", resultado)
```

| Iteración | num | resultado antes | resultado después |
|---|---|---|---|
| 1 | 3 | 0 | 3 |
| 2 | 8 | 3 | 11 |
| 3 | 1 | 11 | 12 |
| 4 | 5 | 12 | 17 |
| 5 | 9 | 17 | 26 |

**Corrección de tu comentario:** el primer intento no solo duplica el primer `3`. En cada vuelta hace `anterior = num` y después suma el elemento consigo mismo. Obtiene sucesivamente `6`, `16`, `2`, `10` y `18`, pero no conserva un total; el `print()` final muestra `18`.

El acumulador debe inicializarse **antes** del bucle. Si lo reinicias dentro, pierdes lo acumulado. El resultado final se imprime fuera; un `print()` dentro mostraría subtotales, algo útil para observar la ejecución.

### 7.2. Acumular un producto: factorial

Adaptado de [ejercicio2-19.py](ejercicio2-19.py):

```python
numero = int(input("Entero no negativo: "))

if numero < 0:
    print("El factorial de este ejercicio requiere un entero no negativo")
else:
    resultado = 1
    for factor in range(numero, 0, -1):
        resultado *= factor
    print(f"{numero}! = {resultado}")
```

Para `5`, calcula `1 × 5 × 4 × 3 × 2 × 1 = 120`. En un producto se empieza en `1`; empezar en `0` dejaría siempre el resultado a cero.

Para `0`, el rango está vacío y se conserva `1`, que es el valor correcto de `0!`. Sin la validación, una entrada negativa también dejaría `1`, aunque no corresponde al factorial de enteros no negativos que practica el ejercicio.

## 8. Índices, pertenencia y continue

### 8.1. Elemento e índice

Una lista de cinco elementos tiene índices de `0` a `4`:

| Índice | Elemento de la lista de nombres |
|---|---|
| 0 | Luis |
| 1 | Jorge |
| 2 | María |
| 3 | Laura |
| 4 | Pedro |

`len(nombres)` vale `5`, pero `nombres[5]` no existe. `range(len(nombres))` recorre `0, 1, 2, 3, 4`.

Adaptado de [ejercicio2-20.py](ejercicio2-20.py):

```python
nombres = ["Luis", "Jorge", "María", "Laura", "Pedro"]

for indice in range(len(nombres)):
    if indice % 2 == 0:
        print(nombres[indice])
```

Muestra Luis, María y Pedro. Son los índices pares `0, 2, 4`, que corresponden a la primera, tercera y quinta posición si contamos coloquialmente desde uno.

**Corrección:** tu archivo crea `nombre`, pero recorre `nombres`. En una ejecución independiente produce `NameError`. Conviene ejecutar cada archivo desde cero: una variable que quedó definida en una consola puede ocultar un error de nombre.

### 8.2. in: comprobar pertenencia

```python
datos = ["t", "a", "w", "p", "o", "z", "i"]

for letra in datos:
    if letra in ["a", "e", "i", "o", "u"]:
        print(letra)
```

Muestra `a`, `o` e `i`. Aquí `in` hace una comprobación de pertenencia. En `for letra in datos`, forma parte de la estructura de recorrido.

Para usar un índice, debe ser entero en estos ejemplos. Si `letra` vale `"a"`, `datos[letra]` no es válido: para mostrar la letra ya tienes `print(letra)`.

### 8.3. Vocales solo en índices impares

Adaptado de [ejercicio2-21.py](ejercicio2-21.py):

```python
datos = ["t", "a", "w", "p", "o", "z", "i"]

for indice in range(len(datos)):
    if indice % 2 != 0 and datos[indice] in ["a", "e", "i", "o", "u"]:
        print(datos[indice])
```

Solo muestra `a`: está en el índice `1`. La `o` y la `i` están en los índices `4` y `6`, que son pares.

**Corrección:** a tu primer `if` le faltan `:` y un cuerpo. Ese error de sintaxis impide ejecutar el archivo entero, aunque más abajo haya alternativas correctas.

En la alternativa larga con varias comparaciones hace falta agrupar las vocales: `condicion_indice and (es_a or es_e or es_i or es_o or es_u)`. `and` tiene prioridad sobre `or`: sin paréntesis, la condición del índice solo se aplica al primer término. La versión con `in` expresa mejor la intención.

### 8.4. continue: saltar el resto de una vuelta

```python
datos = ["t", "a", "w", "p", "o", "z", "i"]

for indice in range(len(datos)):
    if indice % 2 == 0:
        continue
    if datos[indice] in ["a", "e", "i", "o", "u"]:
        print(datos[indice])
```

Si el índice es par, se omite lo que queda de esa vuelta. El bucle continúa con el siguiente índice. También muestra solo `a`.

En un `while`, `continue` vuelve a evaluar su condición. Si una actualización necesaria queda después del `continue`, puede no llegar a ejecutarse y el bucle quedarse sin avanzar.

## 9. Bucles anidados, números primos y break

### 9.1. Un recorrido dentro de otro

Adaptado de [ejercicio2-16.py](ejercicio2-16.py):

```python
for tabla in range(1, 11):
    print(f"Tabla del número {tabla}")
    for numero in range(1, 11):
        print(f"{tabla} x {numero} = {tabla * numero}")
    print()
```

Para `tabla = 1`, el bucle interior hace sus diez vueltas. Después se ejecuta el `print()` vacío, y el exterior pasa a `tabla = 2`. Hay diez tablas y cien multiplicaciones.

**Corrección de presentación:** en `print('Tabla del número', {tabla})`, las llaves crean un conjunto de un elemento; por eso aparece `{1}`. Para mostrar el número usa una f-string o `print("Tabla del número", tabla)`.

### 9.2. Comprobar si un número es primo

Un primo es un entero **mayor que 1** con exactamente dos divisores positivos: uno y él mismo. Adaptado de [ejercicio2-17.py](ejercicio2-17.py):

```python
numero = int(input("Introduce un entero: "))
es_primo = numero >= 2

for divisor in range(2, numero):
    if numero % divisor == 0:
        es_primo = False
        break

if es_primo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
```

La bandera empieza en `False` para números menores que dos. Para los demás, suponemos que son primos hasta encontrar un divisor que lo contradiga.

- Si aparece un divisor exacto, basta para descartar la primalidad y salir con `break`.
- Si un divisor no sirve, no podemos declarar todavía que el número es primo: faltan los demás.
- El resultado se imprime al terminar la búsqueda, no una vez por cada divisor.

**Corrección de clase:** las versiones que empiezan siempre con `esPrimo = True` clasifican mal `1`, `0` y los negativos, porque sus rangos están vacíos. La corrección es necesaria también en el ZIP.

En tu primer intento, además, el mensaje está invertido: un resto cero demuestra que hay un divisor, por lo que el número no es primo.

### 9.3. Primos hasta cien

Adaptado de [ejercicio2-18.py](ejercicio2-18.py):

```python
for numero in range(2, 101):
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, end=" ")
print()
```

Se empieza en `2` para excluir el `1`. La bandera se reinicia para cada candidato. El `break` sale **solo del bucle interior**, el de divisores; el recorrido de candidatos continúa.

Salen 25 primos: `2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97`.

Para estos ejercicios basta esta solución. Buscar únicamente hasta la raíz cuadrada o usar una criba son optimizaciones posibles que no necesitas incorporar ahora.

### 9.4. Diferenciar break, continue y pass

| Instrucción | Efecto |
|---|---|
| `break` | Termina el bucle más cercano que la contiene. |
| `continue` | Omite el resto de la iteración del bucle más cercano. |
| `pass` | No hace nada; permite escribir un bloque vacío válido. |

`pass` no salta una iteración ni termina una estructura. Si después hay otra instrucción en el mismo bloque, se ejecuta normalmente. En el caso de salida de un menú puede servir como hueco explícito, pero la salida la determina la condición del `while`.

## 10. Fibonacci y cambios de estado

En [ejercicio2-22.py](ejercicio2-22.py), quieres los cien primeros términos, no los términos menores que cien. Usamos la convención de empezar en `0, 1`.

```python
n1 = 0
n2 = 1

for posicion in range(1, 101):
    print(f"Término {posicion}: {n1}")
    suma = n1 + n2
    n1 = n2
    n2 = suma
```

| Vuelta | n1 mostrado | n2 antes de actualizar | suma | Pareja para la vuelta siguiente |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 1 y 1 |
| 2 | 1 | 1 | 2 | 1 y 2 |
| 3 | 1 | 2 | 3 | 2 y 3 |
| 4 | 2 | 3 | 5 | 3 y 5 |
| 5 | 3 | 5 | 8 | 5 y 8 |

Se guarda `suma` antes de cambiar `n1`, porque necesita los dos valores anteriores. Si hicieras `n1 = n2` y después `n2 = n1 + n2`, habrías perdido el antiguo `n1` y sumarías dos veces el mismo valor.

Tu versión ya mantiene bien ese orden. La profesora imprime primero dos términos y calcula 98 más: también obtiene cien. En la tuya, el término 1 es `0` y el término 100 es `218922995834555169026`.

## 11. Repetir con while

`while` comprueba una condición **antes de cada vuelta**. Ejecuta su bloque mientras se interprete como verdadera. Si ya es falsa al empezar, no entra ninguna vez.

### 11.1. Inicializar, comprobar y actualizar

De [ejercicio2-24.py](ejercicio2-24.py):

```python
numero = 1

while numero <= 10:
    print(numero)
    numero += 1
```

La inicialización da un punto de partida; la condición fija cuándo continuar; la actualización permite avanzar hacia el final. Si se elimina el incremento, se imprime `1` indefinidamente.

Para mostrar pares desde cero hasta un límite incluido:

```python
limite = int(input("Límite entero no negativo: "))
numero = 0

if limite < 0:
    print("El límite debe ser no negativo")
else:
    while numero <= limite:
        if numero % 2 == 0:
            print(numero)
        numero += 1
```

**Corrección:** tu archivo utiliza `numerp` en vez de `numero`. Además, `< limite` excluiría el extremo; usamos `<=` para incluirlo si es par.

### 11.2. Repetir una entrada

De [ejercicio2-23.py](ejercicio2-23.py):

```python
password = ""

while password != "curso":
    password = input("Introduce la contraseña del ejercicio: ")

print("Contraseña correcta")
```

El texto inicial vacío fuerza la primera pregunta. La entrada dentro del bucle actualiza lo que se comprobará en la vuelta siguiente. El ejemplo enseña repetición; un acceso real necesita otros controles, entre ellos límites de intentos.

### 11.3. Valor centinela: sumar hasta FIN

Un **centinela** es un valor especial que indica que debemos parar. Adaptado de [ejercicio2-25.py](ejercicio2-25.py) y de la solución de la profesora:

```python
total = 0
dato = ""

while dato != "FIN":
    dato = input("Introduce un entero o FIN: ")
    if dato != "FIN":
        total += int(dato)

print("Suma:", total)
```

Con entradas `3`, `8`, `-2`, `FIN`, muestra `9`. Si se introduce `FIN` lo primero, muestra `0`.

El centinela debe comprobarse **antes** de intentar convertirlo a entero. También hay que pedir un dato nuevo en cada vuelta: tu primer intento no lo actualiza y se queda repitiendo el mismo valor.

Esta versión diferencia mayúsculas y minúsculas: se sale con `FIN`, no con `fin`. La limpieza de textos se verá después. La versión corregida de tu propio archivo, que pregunta antes del bucle y de nuevo dentro, también funciona.

### 11.4. Elegir for o while

| Necesidad | Opción habitual |
|---|---|
| Recorrer cada elemento de una lista | `for`. |
| Repetir diez veces | `for` con `range()`. |
| Preguntar hasta una respuesta válida | `while`. |
| Mantener un menú hasta salir | `while`. |
| Buscar hasta encontrar algo | `for` con `break` o `while`, según el caso. |

Un `while` también puede repetir una cantidad conocida de veces, como el del 1 al 10. La distinción «determinado/indeterminado» describe el problema habitual, no una prohibición del lenguaje.

## 12. Menús: integrar while, match e if

Tu [ejercicio2-26.py](ejercicio2-26.py) reúne decisiones, repetición y cambios de saldo. Una organización útil es presentar el menú y leer la opción **una sola vez por vuelta**, antes del `match`.

```python
saldo = 996.0
opcion = ""

while opcion != "4":
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            print(f"Saldo: {saldo:.2f} €")
        case "2":
            ingreso = float(input("Cantidad a ingresar: "))
            if ingreso > 0:
                saldo += ingreso
                print(f"Saldo: {saldo:.2f} €")
            else:
                print("La cantidad debe ser positiva")
        case "3":
            retiro = float(input("Cantidad a retirar: "))
            if retiro <= 0:
                print("La cantidad debe ser positiva")
            elif retiro > saldo:
                print("Saldo insuficiente")
            else:
                saldo -= retiro
                print(f"Saldo: {saldo:.2f} €")
        case "4":
            pass
        case _:
            print("Opción incorrecta")

print("Gracias por tu visita")
```

El `while` conserva el menú, `match` elige la operación y `if` comprueba reglas de cada operación. `pass` no sale del bucle: tras ese caso se llega al final de la vuelta y la condición detecta que `opcion` ya vale `"4"`.

**Lo que resuelve respecto a tus dos versiones:**

- En la primera, una opción inválida no pide una nueva entrada y repite el error indefinidamente.
- En la segunda, `input()` devuelve texto, pero el `while` compara con el entero `4`; `"4" != 4` siempre es verdadero.
- La opción de salida necesita un tratamiento propio para que no aparezca «opción incorrecta» al salir.
- Se comprueban cantidades positivas: retirar un valor negativo no debe aumentar el saldo.

Para probar: consultar → ingresar `4` → retirar `1000` → consultar → salir. Los saldos serán `996`, `1000`, `0`, `0`.

Es una simulación de clase en memoria; al reiniciar pierde el saldo. El formato con dos decimales no añade exactitud aritmética al tipo `float`. La persistencia y la representación de dinero real se tratarán cuando corresponda.

## 13. Aleatoriedad y juegos

Los ejercicios 27–30 introducen `import random`. El módulo viene con Python; no hay que instalarlo.

`random.randint(a, b)` devuelve un entero entre **a y b incluidos**. Esa inclusión del extremo superior lo diferencia de `range(a, b)`. Son números pseudoaleatorios adecuados para estas simulaciones; no se usan para generar credenciales de seguridad. Consulta la [documentación de random](https://docs.python.org/es/3.14/library/random.html).

### 13.1. Adivinar un número

Adaptado de [ejercicio2-27.py](ejercicio2-27.py):

```python
import random

secreto = random.randint(1, 10)
adivinar = 0

while adivinar != secreto:
    adivinar = int(input("Adivina un número del 1 al 10: "))
    if adivinar < 1 or adivinar > 10:
        print("Elige un número dentro del intervalo")
    elif adivinar < secreto:
        print("Te has quedado corta")
    elif adivinar > secreto:
        print("Te has pasado")

print(f"¡Correcto! Era {secreto}")
```

El secreto se elige una vez, antes del bucle. La validación de rango va primero: en tu primera versión está después de las comparaciones con el secreto, de modo que nunca se alcanza para los valores fuera de rango. El cero también está fuera de `1–10`.

En tu segunda versión, el mensaje final usa `variable`, que conserva el `7` de la prueba anterior, en vez del número aleatorio. El mensaje debe mostrar el secreto utilizado en esa partida.

### 13.2. Tirar hasta obtener seis: qué cuenta el contador

Adaptado de [ejercicio2-28.py](ejercicio2-28.py):

```python
import random

dado = 0
contador = 0

while dado != 6:
    dado = random.randint(1, 6)
    contador += 1
    print(f"Ha salido {dado}")

print(f"Han hecho falta {contador} tiradas")
```

Esta versión cuenta **todas las tiradas, incluida la ganadora**. Si sale seis al primer intento, el contador vale uno. Tu versión cuenta las tiradas que no son seis y no imprime la ganadora: con un seis inicial informa de cero. No está mal contar fallos, pero habría que nombrarlos como tales.

Tener la posibilidad de sacar seis no garantiza que ocurra en un número acotado de vueltas. Para una simulación práctica se podría añadir un límite de tiradas; el ejemplo reproduce el objetivo del ejercicio.

### 13.3. Carrera: definir antes qué significa empate

La solución de clase de [ejercicio2-29.py](ejercicio2-29.py) deja tirar a ambos participantes en cada ronda y compara al terminar. Seguimos esa regla: si ambos alcanzan o superan diez en la misma ronda, hay empate.

```python
import random

juan = 0
miguel = 0

while juan < 10 and miguel < 10:
    juan += random.randint(1, 6)
    miguel += random.randint(1, 6)
    print(f"Juan: {juan} km; Miguel: {miguel} km")

if juan >= 10 and miguel >= 10:
    print("Empate")
elif juan >= 10:
    print("Gana Juan")
else:
    print("Gana Miguel")
```

Se continúa mientras **ninguno** haya terminado: ambos deben seguir por debajo de diez, de ahí el `and`. Con `or`, continuaríamos mientras quedara al menos uno por debajo.

Si decides que gana quien cruza primero por orden de turno, hay que comprobar después de cada tirada y ya no tienes la misma regla de empate. Mezclar ambas reglas dentro del bucle es lo que complica tu primera solución.

### 13.4. Piedra, papel o tijera: terminar tanto al ganar como al perder

Esta versión, adaptada de [ejercicio2-30.py](ejercicio2-30.py), repite solo las entradas inválidas y los empates. Termina cuando hay un resultado decisivo.

```python
import random

terminado = False

while not terminado:
    jugador = int(input("1. Piedra; 2. Papel; 3. Tijera: "))
    if jugador < 1 or jugador > 3:
        print("Opción no válida")
        continue

    ordenador = random.randint(1, 3)
    print(f"El ordenador ha elegido {ordenador}")

    if jugador == ordenador:
        print("Empate: jugamos otra vez")
    else:
        gana_jugador = (
            (jugador == 1 and ordenador == 3)
            or (jugador == 2 and ordenador == 1)
            or (jugador == 3 and ordenador == 2)
        )
        if gana_jugador:
            print("Has ganado")
        else:
            print("Has perdido")
        terminado = True
```

En tu archivo, perder no cambia `campeon` ni vuelve a pedir jugada. Se imprime «Has perdido» sin parar. Una bandera llamada `terminado` refleja mejor el objetivo: terminar cuando cualquiera gana. También se corrige la etiqueta del duelo entre piedra y tijera.

La versión del ZIP tiene otro objetivo: permite jugar más partidas hasta contestar `N`. Ambas formas son válidas si la condición de salida corresponde a la regla elegida.

## 14. Aprendizajes y correcciones de tus archivos

Esta revisión explica el material disponible; no modifica tus `.py`. Varias prácticas contienen intentos, alternativas y notas: al ejecutar el archivo entero se ejecutan todas las partes activas en orden. Un error temprano puede impedir llegar a una solución posterior.

### 14.1. Decisiones y patrones: ejercicios 1–12

| Archivo | Aprendizaje o ajuste |
|---|---|
| [2-1](ejercicio2-1.py) | Convertir la entrada una vez. Aplicar `int()` en una expresión no cambia el texto guardado. |
| [2-2](ejercicio2-2.py) | El código incluye 12 y 65; el comentario de extremos estrictos no coincide. |
| [2-3](ejercicio2-3.py) | `and` exige que usuario y clave coincidan a la vez. |
| [2-4](ejercicio2-4.py) | La divisibilidad por 400 es la excepción a la exclusión de los siglos. |
| [2-5](ejercicio2-5.py) | La solución aplica 20 % a 100, aunque el enunciado dice más de 100. |
| [2-6](ejercicio2-6.py) | Proteger la división por cero dentro de la rama correspondiente. |
| [2-7](ejercicio2-7.py) | Modelo ficticio; distinguir porcentaje, puntos porcentuales y paga. Revisar retenciones negativas. |
| [2-8](ejercicio2-8.py) | Comparación útil entre `if` y `match`; al ejecutar entero salen ambos resultados. |
| [2-9](ejercicio2-9.py) | `|` agrupa alternativas de patrón, incluidas mayúscula y minúscula. |
| [2-10](ejercicio2-10.py) | Los literales del patrón deben corresponder al tipo de la entrada. |
| [2-11](ejercicio2-11.py) | Anidar la regla de bisiesto dentro del caso febrero; contiene dos versiones completas. |
| [2-12](ejercicio2-12.py) | `num` captura el valor; la guarda lo comprueba. La expresión condicional produce un valor. |

### 14.2. Recorridos y estado: ejercicios 13–22

| Archivo | Aprendizaje o ajuste |
|---|---|
| [2-13](ejercicio2-13.py) | El primer intento duplica cada elemento; la suma necesita un acumulador separado. |
| [2-14](ejercicio2-14.py) | Último valor excluido; paso negativo; distinguir `sep` y `end`. |
| [2-15](ejercicio2-15.py) | Las dos versiones son válidas; el mensaje del `input` no valida el intervalo. |
| [2-16](ejercicio2-16.py) | Las llaves fuera de una f-string crean un conjunto; no interpolan. |
| [2-17](ejercicio2-17.py) | Imprimir al final, corregir mensajes invertidos y descartar números menores que dos. |
| [2-18](ejercicio2-18.py) | Reiniciar bandera por candidato y empezar en dos; la solución de clase también incluye mal el uno. |
| [2-19](ejercicio2-19.py) | Producto desde uno; `0! = 1`; validar negativos. |
| [2-20](ejercicio2-20.py) | Corregir `nombre`/`nombres`; longitud cinco implica índices de cero a cuatro. |
| [2-21](ejercicio2-21.py) | Completar `if`, usar índices enteros y agrupar las alternativas con `or`. |
| [2-22](ejercicio2-22.py) | Conservar valores anteriores con una variable temporal; cien términos no equivale a llegar al valor cien. |

### 14.3. Repetición y juegos: ejercicios 23–30 y examen

| Archivo | Aprendizaje o ajuste |
|---|---|
| [2-23](ejercicio2-23.py) | Actualizar la contraseña en cada vuelta. |
| [2-24](ejercicio2-24.py) | Corregir `numerp`; decidir si se incluye el límite superior. |
| [2-25](ejercicio2-25.py) | Pedir un dato nuevo y conservar el total. La primera versión se bloquea. |
| [2-26](ejercicio2-26.py) | Leer la opción en todas las vueltas y comparar tipos compatibles; validar cantidades. |
| [2-27](ejercicio2-27.py) | Validar rango antes de las pistas; mostrar el secreto de la partida actual. |
| [2-28](ejercicio2-28.py) | Definir si se cuentan todos los lanzamientos o solo los fallidos. |
| [2-29](ejercicio2-29.py) | Elegir reglas de ronda y empate antes de distribuir condiciones. |
| [2-30](ejercicio2-30.py) | Actualizar el estado también al perder; validar opciones y corregir el mensaje del duelo. |
| [Examen](examen-modulo2.py) | El caso 150 da 135; falta mostrar el importe final cuando no hay descuento. |

### 14.4. Método para revisar un programa pequeño

1. Escribe qué recibe, qué debe hacer y cuándo termina.
2. Anota el tipo de cada entrada: texto, entero o decimal.
3. Distingue variables de recorrido, resultados acumulados y banderas.
4. Simula dos o tres vueltas en una tabla antes de ejecutar.
5. Comprueba los límites exactos y qué sucede si no hay ninguna vuelta.
6. Revisa cada camino: éxito, error de dominio, opción desconocida y salida.
7. Ejecuta el archivo desde cero y contrasta el resultado con lo calculado a mano.

En un bucle que se queda repitiendo, pregunta: **¿qué variable debería cambiar para permitir la salida y en qué ramas se actualiza?** Para detener una ejecución de terminal, normalmente puedes pulsar `Ctrl+C`.

## 15. Aplicaciones a tu máster

**Complemento opcional.** Este módulo de Python refuerza el módulo 3 del máster personalizado, «APIs, webhooks y Python práctico», y prepara lógica que reutilizarás en automatizaciones, agentes y evaluación. No se presenta como temario adicional del examen.

| Base de este módulo | Aplicación posterior |
|---|---|
| Condiciones y validación | Decidir si un registro puede seguir por un workflow. |
| `match` y menús | Elegir una operación o una ruta entre opciones conocidas. |
| Recorridos y acumuladores | Procesar lotes y sumar consumos o incidencias. |
| Banderas y actualización de estado | Saber si un proceso terminó, falló o requiere revisión. |
| Límites y salida de bucles | Acotar reintentos y evitar agentes que repiten acciones sin avanzar. |
| Casos de borde y resultados esperados | Detectar regresiones en el código generado por IA. |

### 15.1. Miniaplicación: procesar un lote con presupuesto

Las cantidades son ficticias y se expresan en céntimos enteros para que la comparación sea exacta. No se llama a ningún servicio ni se genera gasto.

```python
costes_centimos = [2, 4, 3, 5]
presupuesto_centimos = 10
gastado_centimos = 0
procesados = 0

for coste in costes_centimos:
    if gastado_centimos + coste > presupuesto_centimos:
        print("Se detiene el lote por presupuesto")
        break
    gastado_centimos += coste
    procesados += 1

print(f"Elementos procesados: {procesados}")
print(f"Coste simulado: {gastado_centimos / 100:.2f} €")
```

Procesa los tres primeros elementos y acumula nueve céntimos. El cuarto elevaría el total a catorce, por eso se detiene **antes** de contabilizarlo. Esta política detiene el lote; si quisieras saltarte una tarea cara y revisar las siguientes, tendrías que definir otra política y usar `continue` donde corresponda.

En un sistema real, un coste estimado no garantiza el coste final. Más adelante añadirás medición y límites en el punto donde se ejecuta la llamada. El aprendizaje actual es comprobar un requisito antes de cambiar el estado.

### 15.2. Miniaplicación: reintentos simulados con límite

```python
intento = 0
max_intentos = 3
completado = False

while intento < max_intentos and not completado:
    intento += 1
    print(f"Intento {intento}")
    if intento == 2:
        completado = True

if completado:
    print("Tarea completada")
else:
    print("Límite de intentos alcanzado")
```

La simulación tiene éxito en el segundo intento. Si cambias la condición de éxito a `intento == 5`, hace tres intentos y termina sin completarse. Se separan el **estado de éxito** y el **límite de repetición**.

En una API real, reintentar requiere distinguir errores recuperables y evitar duplicar acciones; aparecerán excepciones, esperas e idempotencia. Este ejemplo solo enseña la estructura de control.

### 15.3. Leer código generado por IA con criterio

Tu preocupación por las regresiones se puede concretar ya: guarda casos de referencia y comprueba sus salidas después de un cambio. Que el código «parezca limpio» o lo haya escrito una IA no acredita que termine ni que respete los límites.

Las preguntas más útiles ahora son: ¿mantiene los tipos?, ¿actualiza las variables correctas?, ¿incluye todos los casos?, ¿tiene una salida posible?, ¿preserva resultados anteriores cuando los necesita? Cuando llegues a funciones podrás convertir estos casos en pruebas automatizadas pequeñas.

## 16. Repaso y resultados de referencia

### 16.1. Lo que deberías poder explicar sin copiar

- Por qué la indentación modifica el comportamiento de un programa.
- Cuándo usar `elif` y cuándo varios `if` independientes.
- Por qué `> 100` y `>= 100` no expresan la misma regla.
- Cómo funcionan `case _`, `|` y una guarda con captura.
- Qué diferencia hay entre un elemento, su índice y la longitud de la lista.
- Por qué el final de `range()` se excluye.
- Por qué una suma empieza en cero y un producto en uno.
- Qué variable conserva el estado entre iteraciones.
- Qué diferencia hay entre `break`, `continue` y `pass`.
- Qué debe cambiar para que un `while` pueda terminar.
- Por qué una salida se imprime dentro o fuera de un bucle según el objetivo.

### 16.2. Casos para comprobarte

Los resultados corresponden a las versiones explicadas o corregidas de estos apuntes, que pueden diferir de los intentos originales.

| Práctica | Datos o caso | Resultado esperado |
|---|---|---|
| Piscina | 11, 12, 65 y 66 | No, sí, sí y no. |
| Descuento de examen | 99, 100 y 150 | 99.00, 100.00 y 135.00 €. |
| Bisiestos | 1900, 2000 y 2024 | No, sí y sí. |
| Calculadora | 8 dividido entre 0 | Mensaje de división no válida. |
| Longitud con guardas | 5, 6, 8, 9, 12 y 13 caracteres | Se recorren correctamente los cuatro tramos. |
| Suma | 3, 8, 1, 5 y 9 | 26. |
| Índices pares | Lista de cinco nombres | Luis, María y Pedro. |
| Vocales en índice impar | t, a, w, p, o, z, i | Solo a. |
| Primalidad | −1, 0, 1, 2, 4 y 97 | No, no, no, sí, no y sí. |
| Primos de 2 a 100 | Recorrido completo | 25 números; primero 2 y último 97. |
| Factorial | 0 y 5 | 1 y 120. |
| Fibonacci | Primeros seis términos | 0, 1, 1, 2, 3 y 5. |
| Pares con while | Límite 6 | 0, 2, 4 y 6. |
| Suma con centinela | 3, 8, −2 y FIN | 9. |
| Suma con centinela | FIN como primera entrada | 0. |
| Dado | Secuencia simulada 2, 4, 6 | Tres tiradas, incluida la ganadora. |
| Carrera | Ambos llegan a 10 o más en una ronda | Empate, según la regla elegida. |
| Lote con presupuesto | Costes 2, 4, 3, 5; límite 10 | Tres procesados; gasto 9 céntimos. |

Con aleatoriedad no se espera el mismo resultado en cada ejecución. Para revisar la lógica, imagina o fija una secuencia de tiradas conocida y comprueba los cambios de estado.

### 16.3. Ocho preguntas de autoevaluación

1. Si un precio es 100, ¿cumple `precio > 100`? ¿Y `precio >= 100`?
2. ¿Cuántas vueltas hace `range(1, 11)`? ¿Y `range(2, 2)`?
3. Una lista tiene longitud cinco. ¿Cuál es su último índice?
4. ¿Qué ocurre si reinicias `total = 0` dentro de cada vuelta de una suma?
5. ¿Puede `case nombre:` comparar directamente con el contenido de una variable anterior llamada `nombre`?
6. ¿Por qué no basta probar un divisor para afirmar que un número es primo?
7. ¿Qué ocurre al comparar la entrada de texto `"4"` con el entero `4`?
8. En un bucle de juego, ¿qué debes actualizar si la partida termina al perder?

**Respuestas:** 1) No; sí. 2) Diez; cero. 3) Cuatro. 4) Pierdes el total anterior. 5) No: un nombre simple captura el valor. 6) Puede existir otro divisor; encontrar uno exacto sí basta para descartar un número mayor que dos. 7) Son distintos: `"4" != 4` es verdadero. 8) El estado o condición de finalización; no debe depender solo de que gane el jugador.

## 17. Fuentes y qué estudiar después

### 17.1. Material integrado

- **Guía de clase:** [IFCD0062 Fundamentos programacion Python.pdf](<../../IFCD0062 Fundamentos programacion Python.pdf>), módulo 2, pp. 29–33. Las diapositivas son esquemáticas; las prácticas amplían el desarrollo.
- **Tus notas:** [modulo2.md](modulo2.md), junto con los comentarios, intentos y alternativas de los ejercicios 2-1 a 2-30 y el examen. Se ha conservado la numeración local para poder volver a tus archivos.
- **Condicionales:** [Ejemplo02_Condicionales.zip](../../Ejemplo02_Condicionales.zip).
- **Patrones:** [Ejemplo03_Match_Case.zip](../../Ejemplo03_Match_Case.zip), incluida la duda de captura y guardas de `password.py`.
- **Recorridos:** [Ejemplo04_Bucle_For.zip](../../Ejemplo04_Bucle_For.zip), incluidos los ejemplos de índices y Fibonacci.
- **Repetición:** [Ejemplo05_Bucle_While.zip](../../Ejemplo05_Bucle_While.zip), con menús, centinela, adivinación y juegos.
- **Continuidad:** [apuntes del módulo 1](../modulo1/modulo1.md).
- **Orientación del máster:** [MASTER-PERSONALIZADO-IA.md](../../../../MASTER-PERSONALIZADO-IA.md) y [ENCAJE-TECNOFOR-MASTER.md](../../../../ENCAJE-TECNOFOR-MASTER.md), consultados para mantener la conexión con tus objetivos.

### 17.2. Referencias oficiales para los matices

Consultadas como apoyo el 17 de noviembre de 2026. No son lectura obligatoria adicional. Las explicaciones y correcciones se construyen principalmente sobre tus prácticas y el material de clase.

- [PEP 8: indentación y espacios](https://peps.python.org/pep-0008/#indentation).
- [Tutorial: control de flujo](https://docs.python.org/es/3.14/tutorial/controlflow.html).
- [Referencia: patrones y guardas de match](https://docs.python.org/es/3.14/reference/compound_stmts.html#the-match-statement).
- [Tipos: valores de verdad y range](https://docs.python.org/es/3/library/stdtypes.html).
- [Funciones incorporadas: len, input y print](https://docs.python.org/es/3.14/library/functions.html).
- [Expresiones: prioridades y expresión condicional](https://docs.python.org/es/3.14/reference/expressions.html).
- [random: randint y simulaciones](https://docs.python.org/es/3.14/library/random.html).

### 17.3. Qué dejamos para después

| Tema | Cuándo encaja |
|---|---|
| Definir funciones, parámetros y `return` | Módulo 3: convertir bloques repetidos en piezas reutilizables. |
| Listas, tuplas, diccionarios y conjuntos en detalle | Módulo 3: aquí solo usamos lo necesario para recorrer e indexar. |
| Excepciones y recuperación de entradas no numéricas | Módulo 4: las validaciones actuales comprueban valores ya convertidos. |
| Módulos, importaciones y métodos de texto | Módulo 4: `random` se adelanta solo por su presencia en los ejercicios. |
| Clases y persistencia en archivos | Módulo 5 de la guía. |
| JSON, HTTP, APIs y reintentos reales | Puente del máster, tras funciones, colecciones y excepciones. |
| Comprensiones, generadores y algoritmos optimizados | Complementos posteriores, cuando aporten algo al proyecto. |

La prioridad ahora es poder seguir el estado de un programa, explicar por qué entra en una rama, saber cuántas veces repite y comprobar cómo termina.
