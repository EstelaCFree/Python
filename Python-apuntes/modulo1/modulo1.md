# Módulo 1 · Introducción a Python y a la programación

Apuntes integrados de la guía de Ana Isabel Vegas, los ejemplos de clase y tus ejercicios y comentarios. Revisión: 12 de noviembre de 2026.

**Alcance:** páginas 3–28 del PDF del curso. Los ejemplos usan Python 3. Los condicionales, bucles, funciones propias y excepciones se desarrollarán después.

**Cómo utilizarlos:** la teoría incluye ejemplos explicados y enlaces a tus archivos. Las notas **Aclaración** precisan lo visto en clase. Las **aplicaciones al máster** son complementos opcionales: no se presentan como contenido adicional del examen.

## Índice

1. [Python y su ejecución](#1-python-y-su-ejecución)
2. [Variables, expresiones y comentarios](#2-variables-expresiones-y-comentarios)
3. [Tipos de datos](#3-tipos-de-datos)
4. [Entradas y conversiones](#4-entradas-y-conversiones)
5. [Texto y salida por pantalla](#5-texto-y-salida-por-pantalla)
6. [Operadores aritméticos](#6-operadores-aritméticos)
7. [Porcentajes y decimales](#7-porcentajes-y-decimales)
8. [Asignación y actualización](#8-asignación-y-actualización)
9. [Comparaciones](#9-comparaciones)
10. [Operadores lógicos](#10-operadores-lógicos)
11. [Aprendizajes de tus ejercicios](#11-aprendizajes-de-tus-ejercicios)
12. [Aplicaciones a tu máster](#12-aplicaciones-a-tu-máster)
13. [Qué estudiar después](#13-qué-estudiar-después)
14. [Repaso y resultados de referencia](#14-repaso-y-resultados-de-referencia)
15. [Mapa de ejercicios y fuentes](#15-mapa-de-ejercicios-y-fuentes)

## 1. Python y su ejecución

### 1.1. Qué es Python

Python es un lenguaje de programación de propósito general creado por Guido van Rossum. Permite automatizar tareas, procesar datos y desarrollar aplicaciones, entre muchos otros usos.

| Característica de la guía | Qué significa en la práctica |
|---|---|
| Alto nivel | Podemos centrarnos en el problema sin gestionar manualmente detalles como la reserva de memoria. |
| Interpretado | Un intérprete ejecuta el programa; para estos ejercicios no compilamos manualmente un ejecutable. |
| Sintaxis legible | La estructura facilita la lectura; la indentación delimita bloques. |
| Propósito general | Sirve para problemas de áreas diferentes. |
| Multiplataforma | Está disponible para macOS, Windows y otros sistemas; algunas rutas y dependencias varían. |
| Código abierto | Se puede utilizar y consultar su código fuente. |
| Muchas bibliotecas | Hay herramientas preparadas para numerosas tareas. Algunas vienen incluidas y otras se instalan aparte. |
| Admite orientación a objetos | Permite trabajar con clases y objetos; lo estudiarás en el módulo 5. |

**Aclaración:** «interpretado» no significa que no exista compilación interna. Lo relevante ahora es que ejecutas el archivo `.py` con Python sin compilarlo manualmente. Python permite varios estilos de programación, no solo el orientado a objetos.

### 1.2. Intérprete, editor y terminal

- **Intérprete:** ejecuta el código Python.
- **Editor o entorno de desarrollo:** permite escribir, guardar y depurar. La guía menciona IDLE, Visual Studio Code, Jupyter, Spyder y PyCharm. Anaconda es una distribución que reúne herramientas y paquetes.
- **Terminal:** permite lanzar comandos, como el que ejecuta un archivo.

En la terminal del Mac, para comprobar la versión:

```bash
python3 --version
```

Estando situada en la carpeta `modulo1`, para ejecutar un ejercicio:

```bash
python3 ejercicio1.py
```

Estos comandos se escriben en la terminal, no dentro del archivo `.py`.

También puedes abrir el intérprete interactivo con `python3`. Su indicador suele ser `>>>`: permite probar expresiones sueltas. No copies esos símbolos a tus archivos.

### 1.3. Entrada → proceso → salida

El [ejercicio 5](ejercicio5.py) permite reconocer las tres partes:

```python
# ENTRADA: obtener los datos.
euros = float(input("Importe en euros: "))
dolares_por_euro = float(input("¿Cuántos dólares equivale un euro?: "))

# PROCESO: aplicar la fórmula.
dolares = euros * dolares_por_euro

# SALIDA: mostrar el resultado.
print(f"{euros:.2f} € equivalen a {dolares:.2f} dólares")
```

Con entradas `50` y `1.10`, muestra `55.00` dólares. El cambio lo introduces tú; el programa no consulta cotizaciones.

**Aprendizaje:** `dolares_por_euro` deja clara la unidad. Si el cambio estuviera en euros por dólar, necesitarías otra fórmula. Los nombres de las variables ayudan a evitar errores.

## 2. Variables, expresiones y comentarios

### 2.1. Asignar valores

Una variable es un nombre asociado a un valor. Utilizamos `=` para asignarlo:

```python
precio = 25.50
cantidad = 3
total = precio * cantidad
print(total)  # 76.5
```

En `total = precio * cantidad`, primero se calcula la derecha y después se asocia el resultado al nombre de la izquierda.

| Término | Ejemplo | Significado |
|---|---|---|
| Literal | `3`, `25.50`, `"Hola"` | Valor escrito directamente en el código. |
| Variable | `cantidad` | Nombre que permite acceder a un valor. |
| Expresión | `precio * cantidad` | Código que produce un valor al evaluarse. |
| Asignación | `total = precio * cantidad` | Asocia el resultado a una variable. |
| Llamada | `print(total)` | Ejecuta una función con unos argumentos. |
| Argumento | `total`, en esa llamada | Dato que pasamos a la función. |

No necesitas declarar previamente el tipo de la variable: se conoce por el objeto asignado. Una variable también puede asociarse después a un valor de otro tipo, aunque conviene evitar cambios que confundan.

**Aclaración a la guía:** el tipo no se identifica «al iterar» una variable. Python tiene **tipado dinámico**, pero no convierte automáticamente cualquier dato para operar: no suma directamente `"3"` y `2`.

### 2.2. Nombres de variables

- Pueden empezar por una letra o `_`; después pueden incluir números.
- No pueden contener espacios ni guiones como `precio-final`.
- Distinguen mayúsculas y minúsculas: `edad` y `Edad` son nombres diferentes.
- No pueden ser palabras reservadas, como `if`, `and` o `class`.
- Conviene usar nombres descriptivos con palabras separadas por `_`: `precio_final`.
- Evita usar `print`, `input`, `int`, `float` o `str` como variables: ocultarías las herramientas que tienen esos nombres.

Python admite letras como `ñ` en los identificadores. Para mantener un estilo uniforme y facilitar la compatibilidad puedes usar `contrasena` o `anyo_actual`.

### 2.3. Una asignación no crea una fórmula permanente

```python
precio = 10
total = precio * 2
precio = 15

print(precio)  # 15
print(total)   # 20
```

`total` conserva el resultado calculado en su asignación. No se recalcula automáticamente al cambiar `precio`. Habría que ejecutar de nuevo `total = precio * 2`.

Esta idea es clave para seguir los ejercicios de puntos, saldos y producción: cada línea usa los valores disponibles en ese momento.

### 2.4. Comentarios y comillas triples

Los comentarios empiezan por `#` y llegan hasta el final de la línea:

```python
# Calcular el importe de tres facturas.
facturas = 85 * 3  # Cada factura cuesta 85 euros.
```

Los enunciados entre tres comillas que aparecen en tus ejercicios son **cadenas de texto multilínea**. Cuando están al principio de un módulo, una función o una clase pueden actuar como documentación, llamada *docstring*. No son técnicamente comentarios de bloque, aunque se utilicen para guardar enunciados.

Para comentar varias líneas de código, lo habitual es poner `#` en cada una; el editor puede hacerlo de una vez.

## 3. Tipos de datos

### 3.1. Tipos básicos

| Tipo | Nombre en Python | Ejemplos | Uso en los ejercicios |
|---|---|---|---|
| Entero | `int` | `25`, `0`, `-3` | Edades, personas, unidades o segundos completos. |
| Punto flotante | `float` | `7.5`, `25.0`, `-2.3` | Precios y medidas. |
| Cadena de texto | `str` | `"Estela"`, `"25"`, `""` | Nombres, mensajes y entradas de teclado. |
| Booleano | `bool` | `True`, `False` | Resultados de comprobaciones. |
| Complejo | `complex` | `2 + 3j` | Números con parte imaginaria; fuera de la práctica de este módulo. |

**Aclaraciones:**

- El tipo es `bool`, en minúsculas. Sus valores son `True` y `False`, con inicial mayúscula.
- `"25"` es texto y `25` es un entero. Las comillas cambian el significado.
- Los decimales se escriben con punto en el código: `7.5`.
- `float` representa algunos decimales de forma aproximada; lo retomamos en el apartado 7.

Para consultar el tipo utilizamos `type()`, como hace la profesora en `tipos.py`:

```python
edad = 25
precio = 25.0
edad_escrita = "25"
resuelto = True

print(type(edad))          # <class 'int'>
print(type(precio))        # <class 'float'>
print(type(edad_escrita))  # <class 'str'>
print(type(resuelto))      # <class 'bool'>
```

**Otro detalle del ZIP:** `conversiones.py` muestra que, en operaciones numéricas, `True` se comporta como `1` y `False` como `0`: `8 + True` da `9` y `8 + False` da `8`. Para expresar condiciones sigue siendo más claro usar los booleanos como tales, sin sustituirlos por números.

### 3.2. Colecciones: reconocerlas ahora

La guía las presenta aquí y las desarrolla en el módulo 3. Ahora basta con identificar sus diferencias.

| Colección | Tipo | Ejemplo | Características básicas |
|---|---|---|---|
| Lista | `list` | `["Ana", "Luis", "Ana"]` | Mantiene el orden, admite repetidos y se puede modificar. |
| Tupla | `tuple` | `("Ana", 25)` | Mantiene el orden; sus posiciones no se pueden añadir, eliminar o reasignar. |
| Conjunto | `set` | `{"Ana", "Luis"}` | No tiene un orden de posiciones como una lista y no contiene duplicados. |
| Diccionario | `dict` | `{"nombre": "Ana", "edad": 25}` | Asocia claves únicas a valores; conserva el orden de inserción. |

«Ordenado» no significa «ordenado alfabéticamente»: se refiere a que conserva un orden de sus elementos.

**Aclaración:** un diccionario es una colección de pares clave–valor, no una lista. Un conjunto vacío se crea con `set()`; `{}` crea un diccionario vacío. Las operaciones detalladas se estudiarán después.

## 4. Entradas y conversiones

### 4.1. `input()` devuelve texto

```python
edad = input("Dime tu edad: ")
print(type(edad))  # <class 'str'>, aunque escribas 25.
```

La regla precisa es: **`input()` devuelve una cadena de texto**. Otros orígenes, como una API, pueden entregar números o booleanos; no hay que generalizarlo a toda entrada de un programa.

Si solo vas a mostrar la edad, puede quedarse como texto. Ocurre en tu [ejercicio 1](ejercicio1.py) y con el año de [examen.py](examen.py). Para hacer cálculos o comparaciones numéricas necesitarías convertirla.

### 4.2. Qué hace cada conversión

| Conversión | Ejemplo | Resultado |
|---|---|---|
| A entero | `int("25")` | `25` |
| A decimal | `float("25.5")` | `25.5` |
| A decimal desde entero | `float(25)` | `25.0` |
| A texto | `str(25)` | `"25"` |
| A entero desde decimal | `int(25.9)` | `25`, truncando hacia cero. |

La conversión devuelve un resultado; no cambia por sí sola la variable original:

```python
texto = "25"
numero = int(texto)

print(type(texto))   # <class 'str'>
print(type(numero))  # <class 'int'>
```

Podemos combinar lectura y conversión:

```python
personas = int(input("¿Cuántas personas sois?: "))
```

Primero se ejecuta la llamada interior: `input()` obtiene el texto; después `int()` lo convierte y `=` guarda el resultado.

### 4.3. Ejemplo: sumar dos entradas

Adaptación del [ejercicio 2](ejercicio2.py):

```python
numero1 = int(input("Primer número entero: "))
numero2 = int(input("Segundo número entero: "))

suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {suma}")
```

Con `3` y `4` muestra `7`. Si ambos datos se conservaran como texto, `"3" + "4"` daría `"34"`: `+` une las cadenas.

### 4.4. Errores y casos que engañan

| Expresión | Qué ocurre |
|---|---|
| `int("hola")` | `ValueError`: el texto no representa un entero. |
| `int("7.5")` | `ValueError`: el texto representa un decimal, no un entero. |
| `float("7,5")` | `ValueError`: esta conversión espera punto decimal. |
| `int(7.9)` | Devuelve `7`; no redondea a `8`. |
| `int(-7.9)` | Devuelve `-7`; trunca hacia cero. |
| `bool("False")` | Devuelve `True`, porque es una cadena no vacía. |

El último caso es una **ampliación útil para automatización**: `bool()` comprueba si un valor se considera verdadero; no interpreta la palabra escrita como un booleano. No sirve para convertir automáticamente respuestas de texto «sí/no» o «True/False».

No necesitas controlar todavía estos errores con `try/except`: las excepciones se desarrollan en el módulo 4. Ahora interesa entender su causa.

## 5. Texto y salida por pantalla

### 5.1. Comillas y caracteres especiales

Puedes usar comillas simples o dobles. Debes cerrar con el mismo tipo con el que has abierto.

| Escritura en una cadena | Qué representa |
|---|---|
| `\n` | Salto de línea. |
| `\t` | Tabulación horizontal. |
| `\\` | Una barra invertida. |
| `\'` | Una comilla simple. |
| `\"` | Una comilla doble. |

```python
print("Nombre:\tEstela\nCurso:\tPython")
print('Ella dijo: "Hola"')
print('It\'s Python')
print("Una barra invertida: \\")
```

Cambiar las comillas exteriores, como en el segundo ejemplo, permite evitar algunos escapes.

### 5.2. `print()`, `sep` y `end`

`print()` muestra información por pantalla. Puede recibir varios argumentos separados por comas:

```python
nombre = "Estela"
edad = 25

print("Hola", nombre, "tienes", edad, "años")
print("2026", "11", "12", sep="-")
print("Hola", end=" ")
print(nombre)
```

Salida:

```text
Hola Estela tienes 25 años
2026-11-12
Hola Estela
```

- `sep` indica qué se coloca **entre** los argumentos. Por defecto, un espacio: `" "`.
- `end` indica qué se coloca **al final** de la llamada. Por defecto, un salto de línea: `"\n"`.
- Son parámetros de `print()`, no operadores de Python.
- `print()` ya convierte los valores a texto para mostrarlos: no hace falta envolver cada número en `str()`.

**De tu ejercicio 1:** en `print("Bienvenide ", nombre)` el espacio final del texto se suma al separador de `print()`. Para evitar el doble espacio, escribe `print("Bienvenide", nombre)`.

### 5.3. Tres formas de construir un mensaje

Tu [ejercicio 1](ejercicio1.py) compara estas opciones:

```python
nombre = "Estela"
apellido = "Castro"
edad = "25"  # Solo se muestra; puede seguir siendo texto.

# 1. Concatenar cadenas con +.
print("Bienvenide, " + nombre + " " + apellido + ", con " + edad + " años")

# 2. Pasar varios argumentos a print().
print("Bienvenide,", nombre, apellido, "con", edad, "años")

# 3. Utilizar una f-string.
print(f"Bienvenide, {nombre} {apellido}, con {edad} años")
```

La **f-string** lleva una `f` delante de las comillas y evalúa las expresiones entre `{}`. Puedes incluir variables o cálculos:

```python
precio = 10
cantidad = 3
print(f"Total: {precio * cantidad} €")  # Total: 30 €
```

**Aprendizajes de tus comentarios:**

- El `str(...)` exterior de tu primera solución era innecesario: el contenido ya era texto.
- Si `edad` fuera un entero, la concatenación con `+` necesitaría `str(edad)`. Con comas o f-string puedes mostrarla directamente.
- Sin la `f`, `"Hola {nombre}"` imprime las llaves literalmente.
- Mostrar un dato no es lo mismo que devolverlo a otro código. Aquí `print()` lo muestra; `return` se estudiará con funciones.

## 6. Operadores aritméticos

### 6.1. Tabla de operaciones

| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `17 + 3` | `20` |
| `-` | Resta | `17 - 3` | `14` |
| `*` | Multiplicación | `17 * 3` | `51` |
| `/` | División | `17 / 3` | Aproximadamente `5.666666666666667`. |
| `//` | Cociente redondeado hacia abajo | `17 // 3` | `5` |
| `%` | Resto de la división | `17 % 3` | `2` |
| `**` | Potencia | `2 ** 3` | `8` |

El [ejercicio 2](ejercicio2.py) permite practicarlas todas. Puedes guardar cada resultado en una variable o calcularlo directamente dentro de `print()`.

**Diferencias importantes:**

- Con los números de estos ejercicios, `/` devuelve `float`, incluso en una división exacta: `10 / 2` da `5.0`.
- Con dos enteros, `//` devuelve un entero. Si participa un `float`, puede devolver algo como `5.0`.
- `//` no equivale siempre a quitar decimales con `int()`: `-7 // 2` da `-4`, mientras que `int(-7 / 2)` da `-3`.
- `/`, `//` y `%` con divisor cero producen `ZeroDivisionError`.
- Las potencias utilizan `**`. El símbolo `^` tiene otro significado.

### 6.2. Prioridad y paréntesis

Para los cálculos habituales de este módulo:

1. Los paréntesis agrupan lo que se calcula primero.
2. Después van las potencias.
3. Multiplicación, división, división entera y resto tienen el mismo nivel; se resuelven de izquierda a derecha.
4. Suma y resta van después, de izquierda a derecha.
5. La asignación guarda el resultado tras calcular la expresión de la derecha.

**Ejemplo 1 · Conversión de temperatura**, del [ejercicio 4](ejercicio4.py):

```python
celsius = float(input("Temperatura en grados Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
```

Con `20` °C da `68.00` °F. El código convierte **de Celsius a Fahrenheit**. La multiplicación y la división se hacen antes de sumar `32`.

**Ejemplo 2 · Cuenta compartida**, del [ejercicio 7](ejercicio7.py):

```python
cuenta = 60
propina = 6
personas = 3

pago_por_persona = (cuenta + propina) / personas
print(f"Cada persona paga {pago_por_persona:.2f} €")  # 22.00 €
```

Sin paréntesis, `cuenta + propina / personas` daría `62.0`: solo dividiría la propina. La fórmula debe representar lo que quieres repartir.

### 6.3. Ejemplo explicado: segundos → horas, minutos y segundos

Adaptación del [ejercicio 6](ejercicio6.py):

```python
segundos_totales = int(input("Cantidad de segundos: "))

horas = segundos_totales // 3600
resto = segundos_totales % 3600
minutos = resto // 60
segundos_finales = resto % 60

print(f"{horas} horas, {minutos} minutos y {segundos_finales} segundos")
```

Para una entrada de `3675`:

| Paso | Operación | Resultado | Interpretación |
|---|---|---|---|
| Horas | `3675 // 3600` | `1` | Cabe una hora completa. |
| Resto | `3675 % 3600` | `75` | Quedan 75 segundos tras separar esa hora. |
| Minutos | `75 // 60` | `1` | Cabe un minuto completo en el resto. |
| Segundos | `75 % 60` | `15` | Sobran 15 segundos. |

Tu solución con `(segundos % 3600) // 60` también es correcta. La variable `resto` evita repetir la expresión y permite seguir mejor el cálculo.

La profesora también propone reutilizar `resto` para guardar los segundos finales: la nueva asignación sustituye el valor anterior. Aquí usamos `segundos_finales` para que cada nombre conserve un significado claro.

Este ejemplo presupone una duración no negativa y expresada en segundos completos.

## 7. Porcentajes y decimales

### 7.1. Aplicar un porcentaje a su base

El 10 % de una cantidad se calcula multiplicándola por `10 / 100`, equivalente a `0.10`.

En el [ejercicio 3](ejercicio3.py) se descuenta primero y se calcula el IVA después. Es la regla del ejercicio; hay que identificar sobre qué importe se aplica cada porcentaje.

```python
precio_inicial = float(input("Precio del producto: "))

importe_descuento = precio_inicial * 0.10
precio_con_descuento = precio_inicial - importe_descuento
importe_iva = precio_con_descuento * 0.21
precio_final = precio_con_descuento + importe_iva

print(f"Precio inicial: {precio_inicial:.2f} €")
print(f"Importe del descuento: {importe_descuento:.2f} €")
print(f"Precio tras el descuento: {precio_con_descuento:.2f} €")
print(f"Importe del IVA: {importe_iva:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
```

Con precio inicial `100`:

| Concepto | Importe |
|---|---|
| Precio inicial | 100,00 € |
| Descuento: 10 % de 100 | 10,00 € |
| Precio tras el descuento | 90,00 € |
| IVA: 21 % de 90 | 18,90 € |
| Precio final | 108,90 € |

**Aclaración a tu ejercicio:** la línea con la etiqueta `"Descuento aplicado"` muestra `precio_dto`, el precio después del descuento. El importe descontado es la variable `descuento`. Son conceptos diferentes.

### 7.2. `int()`, `round()` y `:.2f`

| Herramienta | Ejemplo | Resultado | Qué hace |
|---|---|---|---|
| `int()` | `int(12.987)` | `12` | Convierte a entero truncando hacia cero. |
| `round()` sin segundo argumento | `round(12.987)` | `13` | Redondea al entero más cercano. |
| `round()` con decimales | `round(12.987, 2)` | `12.99` | Devuelve un número redondeado. |
| Formato `:.2f` | `f"{12.987:.2f}"` | `"12.99"` | Construye texto con dos decimales. |

```python
precio = 12.5

print(round(precio, 2))  # 12.5
print(f"{precio:.2f}")  # 12.50
print(precio)          # 12.5: el formato no ha cambiado la variable.
```

Para presentar importes con dos decimales utiliza `:.2f`. Para conservar el resultado de `round()`, debes asignarlo: `redondeado = round(precio, 2)`.

En la corrección del [ejercicio 10](ejercicio10.py) aparece `int(saldo)` para quitar decimales. Con esos datos el saldo es `1413.0`, así que no se pierden céntimos; con otros importes sí podrían perderse. Para mostrar dinero es más adecuado `f"{saldo:.2f}"`.

### 7.3. Dos matices útiles

**Empates:** `round()` no sigue siempre la regla escolar de «si termina en 5, subir». En un empate exacto elige el valor par: `round(2.5)` da `2` y `round(3.5)` da `4`.

**Precisión:** algunos decimales se almacenan como aproximaciones binarias. Por eso `0.1 + 0.2` puede mostrarse como `0.30000000000000004`. Dar formato mejora la presentación, pero no convierte el cálculo interno en aritmética decimal exacta.

**Para más adelante:** una aplicación con dinero real debe definir la representación de importes y las reglas de redondeo. Se puede trabajar con céntimos enteros o con `Decimal`; no necesitas aprender esa biblioteca ahora.

## 8. Asignación y actualización

### 8.1. Operadores de asignación compuesta

Para los números de estos ejercicios, abrevian una operación y su asignación:

| Abreviatura | Equivalente en estos ejemplos |
|---|---|
| `puntos += 25` | `puntos = puntos + 25` |
| `puntos -= 15` | `puntos = puntos - 15` |
| `puntos *= 2` | `puntos = puntos * 2` |
| `puntos /= 5` | `puntos = puntos / 5` |
| `puntos //= 5` | `puntos = puntos // 5` |
| `puntos %= 12` | `puntos = puntos % 12` |
| `puntos **= 2` | `puntos = puntos ** 2` |

La variable debe tener un valor previo. `puntos += 25` sin haber definido antes `puntos` produce un error.

**Ejemplo 1 · Puntos**, del [ejercicio 8](ejercicio8.py):

```python
puntos = 100
puntos += 25  # 125
puntos -= 15  # 110
puntos *= 2   # 220

print(f"Los puntos finales son {puntos}")
```

Cada operación parte del resultado anterior, no de los `100` iniciales.

**Ejemplo 2 · Saldo**, del [ejercicio 10](ejercicio10.py):

```python
saldo = 1250
saldo += 375
saldo -= 85 * 3
saldo += 200

retiro = saldo * 0.10
saldo -= retiro

print(f"Se retiran {retiro:.2f} €")
print(f"Saldo final: {saldo:.2f} €")
```

| Momento | Saldo |
|---|---|
| Inicio | 1.250 € |
| Transferencia | 1.625 € |
| Tres facturas de 85 € | 1.370 € |
| Bizum | 1.570 € |
| Retirada del 10 % de 1.570, es decir, 157 € | 1.413 € |

**Corrección de la profesora:** en `saldo -= 85 * 3`, primero se calcula `85 * 3` y después se resta del saldo. Los paréntesis serían válidos, pero no son necesarios.

### 8.2. Conservar o sustituir el dato original

En el [ejercicio 9](ejercicio9.py), `caramelos %= 5` guarda el resto, pero `caramelos` deja de contener los `47` originales. Si necesitas ambos datos, usa otra variable:

```python
caramelos = 47
por_persona = caramelos // 5
sobran = caramelos % 5

print(f"Cada persona recibe {por_persona} caramelos y sobran {sobran}")
print(f"Al principio había {caramelos} caramelos")
```

**Del ejercicio 11:** `/=` puede cambiar un entero a `float`. Aunque el resultado matemático sea 160, `produccion /= 5` guarda `160.0`: es el comportamiento de `/`.

## 9. Comparaciones

Los operadores relacionales comparan valores. Con los tipos básicos que usamos aquí, producen `True` o `False`.

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `>` | Mayor que | `7.5 > 5` | `True` |
| `<` | Menor que | `7.5 < 10` | `True` |
| `>=` | Mayor o igual que | `7.5 >= 7` | `True` |
| `<=` | Menor o igual que | `7.5 <= 5` | `False` |
| `==` | Igual que | `7.5 == 10` | `False` |
| `!=` | Distinto de | `7.5 != 5` | `True` |

**Ejemplo 1 · Notas**, de tu [ejercicio 12 bis](ejercicio12bis.py):

```python
nota = 7.5

print("¿La nota es superior a 5?", nota > 5)
print("¿La nota es igual o superior a 7?", nota >= 7)
print("¿La nota es inferior a 10?", nota < 10)
print("¿La nota es exactamente 10?", nota == 10)
print("¿La nota es distinta de 5?", nota != 5)
```

Resultados: `True`, `True`, `True`, `False`, `True`.

**Aprendizaje:** añadir la pregunta, como en la corrección de la profesora, ayuda a interpretar la salida. Es más claro que imprimir cinco booleanos aislados.

**Ejemplo 2 · Sueldos**, de los [ejercicios 12](ejercicio12.py) y [13](ejercicio13.py):

```python
empleado1 = 1800
empleado2 = 2100
empleado3 = 1800

print("¿El 1 cobra más que el 2?", empleado1 > empleado2)  # False
print("¿El 2 cobra más que el 3?", empleado2 > empleado3)  # True
print("¿El 1 y el 3 cobran lo mismo?", empleado1 == empleado3)  # True
```

### No confundir asignar con comparar

```python
nota = 7.5                   # Asignación.
es_sobresaliente = nota >= 9  # Guarda el resultado de una comparación.
print(nota == 10)            # Comparación; no modifica la nota.
```

En el código de tu compañera guardado en el ejercicio 15, escribir `usuario == "admin"` en una línea suelta no cambia el usuario ni muestra nada al ejecutar un archivo `.py`.

**Aclaración:** `"10"` y `10` no son iguales. Entre cadenas, `"10" < "2"` da `True` por el orden de sus caracteres. Para comparar cantidades, conviértelas a números.

## 10. Operadores lógicos

### 10.1. Combinar condiciones

| Operador | Lectura | Cuándo se cumple |
|---|---|---|
| `and` | Y | Se cumplen ambas condiciones. |
| `or` | O | Se cumple al menos una, incluidas las dos a la vez. |
| `not` | No | Invierte el valor lógico. |

Tabla para condiciones booleanas:

| A | B | `A and B` | `A or B` |
|---|---|---|---|
| `True` | `True` | `True` | `True` |
| `True` | `False` | `False` | `True` |
| `False` | `True` | `False` | `True` |
| `False` | `False` | `False` | `False` |

Además, `not True` es `False` y `not False` es `True`.

**Matiz:** al combinar comparaciones obtienes booleanos. `and` y `or` también pueden operar con otros valores y devolver uno de sus operandos; no convierten siempre cualquier resultado a `bool`.

### 10.2. Ejemplo 1 · Intervalos de edad

Del [ejercicio 14](ejercicio14.py):

```python
edad = 25

print("Tiene entre 12 y 65:", edad >= 12 and edad <= 65)  # True
print("Tiene menos de 12 o más de 65:", edad < 12 or edad > 65)  # False
print("No tiene 18 años:", not (edad == 18))  # True
print("Tiene más de 18 y menos de 30:", edad > 18 and edad < 30)  # True
```

**Aprendizajes:**

- `>= 12` y `<= 65` incluyen a quienes tienen exactamente 12 o 65 años.
- `> 18` y `< 30` excluyen a quienes tienen exactamente 18 o 30 años.
- `not (edad == 18)` también puede escribirse `edad != 18`.
- Python permite encadenar comparaciones: `12 <= edad <= 65` equivale a la primera condición.

Para estar dentro de ese intervalo utilizamos `and`; para estar por debajo o por encima, `or`. La expresión `edad >= 12 or edad <= 65` no sirve para delimitarlo: basta con cumplir uno de sus lados, incluso estando fuera del intervalo.

### 10.3. Ejemplo 2 · Comprobar credenciales

Del [ejercicio 15](ejercicio15.py):

```python
usuario = input("Introduce el usuario: ")
contrasena = input("Introduce la contraseña: ")

credenciales_validas = usuario == "admin" and contrasena == "python123"
print("¿Las credenciales coinciden?", credenciales_validas)
```

Deben cumplirse ambas comparaciones. Con `or` bastaría acertar solo el usuario o solo la contraseña. La comparación distingue mayúsculas: `"Admin"` no es igual que `"admin"`.

**De tus comentarios:** para introducir la contraseña sin mostrar normalmente lo tecleado en una terminal, la profesora utiliza:

```python
import getpass

contrasena = getpass.getpass("Introduce la contraseña: ")
```

Es una ampliación puntual del material; `import` se explicará con módulos. Algunos entornos no admiten la entrada oculta y pueden mostrar un aviso. Este ejercicio practica comparaciones, no implementa un sistema de autenticación para una aplicación real.

El `if/else` guardado de tu compañera corresponde al módulo 2. Entonces aprenderás a tomar una decisión a partir del booleano; ahora lo calculamos y lo mostramos.

### 10.4. Prioridad y cortocircuito

El orden habitual entre los operadores de este módulo es: aritmética → comparaciones → `not` → `and` → `or`. Los paréntesis ayudan a expresar la intención.

**Aclaración útil:** `and` deja de evaluar al encontrar una parte falsa y `or` al encontrar una verdadera. Se llama evaluación en cortocircuito.

```python
personas = 0
cuenta = 60

reparto_asequible = personas > 0 and cuenta / personas <= 25
print(reparto_asequible)  # False; no llega a dividir entre cero.
```

El orden importa: se comprueba primero `personas > 0`. Es una forma de entender cómo se evalúan expresiones; no necesitas introducir este patrón en todos los ejercicios.

## 11. Aprendizajes de tus ejercicios

Esta tabla reúne detalles repartidos entre enunciados, comentarios y versiones alternativas. Las aclaraciones se incorporan a los apuntes; los archivos `.py` originales se conservan.

| Archivo | Observación | Qué aprender de ella |
|---|---|---|
| [ejercicio1.py](ejercicio1.py) | Sobra el `str(...)` exterior de la concatenación. | Antes de convertir, identifica el tipo y para qué necesitas el dato. |
| [ejercicio2.py](ejercicio2.py) | Guardas resultados y también calculas dentro de f-strings. | Ambas opciones son válidas. La variable intermedia ayuda si reutilizas el dato. El segundo número no puede ser cero para las divisiones y el resto. |
| [ejercicio3.py](ejercicio3.py) | «Descuento aplicado» muestra el precio rebajado. | Diferencia importe descontado, precio rebajado e impuesto. |
| [ejercicio4.py](ejercicio4.py) | La primera línea dice Fahrenheit → centígrados, pero la fórmula hace Celsius → Fahrenheit. | Comprueba dirección y unidades. El código coincide con la versión del ZIP. |
| [ejercicio5.py](ejercicio5.py) | La multiplicación presupone dólares por euro. | La unidad del cambio decide la fórmula. |
| [ejercicio6.py](ejercicio6.py) | Tu fórmula y la solución con `resto` son correctas. | Una variable intermedia puede hacer más legible la solución. |
| [ejercicio7.py](ejercicio7.py) | La propina es un importe, no un porcentaje. | «6 €» y «6 %» requieren cálculos distintos. Las personas deben ser un número positivo. |
| [ejercicio8.py](ejercicio8.py) | Actualización sucesiva de puntos. | Cada línea parte del resultado anterior. |
| [ejercicio9.py](ejercicio9.py) | `%=` sustituye la cantidad inicial por el resto. | Guarda el original si lo necesitarás después. |
| [ejercicio10.py](ejercicio10.py) | Hay dos versiones completas y una salida con `int(saldo)`. | Al ejecutar salen ambas versiones. `int()` trunca; para mostrar dinero utiliza formato decimal. |
| [ejercicio11.py](ejercicio11.py) | Tu enunciado dice «aumenta en 75», pero el código suma 125 y resta 75. | El ZIP confirma los dos pasos: +125 y −75. Tu código sigue esa versión. |
| [ejercicio12.py](ejercicio12.py) y [ejercicio13.py](ejercicio13.py) | Ambos comparan sueldos. | Practican el mismo concepto. |
| [ejercicio12bis.py](ejercicio12bis.py) | Las notas son el ejercicio 12 en el ZIP. | La numeración local no siempre coincide con la de la profesora. |
| [ejercicio14.py](ejercicio14.py) | Intervalos y negación. | Revisa límites incluidos/excluidos y si corresponde `and` u `or`. |
| [ejercicio15.py](ejercicio15.py) | Mezcla solución del módulo, propuesta con `if` y nota de `getpass`. | Distingue comprobar, actuar según el resultado y ocultar la entrada. |
| [examen.py](examen.py) | Lee empresa y año para dar un saludo. | Si el año solo se muestra, puede seguir siendo texto. Este archivo no permite deducir el examen completo. |

### Comprobación del ejercicio 11

La secuencia del ZIP resuelve la discrepancia del enunciado:

```python
produccion = 350
produccion += 125  # 475
produccion -= 75   # 400
produccion *= 2    # 800
produccion /= 5    # 160.0
sobran = produccion % 12  # 4.0

print(f"Sobran {int(sobran)} unidades")
```

`int(sobran)` presenta aquí un resultado que ya es matemáticamente entero. No debe emplearse como arreglo automático si aparecieran fracciones de producto: primero habría que comprobar si las operaciones tienen sentido.

### Cómo revisar un ejercicio

1. Identifica entradas y unidades.
2. Decide qué datos son texto, enteros o decimales.
3. Expresa la fórmula o condición con palabras.
4. Ejecuta un caso que puedas resolver a mano.
5. Comprueba que cada etiqueta describe el dato mostrado.
6. Anota restricciones: personas positivas, divisor distinto de cero, duración no negativa, etc.

Prueba también límites: 0 y 60 segundos; 12 y 65 años. Ahora basta con entender qué ocurriría con una entrada inválida; aprenderás a gestionarla después.

## 12. Aplicaciones a tu máster

**Complemento opcional.** Este módulo de Python contribuye sobre todo a las bases del **módulo 3 del máster: «APIs, webhooks y Python práctico»**. Las numeraciones de los programas no coinciden.

El plan actual y el informe de encaje de TecnoFor proponen aprovechar esta formación como base de Python y complementarla con integraciones, sin repetir otro curso de iniciación.

### 12.1. Qué merece especial atención para ti

| Base de Python | Por qué te interesa | Relación con el máster |
|---|---|---|
| Tipos y conversiones | Evitar sumar texto o interpretar `"False"` como si fuera `False`. | Transformación y validación de datos. |
| Asignaciones y cambios de estado | Leer el código generado por IA y detectar si sobrescribe información necesaria. | Automatización y estado de agentes. |
| Fórmulas, nombres y unidades | Comprobar tiempos, presupuestos y costes con cálculos explícitos. | Discovery, ROI y economía de tokens. |
| Comparaciones y lógica | Expresar requisitos, límites y condiciones de parada comprobables. | Workflows, harnessing y supervisión. |
| Mensajes claros y f-strings | Preparar informes y primeras trazas interpretables. | Observabilidad básica. |
| Casos de referencia y límites | Detectar cuándo un cambio hace fallar algo que funcionaba. | Fiabilidad y regresiones. |
| Listas y diccionarios | Preparar el trabajo con registros y respuestas estructuradas. | APIs, JSON y herramientas de agentes. |

La utilidad inmediata está en poder **leer, explicar y corregir expresiones pequeñas**. No necesitas todavía una biblioteca de agentes.

### 12.2. Miniaplicación 1 · Estimar coste por tokens

Solo usa variables, operaciones y formato. **Las tarifas son ficticias**, expresadas en euros por millón de tokens. Es una estimación local: no llama a servicios ni genera cargos.

```python
tokens_entrada = 1200
tokens_salida = 300
euros_por_millon_entrada = 0.50
euros_por_millon_salida = 2.00
numero_llamadas = 1000

coste_entrada = tokens_entrada * euros_por_millon_entrada / 1_000_000
coste_salida = tokens_salida * euros_por_millon_salida / 1_000_000
coste_por_llamada = coste_entrada + coste_salida
coste_total = coste_por_llamada * numero_llamadas

print(f"Coste estimado por llamada: {coste_por_llamada:.6f} €")
print(f"Coste estimado de {numero_llamadas} llamadas: {coste_total:.2f} €")
```

Salida: `0.001200 €` por llamada y `1.20 €` por 1.000 llamadas.

**Qué conecta con el módulo:**

- Contadores enteros y tarifas decimales.
- División entre un millón para convertir la unidad de tarifa.
- Los guiones bajos de `1_000_000` solo facilitan la lectura del número.
- Con `:.2f`, cada llamada aparecería como `0.00 €`: un formato inadecuado puede ocultar un coste pequeño pero acumulable.

El modelo supone las mismas cantidades en todas las llamadas. El bloque A del máster añadirá consumo medido, reintentos, caché y reglas de facturación. Para inferencia puramente local este precio externo por token no representa el coste operativo.

### 12.3. Miniaplicación 2 · Comprobar requisitos antes de continuar

Calculamos una regla sin ejecutar acciones externas:

```python
datos_completos = True
aprobacion_humana = False
coste_estimado = 0.03
limite_coste = 0.05

puede_continuar = (
    datos_completos
    and aprobacion_humana
    and coste_estimado <= limite_coste
)

print("¿Se cumplen los requisitos para continuar?", puede_continuar)
```

Da `False`: falta aprobación aunque el coste esté dentro del límite. Los paréntesis permiten repartir una expresión larga entre líneas.

Es una regla con datos ficticios. En un sistema real, una variable por sí sola no acredita una aprobación: habrá que obtenerla de una fuente válida y comprobarla donde se ejecuta la acción. Los condicionales del módulo 2 permitirán empezar a actuar según el resultado.

**Prioridad de estudio para ti:** tipos y conversiones → asignaciones → comparaciones y lógica → fórmulas y unidades → presentación. Las colecciones merecerán especial atención cuando se desarrollen, porque sustentan gran parte de las integraciones.

## 13. Qué estudiar después

La distribución procede del PDF completo. Permite ampliar con criterio sin intentar aprender todo Python en este módulo.

| Tema | Dónde aparece | Qué hacer ahora |
|---|---|---|
| Bloques e indentación | Módulo 2, p. 30 | Saber que tienen significado. La convención habitual es usar cuatro espacios por nivel; el editor puede insertarlos al pulsar Tab. |
| `if`, `elif`, `else` | Módulo 2, p. 31 | Entender los booleanos que usarán como condiciones. |
| `for` y `while` | Módulo 2, pp. 32–33 | Posponer la repetición de tareas. |
| `match/case` | ZIP 03 y tus apuntes del módulo 2; sin diapositiva propia en la guía | Mantenerlo en ese módulo, sin suponerlo parte del examen del 1. |
| Funciones y `return` | Módulo 3, pp. 35–37 | Usar funciones disponibles; posponer la definición de funciones propias. |
| Listas, tuplas, conjuntos y diccionarios | Módulo 3, pp. 38–43 | Reconocer sus formas y diferencias. |
| Excepciones y `try/except` | Módulo 4, pp. 45–49 | Identificar por qué fallan entradas, sin gestionar aún la recuperación. |
| Módulos, importaciones y `pip` | Módulo 4, pp. 50–52 | Saber que `getpass` es importado; estos ejemplos no requieren instalar paquetes. |
| Métodos de texto y otras funciones | Módulo 4, pp. 53–67 | Posponer la limpieza detallada. `len()` ya aparece en tus ejercicios del módulo 2. |
| Clases, objetos y herencia | Módulo 5, pp. 69–79 | Reconocer que existen. No son necesarios para estos ejercicios. |
| Archivos | Módulo 5, pp. 80–83 | Posponer lectura, escritura y persistencia. |

### Complementos para automatización e IA

El PDF no desarrolla explícitamente estos temas. No significa que la profesora no pueda mencionarlos después; significa que no conviene darlos por cubiertos por esta guía.

| Complemento | Para qué servirá | Cuándo incorporarlo |
|---|---|---|
| JSON y validación de estructuras | Interpretar respuestas de servicios y salidas de herramientas o modelos. | Tras listas, diccionarios y funciones. |
| HTTP, APIs, autenticación y webhooks | Conectar sistemas sin depender de un nodo preparado de n8n. | Después de funciones, importaciones y excepciones. |
| Timeouts, reintentos, paginación e idempotencia | Evitar bloqueos, datos perdidos o acciones duplicadas. | En el puente de integraciones del módulo 3 del máster. |
| Entornos virtuales y dependencias | Ejecutar proyectos sin mezclar paquetes. | Cuando utilices bibliotecas externas. |
| Pruebas automatizadas y registros | Detectar regresiones y explicar qué ocurrió. | Después de funciones; ahora practica resultados esperados y salidas claras. |
| Dinero y reglas de redondeo | Evitar pérdidas de precisión y aplicar criterios consistentes. | Cuando un proyecto gestione importes reales. |

No hace falta añadir ahora pandas, NumPy, frameworks de agentes o entrenamiento de redes. El siguiente puente útil para tu objetivo será transformar datos y comunicar programas mediante APIs. Las bibliotecas se elegirán según un problema concreto.

## 14. Repaso y resultados de referencia

### 14.1. Lo que deberías poder explicar sin copiar

- Qué hace el intérprete y cómo se ejecuta un `.py`.
- Qué diferencia hay entre `=` y `==`.
- Por qué `"3" + "4"` da `"34"` y `3 + 4` da `7`.
- Cuándo conservar una entrada como texto y cuándo convertirla.
- Cómo mostrar valores con comas, concatenación y f-strings.
- Qué diferencia hay entre `/`, `//` y `%`.
- Qué valores se usan en una actualización con `+=`, `-=` o `*=`.
- Qué diferencia hay entre descuento, precio rebajado e impuesto.
- Qué hacen `int()`, `round()` y `:.2f`.
- Cómo combinar condiciones y cómo incluir o excluir los extremos de un intervalo.

### 14.2. Errores frecuentes

| Síntoma | Posible causa | Qué revisar |
|---|---|---|
| Sale `34` en vez de `7` | Se han unido cadenas. | Conversión de `input()`. |
| `TypeError` al unir texto y número | `+` entre tipos incompatibles. | `str()`, comas o f-string. |
| `ValueError` en una conversión | Formato no convertible. | Texto recibido, punto decimal y tipo esperado. |
| `ZeroDivisionError` | Divisor cero. | Segundo número o personas. |
| `NameError` | Nombre inexistente. | Ortografía, mayúsculas y asignación previa. |
| Se imprime `{nombre}` | Falta la `f`. | Cadena del mensaje. |
| Espacios duplicados | Espacio del texto más separador de `print()`. | Literales y `sep`. |
| Desaparecen céntimos | `int()` para presentar dinero. | Formato decimal. |
| La condición admite edades indebidas | `or` para un intervalo interior o límites incorrectos. | Requisito expresado con palabras. |
| Un importe tiene una etiqueta equivocada | Se confunden descuento y precio rebajado. | Significado de variable y mensaje. |
| Un resultado no cambia al cambiar otro dato | Se esperaba recálculo automático. | Volver a ejecutar la fórmula. |

### 14.3. Resultados para comprobarte

Puedes ocultar la última columna y calcular antes de ejecutar.

| Práctica | Datos | Resultado esperado |
|---|---|---|
| Operaciones, ejercicio 2 | `17` y `3` | Suma 20; resta 14; producto 51; división ≈ 5.6667; cociente 5; resto 2; potencia 4913. |
| Descuento e IVA, ejercicio 3 | Precio 100 | Descuento 10; precio rebajado 90; IVA 18.90; total 108.90. |
| Temperatura, ejercicio 4 | 20 °C | 68.00 °F. |
| Duración, ejercicio 6 | 3675 segundos | 1 hora, 1 minuto y 15 segundos. |
| Cuenta, ejercicio 7 | Cuenta 60; propina 6; personas 3 | 22.00 € por persona. |
| Puntos, ejercicio 8 | 100; +25; −15; ×2 | 220. |
| Caramelos, ejercicio 9 | 47 entre 5 | 9 por persona y 2 sobrantes. |
| Saldo, ejercicio 10 | Datos del enunciado | Retiro 157; saldo final 1413. |
| Producción, ejercicio 11 | +125; −75; ×2; ÷5 | 160 antes de agrupar; sobran 4 en lotes de 12. |
| Intervalo, ejercicio 14 | Edades 12 y 65 | Ambos extremos cumplen `12 <= edad <= 65`. |

Estos resultados ayudan a estudiar el material disponible; no predicen las preguntas del examen.

## 15. Mapa de ejercicios y fuentes

### 15.1. Qué repasar según el tema

| Tema | Archivos |
|---|---|
| Entrada de texto y mensajes | [ejercicio1.py](ejercicio1.py), [examen.py](examen.py) |
| Enteros y operaciones | [ejercicio2.py](ejercicio2.py) |
| Porcentajes y decimales | [ejercicio3.py](ejercicio3.py) |
| Fórmulas y unidades | [ejercicio4.py](ejercicio4.py), [ejercicio5.py](ejercicio5.py), [ejercicio7.py](ejercicio7.py) |
| Cociente y resto | [ejercicio6.py](ejercicio6.py), [ejercicio9.py](ejercicio9.py) |
| Asignación compuesta | [ejercicio8.py](ejercicio8.py), [ejercicio9.py](ejercicio9.py), [ejercicio10.py](ejercicio10.py), [ejercicio11.py](ejercicio11.py) |
| Comparaciones | [ejercicio12.py](ejercicio12.py), [ejercicio12bis.py](ejercicio12bis.py), [ejercicio13.py](ejercicio13.py) |
| Lógica | [ejercicio14.py](ejercicio14.py), [ejercicio15.py](ejercicio15.py) |

### 15.2. Material integrado

- **Guía de clase:** [IFCD0062 Fundamentos programacion Python.pdf](<../../IFCD0062 Fundamentos programacion Python.pdf>). Módulo 1: pp. 3–28; se ha consultado el resto para delimitar ampliaciones.
- **Ejemplos de la profesora:** [Ejemplo01_Tipos_Datos.zip](../../Ejemplo01_Tipos_Datos.zip), incluidos `tipos.py`, `conversiones.py` y los ejercicios 1–15.
- **Trabajo propio:** `modulo1.md` original, los ejercicios de esta carpeta, `ejercicio12bis.py`, `examen.py`, comentarios y correcciones anotadas.
- **Orientación del máster:** [MASTER-PERSONALIZADO-IA.md](../../../../MASTER-PERSONALIZADO-IA.md) y [ENCAJE-TECNOFOR-MASTER.md](../../../../ENCAJE-TECNOFOR-MASTER.md), versiones locales consultadas.

### 15.3. Referencias oficiales para consultar matices

No son lectura adicional obligatoria:

- [Introducción: números, texto y variables](https://docs.python.org/es/3/tutorial/introduction.html).
- [Funciones incorporadas: conversiones, entradas, salidas y redondeo](https://docs.python.org/es/3/library/functions.html).
- [Expresiones, comparaciones, lógica y prioridades](https://docs.python.org/es/3/reference/expressions.html).
- [Estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html).
- [Punto flotante y sus limitaciones](https://docs.python.org/es/3/tutorial/floatingpoint.html).
- [`getpass`: lectura de contraseñas](https://docs.python.org/es/3/library/getpass.html).
