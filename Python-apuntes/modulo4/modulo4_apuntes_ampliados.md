# Módulo 4 · Excepciones, módulos y manejo de texto

Apuntes integrados de la guía de Ana Isabel Vegas, los ejemplos 11–13, tus ejercicios y comentarios y las explicaciones de recuperación de clase. Actualización: 25 de noviembre de 2026.

**Alcance:** módulo 4 del PDF: portada en p. 44, excepciones en pp. 45–49, módulos en pp. 50–51, pip en p. 52 y texto en pp. 53–67. El módulo 5 comienza en p. 68. Se integran los 14 archivos Python de los ZIP 11–13 disponibles en esta revisión; los ejemplos de la biblioteca estándar amplían las diapositivas de módulos.

**Estado:** versión ampliada del material disponible. Se podrá actualizar si la profesora añade prácticas. El documento incluye explicaciones, ejemplos resueltos, resultados de referencia y aplicaciones opcionales a automatización y al pipeline editorial.

**Cómo leerlo:** **Aclaración** precisa una idea de clase; **Corrección** identifica una discrepancia del material; **Complemento opcional** conecta con tus proyectos o prepara un siguiente paso. No se presupone qué se explicó oralmente ni qué preguntas habrá en el examen.

Se conservan [modulo4.md](modulo4.md) y tus cuatro ejercicios originales. Los bloques Python son ejemplos completos para ejecutar por separado, salvo la pareja `operaciones.py` y `calculadora.py`, que se identifica expresamente como dos archivos relacionados. Los comandos de terminal se muestran como instrucciones de consulta: no forman parte de un archivo `.py`.

## Índice

1. [Errores, excepciones y sus tipos](#1-errores-excepciones-y-sus-tipos)
2. [Capturar con try y except](#2-capturar-con-try-y-except)
3. [Qué hacen else y finally](#3-qué-hacen-else-y-finally)
4. [Múltiples capturas y procesamiento de listas](#4-múltiples-capturas-y-procesamiento-de-listas)
5. [Lanzar una excepción con raise](#5-lanzar-una-excepción-con-raise)
6. [Saldo y variables globales](#6-saldo-y-variables-globales)
7. [Adivinar un número y recuperar entradas](#7-adivinar-un-número-y-recuperar-entradas)
8. [Crear y utilizar módulos propios](#8-crear-y-utilizar-módulos-propios)
9. [Paquetes, biblioteca estándar y pip](#9-paquetes-biblioteca-estándar-y-pip)
10. [Matemáticas con math](#10-matemáticas-con-math)
11. [Fechas y horas con datetime](#11-fechas-y-horas-con-datetime)
12. [Calendarios y configuración regional](#12-calendarios-y-configuración-regional)
13. [Selecciones con random](#13-selecciones-con-random)
14. [Cadenas y métodos: cómo conservar los resultados](#14-cadenas-y-métodos-cómo-conservar-los-resultados)
15. [Cambiar y comprobar mayúsculas, letras y dígitos](#15-cambiar-y-comprobar-mayúsculas-letras-y-dígitos)
16. [Limpiar extremos, separar y unir](#16-limpiar-extremos-separar-y-unir)
17. [Sustituir, buscar y contar](#17-sustituir-buscar-y-contar)
18. [Caracteres, orden y funciones incorporadas](#18-caracteres-orden-y-funciones-incorporadas)
19. [Ejercicio completo de Java y Python](#19-ejercicio-completo-de-java-y-python)
20. [Aplicaciones a tus proyectos](#20-aplicaciones-a-tus-proyectos)
21. [Repaso, correcciones y fuentes](#21-repaso-correcciones-y-fuentes)

## Parte I · Excepciones

## 1. Errores, excepciones y sus tipos

Una instrucción puede estar bien escrita y fallar al ejecutarse. Por ejemplo, `int("dos")` no puede convertir ese texto a entero y dividir entre cero no produce un cociente válido. Python comunica estos problemas mediante **excepciones**.

Si no se captura una excepción, normalmente se interrumpe la ejecución y se muestra un traceback: el recorrido de llamadas y líneas que llevó hasta el fallo. Gestionar una excepción permite decidir si pedir otro dato, saltar un registro, explicar el problema o dejar que el error llegue a otra parte del programa.

**Manejar no equivale a impedir que ocurra.** Puedes comprobar previamente que un divisor no sea cero; también puedes intentar dividir y reaccionar si se lanza la excepción. Cada forma tiene su contexto.

### 1.1. Sintaxis, ejecución y lógica

| Tipo de problema | Ejemplo | Qué necesitas hacer |
|---|---|---|
| Sintaxis | Falta `:` después de `if`. | Corregir el código para que pueda interpretarse. |
| Excepción en ejecución | `int("dos")`. | Corregir la entrada o gestionar el fallo según el objetivo. |
| Error lógico | Aplicar un descuento equivocado sin que Python se queje. | Comprobar reglas y resultados esperados. |

Un `try` dentro de un archivo no arregla una sintaxis incorrecta que impide interpretar ese mismo archivo. Tampoco descubre automáticamente errores de cálculo o requisitos mal expresados.

### 1.2. Tipos que aparecen o ayudan a entender estos ejemplos

| Excepción | Situación habitual |
|---|---|
| `ValueError` | Se recibe un valor no válido para una operación: `int("dos")`. |
| `ZeroDivisionError` | División entre cero. |
| `TypeError` | Se utiliza un tipo incompatible, como sumar un número y una lista. |
| `IndexError` | Índice fuera de una secuencia. |
| `KeyError` | Clave ausente al acceder directamente a un diccionario. |
| `NameError` | Nombre que no está definido en ese contexto. |
| `UnboundLocalError` | Se intenta leer una variable local antes de asignarla; aparece al estudiar el saldo. |
| `ModuleNotFoundError` | Python no encuentra un módulo que se intenta importar. |

La guía cita familias como `ArithmeticError`, `LookupError` y `BufferError`. Para estas prácticas, céntrate en los errores concretos: `ZeroDivisionError` pertenece a la familia aritmética; `IndexError` y `KeyError`, a la de búsqueda.

**Aclaración a la guía:** `Exception` es la base de muchas excepciones habituales, pero no de absolutamente todas. Por encima está `BaseException`; interrupciones como `KeyboardInterrupt` y `SystemExit` tienen otro tratamiento. No necesitas crear una jerarquía propia para resolver estos ejercicios.

## 2. Capturar con try y except

`try` contiene instrucciones que pueden fallar. Un `except` indica qué hacer si aparece un tipo determinado de excepción.

```python
try:
    numero = int(input("Introduce un entero: "))
except ValueError:
    print("Ese texto no representa un entero válido")
```

Si introduces `7`, la conversión termina normalmente. Si introduces `siete`, se ejecuta el mensaje. No se vuelve a preguntar automáticamente: para repetir necesitas un bucle, como veremos en el juego.

Cuando falla una instrucción del `try`, se omite lo que quedaba de ese bloque y se busca una captura compatible. Una vez atendido el error, el programa continúa después de la estructura; no regresa por sí solo a la línea que falló.

### 2.1. Recoger el objeto del error

```python
try:
    numero = int(input("Introduce un entero: "))
except ValueError as error:
    print("El valor introducido no es numérico")
    print("Tipo:", type(error))
    print("Detalle:", error)
```

`as error` da un nombre al objeto de excepción dentro de ese manejador. `error` puede llamarse `ex`, `fallo` u otro nombre. Mostrar su detalle no es obligatorio; depende del mensaje que necesite quien utiliza el programa.

`type(error)` muestra su clase. No es lo mismo el tipo del error que el tipo del dato que estabas intentando procesar.

### 2.2. Orden de capturas y captura genérica

Las capturas se revisan en orden y se ejecuta la primera compatible. Si incluyes una muy amplia antes de las concretas, puede absorber errores que querías distinguir.

**Corrección de tus notas:** no es obligatorio poner siempre una captura genérica al final. Puedes capturar únicamente los errores esperados y dejar que otros se propaguen para poder identificarlos.

| Forma | Alcance |
|---|---|
| `except ValueError:` | Ese tipo de error y sus subtipos. |
| `except Exception as error:` | Muchas excepciones habituales. |
| `except:` | Captura más ampliamente, incluidas interrupciones como `KeyboardInterrupt`. |

Los ejemplos originales utilizan a veces `except:` para enseñar una captura general. En las versiones ampliadas se prefieren errores concretos y se añade `except Exception` solo cuando tiene sentido una alternativa general. Una captura amplia no debe convertir cualquier fallo en un mensaje de éxito.

## 3. Qué hacen else y finally

**Fuentes:** `Ejemplo11_Excepciones/errores.py` y tu [ejercicio4-1.py](ejercicio4-1.py).

```python
try:
    numero1 = int(input("Introduce dividendo: "))
    numero2 = int(input("Introduce divisor: "))
    division = numero1 / numero2
except ValueError as error:
    print("El valor introducido no es numérico:", error)
except ZeroDivisionError as error:
    print("No se puede dividir por cero:", error)
else:
    print("Resultado:", division)
finally:
    print("***** FIN *****")
```

| Bloque | Cuándo interviene |
|---|---|
| `try` | Se intenta ejecutar su contenido. |
| `except` | Si aparece una excepción compatible en el `try`. |
| `else` | Si el `try` llega al final sin una excepción. |
| `finally` | Al salir de la estructura por el flujo habitual o de excepciones, haya o no error. |

### 3.1. Seguir tres casos

| Entradas | Recorrido | Salida relevante |
|---|---|---|
| `8`, `2` | try → else → finally | Resultado 4.0 y FIN. |
| `8`, `0` | try → except de división → finally | Mensaje de división y FIN. |
| `dos` | try → except de conversión → finally | Mensaje de conversión y FIN; no se pide el segundo dato. |

El resultado se muestra en `else` porque solo existe si el cálculo ha salido bien. Mostrarlo indiscriminadamente después de un error podría utilizar una variable sin asignar o un resultado anterior.

### 3.2. Matices importantes

- `else` no es un segundo bloque de captura: si algo falla dentro del propio `else`, no lo gestionan los `except` anteriores de esa estructura.
- `finally` también se ejecuta si una excepción no ha sido atendida y va a propagarse. No significa que esa excepción desaparezca.
- `finally` no es obligatorio. Para el ejercicio de sumar datos de una lista basta gestionar los fallos y continuar.
- Además de `try/except`, Python admite `try/finally` sin capturas cuando solo se necesita una acción de cierre. Es una forma válida aunque no sea la estructura mínima utilizada en tus primeros ejemplos.

El uso típico de `finally` será liberar recursos, como una conexión. El cierre de archivos y la forma `with` se estudiarán con archivos. «Siempre» se entiende aquí dentro del funcionamiento normal del intérprete; no es una garantía frente a un cierre forzado del proceso.

## 4. Múltiples capturas y procesamiento de listas

**Fuentes:** `ejercicio1.py`, `multiples_capturas.py` del ZIP 11 y tu [ejercicio4-2.py](ejercicio4-2.py).

La lista contiene textos que intentamos convertir y sumar:

```python
datos = ["1", "dos", "3", "4", "5"]
suma = 0

for indice in range(len(datos) + 1):
    try:
        dato = datos[indice]
        numero = int(dato)
    except IndexError:
        print("Índice fuera de rango")
    except ValueError:
        print("El valor no es numérico")
    else:
        suma += numero

print("Suma:", suma)
```

| Índice | Dato o situación | Qué ocurre | Total después |
|---|---|---|---|
| 0 | `"1"` | Convierte y suma. | 1 |
| 1 | `"dos"` | `ValueError`; no suma. | 1 |
| 2 | `"3"` | Convierte y suma. | 4 |
| 3 | `"4"` | Convierte y suma. | 8 |
| 4 | `"5"` | Convierte y suma. | 13 |
| 5 | No existe. | `IndexError`; no suma. | 13 |

El `+ 1` de `range(len(datos) + 1)` está **puesto para provocar el error**. En un programa normal no recorreríamos una posición inexistente deliberadamente: usaríamos el rango correcto o recorreríamos los valores directamente.

Colocar el `try` dentro del bucle permite continuar con el siguiente dato después de una captura. Si el `try` envolviera el bucle entero, un fallo haría salir de ese bloque y no se continuarían automáticamente las vueltas pendientes.

### 4.1. Atender dos tipos de la misma manera

```python
datos = ["1", "dos", "3", "4", "5"]
suma = 0

for indice in range(len(datos) + 1):
    try:
        suma_parcial = int(datos[indice])
    except (IndexError, ValueError) as error:
        print("Tipo de error:", type(error).__name__)
        print("Mensaje:", error)
    else:
        suma += suma_parcial

print("Suma:", suma)
```

La tupla de tipos permite compartir el manejador. `type(error).__name__` obtiene un nombre legible; la forma `type(error)` que usa la profesora también es válida y muestra la clase.

**Corrección del material:** `except (IndexError, ValueError, Exception)` añade una captura tan amplia que las dos primeras entradas resultan redundantes. Para esos dos errores utiliza `(IndexError, ValueError)`; si necesitas otra alternativa, añade después una captura separada de `Exception`.

### 4.2. Un detalle de tu archivo

Tu captura final escribe `except:` y después intenta imprimir `error`. Ese bloque no ha asociado ningún objeto a ese nombre. Si se alcanza, puede producir otro error mientras intenta informar del primero. Además, los nombres de excepción ligados con `as` no deben darse por disponibles después de terminar su manejador.

Si necesitas esa rama, debe vincular su propio objeto: `except Exception as error:`. En los datos habituales de este ejercicio se atienden los dos errores concretos, de modo que esa rama puede no ejecutarse y ocultar el problema durante las pruebas.

## 5. Lanzar una excepción con raise

**Fuentes:** `lanzar_excepciones.py` y tu [ejercicio4-3.py](ejercicio4-3.py). A veces el formato de una entrada es correcto, pero su valor incumple una regla. `-3` se convierte a entero, aunque no queramos admitirlo como edad.

```python
def solicitar_edad() -> int:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

try:
    edad = solicitar_edad()
except ValueError as error:
    print("No se ha aceptado la edad:", error)
else:
    print("Edad del usuario:", edad)
```

La profesora utiliza `raise Exception(...)`. Funciona, pero aquí se propone `ValueError` porque el problema es un valor no permitido. La misma captura atiende tanto una conversión fallida como una edad negativa.

`raise` no se limita a crear un mensaje: lanza una excepción y cambia el flujo. Si se lanza, la función no llega al `return` siguiente. El código que la llama decide cómo tratar el fallo.

| Entrada | Qué sucede |
|---|---|
| `25` | Devuelve 25 y se muestra la edad. |
| `0` | Devuelve cero; esta regla lo admite. |
| `-3` | Se lanza la excepción creada por la función. |
| `tres` | La conversión ya lanza `ValueError` antes de comprobar el signo. |

Validar significa aplicar reglas concretas, no rechazar cualquier dato que nos parezca raro. Si el programa necesitara un máximo de edad, habría que definirlo e incorporarlo expresamente.

## 6. Saldo y variables globales

**Fuente:** `Ejemplo11_Excepciones/ejercicio2.py`. La versión de clase mantiene un saldo del módulo y una función que lo modifica:

```python
saldo = 1000

def retirar(importe):
    global saldo
    if importe > saldo:
        raise Exception("No tienes saldo suficiente")
    saldo = saldo - importe

try:
    retirar(1200)
except Exception as error:
    print(error)
else:
    print("Saldo actual:", saldo)
```

La retirada no se realiza: se imprime el mensaje y el saldo sigue en mil.

### 6.1. Por qué apareció global

**Aclaración a tu comentario:** el saldo definido fuera ya es una variable del módulo. Una función puede leer ese nombre sin declarar `global`. El problema aparece al **asignar** a `saldo` dentro del cuerpo.

Sin `global`, la asignación hace que Python trate ese nombre como local en esa función. La lectura previa de `saldo` puede entonces producir `UnboundLocalError`: se intenta utilizar la variable local antes de asignarla.

`global saldo` indica que la reasignación se refiere al nombre del módulo. No significa «hacer disponible cualquier variable de cualquier archivo» ni es necesaria para todas las lecturas.

### 6.2. Alternativa con datos explícitos y retorno

**Complemento práctico para reutilizar la función:**

```python
def retirar(saldo: int, importe: int) -> int:
    if importe <= 0:
        raise ValueError("La retirada debe ser positiva")
    if importe > saldo:
        raise ValueError("No tienes saldo suficiente")
    return saldo - importe

saldo = 1000
try:
    nuevo_saldo = retirar(saldo, 200)
except ValueError as error:
    print(error)
else:
    saldo = nuevo_saldo
    print("Saldo actual:", saldo)  # 800
```

Recibe el estado necesario y devuelve otro saldo. Esto facilita probarla sin depender de una variable global. La comprobación de retirada positiva es una regla añadida: el original permitiría un importe negativo y acabaría aumentando el saldo.

Son importes enteros ficticios para practicar. No se está construyendo un sistema bancario ni un modelo completo de dinero o transacciones.

## 7. Adivinar un número y recuperar entradas

**Fuente:** `Ejemplo11_Excepciones/ejercicio3.py`. Reutiliza el juego del módulo 2 y añade una captura de errores de conversión.

```python
import random

secreto = random.randint(1, 10)
adivinar = 0

while adivinar != secreto:
    try:
        adivinar = int(input("Adivina el número del 1 al 10: "))
    except ValueError:
        print("Debes introducir un entero")
        continue

    if adivinar < 1 or adivinar > 10:
        print("Elige un número entre 1 y 10")
    elif adivinar < secreto:
        print("Te has quedado corta")
    elif adivinar > secreto:
        print("Te has pasado")
    else:
        print("Enhorabuena, lo adivinaste")
```

La versión de clase sitúa también las pistas dentro del `try`. Esta adaptación reduce el bloque protegido a la conversión y añade validación de rango. Ambas permiten seguir preguntando tras escribir texto.

Cuando `int(input(...))` falla, la asignación a `adivinar` no se completa. El valor anterior no se sustituye por un entero nuevo. `continue` evita dar pistas sobre ese valor anterior y pasa a la siguiente vuelta.

No confundas los dos controles: `ValueError` atiende formatos como `hola`; el `if` atiende un entero como 15 que queda fuera del intervalo. El juego no tiene un límite de intentos; añadirlo sería otra regla.

## Parte II · Módulos, paquetes y herramientas disponibles

## 8. Crear y utilizar módulos propios

**Fuentes:** pp. 50–51, `operaciones.py` y `calculadora.py` del ZIP 12, y tu [ejercicio4-4.py](ejercicio4-4.py).

Un módulo de Python permite organizar definiciones en un archivo y utilizarlas desde otros. Puede contener funciones, constantes, clases y otras instrucciones, no únicamente funciones.

### 8.1. La calculadora repartida en dos archivos

Primer archivo, **operaciones.py**:

```python
# Archivo: operaciones.py
def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2
```

Segundo archivo, **calculadora.py**, en la misma carpeta para este ejemplo:

```python
# Archivo: calculadora.py
import operaciones
print(operaciones.sumar(6, 2))  # 8

from operaciones import restar
print(restar(8, 3))            # 5

from operaciones import dividir as div
print(div(8, 4))               # 2.0
```

Se importa el nombre del módulo sin la extensión `.py`. El punto de `operaciones.sumar` indica que buscamos ese nombre dentro del módulo.

La división no tiene aquí su propia captura. `div(8, 0)` lanzaría `ZeroDivisionError`, que podría atender el programa que llama a la función. Guardar funciones en otro archivo no elimina sus posibles errores.

### 8.2. Qué cambia en las tres formas de importación

| Forma | Nombre disponible en el programa que importa | Llamada |
|---|---|---|
| `import operaciones` | `operaciones`. | `operaciones.sumar(6, 2)`. |
| `from operaciones import restar` | `restar`. | `restar(8, 3)`. |
| `from operaciones import dividir as div` | `div`. | `div(8, 4)`. |

`as` crea un alias en el contexto que importa. No cambia el nombre original de la función dentro de su módulo. Tras importar solo `dividir as div`, no aparece automáticamente un nombre local `dividir`.

**Matiz de tu ejercicio:** en `ejercicio4-4.py` hay también una función local llamada `dividir` escrita antes de los imports. Allí ese nombre sí podría existir por esa definición previa. El comentario «no funcionaría» es correcto para el ejemplo que solo ha importado el alias, no para cualquier archivo que ya tuviera otro nombre `dividir`.

### 8.3. Importar no es descargar

**Corrección de tus notas:** `import operaciones` no descarga todas sus funciones desde Internet. Busca y carga un módulo disponible. `from operaciones import restar` no es un mecanismo para descargar exclusivamente esa función.

En el funcionamiento habitual, ambas formas requieren cargar e inicializar el módulo; lo que cambia es qué nombres quedan disponibles en tu archivo. Normalmente una importación posterior en el mismo proceso reutiliza el módulo ya cargado.

En los ejemplos de la guía ocurre lo mismo con `modulo1.py`, que contiene un saludo y una despedida: un archivo reúne las funciones y otro las llama mediante el módulo, un nombre importado o un alias.

### 8.4. Código que se ejecuta al importar

Si un módulo contiene un `print` en su nivel principal, ese `print` puede ejecutarse al cargarlo. Definir una función no ejecuta su cuerpo, pero las instrucciones situadas fuera de ella sí participan en la inicialización.

**Complemento opcional:** para separar una demostración del código reutilizable se suele escribir:

```python
def sumar(a, b):
    return a + b

if __name__ == "__main__":
    print(sumar(6, 2))
```

Al ejecutar ese archivo como programa, se muestra ocho. Al importarlo como módulo, esa demostración no se ejecuta. La condición comprueba el modo en que se está usando el archivo; no hace falta profundizar ahora en todos los nombres especiales de Python.

### 8.5. Resolver problemas de importación

En tu ejercicio se anotan las funciones de `operaciones.py` y la calculadora dentro de un único archivo como recordatorio. Para ejecutarlo con `import operaciones`, debe existir realmente el módulo que se importa. Las definiciones previas en otro nombre de archivo no lo crean automáticamente.

Comprueba el nombre del archivo, la carpeta desde la que organizas el ejemplo y el intérprete utilizado. Evita llamar a un archivo propio `math.py`, `random.py` o `datetime.py` si quieres importar los módulos estándar con esos nombres: podrías ocultarlos con tu archivo.

El ZIP incluye `__pycache__/operaciones.cpython-314.pyc`. Es una caché de código compilado que Python puede generar automáticamente. Para estudiar o modificar la función utiliza `operaciones.py`; no necesitas editar la caché.

## 9. Paquetes, biblioteca estándar y pip

**Fuente:** p. 52 de la guía. Los comandos de esta sección son de terminal, no instrucciones para introducir en un `.py` ni en el indicador `>>>`.

| Término | Idea útil ahora |
|---|---|
| Módulo | Unidad de código que se importa; en nuestros ejemplos propios, un archivo `.py`. |
| Paquete | Forma de organizar módulos bajo un mismo nombre o estructura. |
| Biblioteca | Nombre general para un conjunto de herramientas de código. |
| Biblioteca estándar | Herramientas distribuidas con Python, como `math` o `datetime`. |
| pip | Gestor utilizado para instalar y administrar distribuciones de paquetes. |

No toda biblioteca tiene que descargarse. Los ejemplos 11–13 actuales utilizan código propio y biblioteca estándar: no requieren instalar paquetes externos.

### 9.1. Comprobar pip y consultar paquetes

```bash
python3 -m pip --version
python3 -m pip list
```

`python3 -m pip` ejecuta pip con ese intérprete. Esto ayuda a distinguir entre varios Python instalados. En el PDF también aparece `-V` para la versión; `--version` evita confundir mayúsculas y minúsculas.

### 9.2. Plantillas para instalar y desinstalar

Estos nombres son marcadores para un paquete real, no dependencias de la clase:

```bash
python3 -m pip install nombre_paquete
python3 -m pip uninstall nombre_paquete
```

Usa guiones normales `-`. Los guiones tipográficos que pueden copiarse de un PDF no siempre son interpretados como opciones. El nombre de instalación y el nombre utilizado después en `import` no tienen por qué coincidir en todas las bibliotecas.

### 9.3. Entornos virtuales para tus proyectos

**Complemento opcional:** cuando empieces a instalar bibliotecas externas en un proyecto, un entorno virtual permite separar sus dependencias de las de otros trabajos.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
```

Es una secuencia para macOS y shells compatibles como zsh. Crear el entorno y activarlo son operaciones distintas. Esta sección prepara el trabajo posterior; no necesitas hacerlo para importar `math` y completar las prácticas actuales.

## 10. Matemáticas con math

**Fuente:** `Ejemplo12_Modulos/modulo_math.py`.

```python
import math

print(math.pow(2, 8))                # 256.0
print(math.pi)                       # 3.141592...
print(math.sin(math.radians(90)))     # 1.0
print(math.factorial(4))             # 24
print(math.sqrt(9))                  # 3.0
print(round(6.765456, 2))             # 6.77
```

| Operación | Qué aporta |
|---|---|
| `math.pow(a, b)` | Potencia; en el ejemplo devuelve un flotante. |
| `math.pi` | Constante π; no es una llamada y no lleva `()`. |
| `math.radians(grados)` | Conversión de grados a radianes. |
| `math.sin(radianes)` | Seno del ángulo indicado. |
| `math.factorial(entero)` | Factorial de un entero no negativo. |
| `math.sqrt(numero)` | Raíz cuadrada real de un número no negativo. |
| `round(numero, decimales)` | Redondeo; es una función incorporada, no pertenece a `math`. |

El factorial y otras operaciones que antes programábamos mediante bucles tienen implementaciones preparadas. Conocer el algoritmo ayuda a interpretar lo que hace la función, aunque no tengas que volver a escribirlo.

### 10.1. Corrección del logaritmo

```python
import math

print(math.log(1000))    # 6.907755278982137
print(math.log10(1000))  # 3.0
```

El mensaje de clase dice «logaritmo base 10», pero llama a `math.log(1000)`. Con un argumento, `log` calcula el logaritmo natural, en base e. Para base diez, utiliza `log10`. El error está en la correspondencia entre etiqueta y función, no en el resultado que calcula Python.

### 10.2. Redondear hacia arriba, abajo y cero

```python
import math

for valor in [3.89, 3.19, -3.19]:
    print(valor, math.ceil(valor), math.floor(valor), math.trunc(valor))
```

| Valor | ceil: entero hacia arriba | floor: entero hacia abajo | trunc: quitar fracción hacia cero |
|---|---|---|---|
| 3.89 | 4 | 3 | 3 |
| 3.19 | 4 | 3 | 3 |
| −3.19 | −3 | −4 | −3 |

«Arriba» significa hacia números mayores; para un negativo puede ser acercarse a cero. `floor` va hacia números menores. `trunc` descarta la parte fraccionaria y se acerca a cero.

`round` no equivale a ninguna de esas tres políticas. Tampoco debe confundirse con `:.2f`, que produce una presentación de dos decimales. Define la regla de cálculo antes de elegir la función.

## 11. Fechas y horas con datetime

**Fuente:** `Ejemplo12_Modulos/modulo_datetime.py`.

```python
import datetime

print("Ahora:", datetime.datetime.today())
print("Ahora:", datetime.datetime.now())

fecha_hora = datetime.datetime(2027, 1, 26, 8, 30)
print(fecha_hora)
print(fecha_hora.date().strftime("%d/%m/%Y"))
print(fecha_hora.date().strftime("%d/%m/%y"))
print(fecha_hora.time().strftime("%H:%M:%S"))
```

Las dos primeras llamadas consultan el momento local del ordenador. Las últimas utilizan la fecha fija construida por el ejemplo:

```text
2027-01-26 08:30:00
26/01/2027
26/01/27
08:30:00
```

### 11.1. Por qué datetime aparece dos veces

En `datetime.datetime(...)`, el primer nombre es el módulo y el segundo identifica una clase dentro de él. Su construcción recibe año, mes, día, hora y minutos. No necesitas definir clases propias para utilizar este objeto.

Otra forma válida de importar es `from datetime import datetime`; entonces se escribiría `datetime(...)`. Las dos variantes de importación explican por qué puedes encontrar llamadas con aspecto diferente que realizan la misma construcción.

### 11.2. Extraer y dar formato

`date()` obtiene la parte de fecha; `time()`, la parte de hora. `strftime(formato)` produce un texto con la presentación indicada.

| Código | Significado |
|---|---|
| `%d` | Día con dos cifras. |
| `%m` | Mes con dos cifras. |
| `%Y` | Año con cuatro cifras. |
| `%y` | Año con dos cifras. |
| `%H` | Hora en formato de 24 horas. |
| `%M` | Minutos. |
| `%S` | Segundos. |

`%m` y `%M` no son intercambiables. Cambiar el formato no modifica la fecha del objeto ni valida una fecha escrita en una cadena. Una construcción imposible, como el 30 de febrero, puede producir `ValueError`.

En tus calendarios y automatizaciones habrá que tratar zonas horarias y cambios de hora. Los ejemplos actuales no incluyen esa información: trabajan con fechas y horas sin zona explícita. Es un siguiente paso, no algo que quede resuelto por mostrar una fecha bonita.

## 12. Calendarios y configuración regional

**Fuente:** `Ejemplo12_Modulos/modulo_calendar.py`. El original usa `from calendar import *`, que deja disponibles muchos nombres sin prefijo. Aquí se mantiene el prefijo para reconocer su procedencia.

```python
import calendar

print(calendar.calendar(2026, w=4, l=2, c=10, m=2))
print(calendar.month(2026, 12))

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2026, 12))

print(calendar.isleap(2024))        # True
print(calendar.isleap(2025))        # False
print(calendar.leapdays(2010, 2024))  # 3
print(calendar.leapdays(2010, 2025))  # 4
```

`calendar.calendar` devuelve una representación textual de un año; `calendar.month`, la de un mes. Los parámetros de presentación del año son `w`, ancho de cada columna de día; `l`, líneas por semana; `c`, separación entre meses, y `m`, cantidad de meses por fila.

### 12.1. Primer día y bisiestos

`setfirstweekday(6)` y `setfirstweekday(calendar.SUNDAY)` indican domingo; lunes es cero. Esa configuración afecta a las funciones de calendario que usan el calendario global del módulo.

`isleap` devuelve un booleano. `leapdays(inicio, fin)` cuenta los años bisiestos dentro del intervalo con **fin excluido**: 2024 no entra en `leapdays(2010, 2024)`, pero sí en el intervalo que acaba en 2025.

### 12.2. Calendario en español

El original configura la región del proceso con `locale.setlocale(locale.LC_ALL, "es_ES")` y crea un `LocaleTextCalendar`. La disponibilidad del identificador depende del sistema.

Una versión que informa de un fallo regional sería:

```python
import calendar
import locale

try:
    calendario = calendar.LocaleTextCalendar(locale="es_ES")
    texto_calendario = calendario.formatmonth(2026, 12)
except locale.Error as error:
    print("La configuración regional solicitada no está disponible:", error)
else:
    print(texto_calendario)
```

Si no está disponible, el problema es la configuración regional solicitada, no la regla de bisiestos. El manejo muestra una relación entre módulos y excepciones.

`from calendar import *` funciona en el archivo de clase, pero puede ocultar de dónde viene cada nombre o provocar coincidencias con otros nombres del programa. Importar el módulo y usar su prefijo suele facilitar la lectura de proyectos con varias herramientas.

## 13. Selecciones con random

**Fuente:** `Ejemplo12_Modulos/modulo_random.py`. Amplía los números aleatorios de los juegos anteriores con selección de elementos de secuencias.

```python
from random import random, randrange, randint, choice, sample

print(random())
print(randrange(10))
print(randrange(8, 10))
print(randint(8, 10))

for intento in range(5):
    print("Número entre 20 y 30:", randint(20, 30))

print(choice([1, 2, 3, 4, 5, 6]))
print(choice((1, 2, 3, 4, 5, 6)))
print(sample([1, 2, 3, 4, 5, 6], 3))
print(sample((1, 2, 3, 4, 5, 6), 3))
```

| Función | Qué devuelve |
|---|---|
| `random()` | Decimal desde cero incluido hasta uno excluido. |
| `randrange(10)` | Entero de cero a nueve. |
| `randrange(8, 10)` | Ocho o nueve. |
| `randint(8, 10)` | Ocho, nueve o diez. |
| `choice(secuencia)` | Un elemento de la secuencia. |
| `sample(secuencia, cantidad)` | Una lista con la muestra seleccionada sin reemplazo. |

### 13.1. Extremos y repeticiones

`randrange` sigue la idea del rango con extremo final excluido; `randint` incluye sus dos extremos. Repetir cualquiera de esas llamadas puede devolver el mismo número.

**Corrección al comentario de clase:** `choice` no evita repeticiones entre llamadas. Elige un elemento cada vez, sin recordar cuáles eligió anteriormente.

`sample` selecciona posiciones sin reemplazo en esa llamada. Cuando la población contiene valores distintos, no se repiten valores. Si la población ya contiene valores duplicados, puede seleccionar varias apariciones del mismo valor. Pedir más elementos de los disponibles produce `ValueError`; elegir con `choice` en una secuencia vacía produce `IndexError`.

### 13.2. Los dos ejemplos finales

```python
from random import sample

numeros = sample(range(1, 50), 6)
responsables = sample(["Luis", "Marta", "Pedro", "Laura"], 2)

print("Primitiva:", numeros)
print("Pone y recoge la mesa:", responsables)
```

La primera muestra contiene seis enteros distintos entre uno y cuarenta y nueve, no cincuenta. La segunda contiene dos personas distintas; sus posiciones permiten asignar los dos papeles.

No esperes los mismos resultados en cada ejecución. Para probar un programa aleatorio conviene fijar el escenario de prueba o comprobar propiedades —cantidad, intervalo y ausencia de repeticiones cuando corresponde— en lugar de una salida concreta.

## Parte III · Manejo de texto

## 14. Cadenas y métodos: cómo conservar los resultados

**Fuentes:** pp. 53–67 y `Ejemplo13_Manejo_Texto/metodos_funciones.py`. El archivo utiliza principalmente `"bienvenidos al curso de Python"` para mostrar distintas operaciones.

Una cadena es una secuencia de texto inmutable. Se puede recorrer e indexar como vimos en el módulo 3, pero no sustituir una posición de la cadena original como si fuera una lista.

```python
texto = "Hola Python"
mayusculas = texto.upper()

print(mayusculas)  # HOLA PYTHON
print(texto)       # Hola Python

texto = texto.upper()
print(texto)       # HOLA PYTHON
```

El método produce un resultado. Mostrar ese resultado con `print` no lo guarda en la variable original; reasignar el nombre sí hace que apunte al texto resultante.

### 14.1. Funciones y métodos que se combinan

| Forma | Qué utiliza |
|---|---|
| `len(texto)` | Función incorporada que recibe un objeto. |
| `texto.upper()` | Método del objeto de texto. |
| `texto.split()` | Método que devuelve una lista. |
| `"-".join(palabras)` | Método de una cadena separadora que recibe los textos que unirá. |

La guía llama «funciones con cadenas» al conjunto de herramientas. Para distinguir la sintaxis, aquí se indican cuáles son métodos y cuáles funciones incorporadas. Que un método devuelva un dato no garantiza que sea otro texto: puede ser un booleano, un entero o una lista.

## 15. Cambiar y comprobar mayúsculas, letras y dígitos

### 15.1. Transformaciones de mayúsculas y minúsculas

```python
texto = "bienvenidos al curso de Python"

print(texto.capitalize())
print(texto.title())
print(texto.upper())
print(texto.lower())
print(texto.swapcase())
```

| Método | Resultado |
|---|---|
| `capitalize()` | `Bienvenidos al curso de python` |
| `title()` | `Bienvenidos Al Curso De Python` |
| `upper()` | `BIENVENIDOS AL CURSO DE PYTHON` |
| `lower()` | `bienvenidos al curso de python` |
| `swapcase()` | `BIENVENIDOS AL CURSO DE pYTHON` |

**Matiz de capitalize:** además de poner el comienzo en mayúscula, convierte el resto a minúsculas. Puede cambiar nombres propios y siglas. `title` aplica sus reglas de capitalización a palabras, pero no conoce las convenciones editoriales de cada título o nombre. No lo uses como corrector lingüístico automático.

### 15.2. Métodos que devuelven booleanos

| Método | Qué pregunta |
|---|---|
| `isalnum()` | ¿Hay al menos un carácter y todos son letras o dígitos según su clasificación? |
| `isalpha()` | ¿Hay al menos un carácter y todos son letras? |
| `isdigit()` | ¿Hay al menos un carácter y todos son dígitos? |
| `isupper()` | ¿Hay caracteres con caso y todos esos caracteres están en mayúsculas? |
| `islower()` | ¿Hay caracteres con caso y todos esos caracteres están en minúsculas? |

```python
for texto in ["hola", "1234", "hola1234", "hola_1234", "hola mundo", ""]:
    print(texto, texto.isalnum(), texto.isalpha(), texto.isdigit())
```

| Texto | isalnum | isalpha | isdigit |
|---|---|---|---|
| `hola` | True | True | False |
| `1234` | True | False | True |
| `hola1234` | True | False | False |
| `hola_1234` | False | False | False |
| `hola mundo` | False | False | False |
| Cadena vacía | False | False | False |

Los espacios y el guion bajo no son letras ni dígitos. Las letras no se limitan a las del alfabeto ASCII: `"niño".isalpha()` devuelve `True`.

### 15.3. Mayúsculas y minúsculas no exigen que todo sean letras

```python
for texto in ["HOLA", "HOLA1234", "HOLA_1234", "1234", "hola", "hola_1234"]:
    print(texto, texto.isupper(), texto.islower())
```

`HOLA_1234` cumple `isupper`: el guion bajo y los números no contradicen que las letras estén en mayúsculas. `1234` no cumple ninguno de los dos porque no contiene caracteres con caso. La cadena original de clase tampoco cumple ninguno: combina minúsculas y la P mayúscula de Python.

### 15.4. isdigit no valida cualquier número convertible

```python
for texto in ["1234", "-3", "3.5", "²"]:
    print(texto, texto.isdigit())
```

| Texto | isdigit | Observación |
|---|---|---|
| `1234` | True | Puede convertirse a entero. |
| `-3` | False | El signo no es un dígito, aunque `int` acepte ese texto. |
| `3.5` | False | El punto no es un dígito, aunque `float` acepte el texto. |
| `²` | True | Es un dígito Unicode, pero `int("²")` falla. |

Para una entrada numérica general, intenta la conversión apropiada y captura su error. Después comprueba las reglas del valor: una conversión válida no implica que una cantidad sea positiva o que una edad esté dentro del intervalo requerido.

## 16. Limpiar extremos, separar y unir

### 16.1. lstrip, rstrip y strip

```python
ejemplo = "     Hoy es lunes    "

print(repr(ejemplo.lstrip()))  # 'Hoy es lunes    '
print(repr(ejemplo.rstrip()))  # '     Hoy es lunes'
print(repr(ejemplo.strip()))   # 'Hoy es lunes'
print("........hola........".strip("."))  # hola
```

`lstrip` quita por el comienzo; `rstrip`, por el final; `strip`, por ambos extremos. `repr` se utiliza aquí para ver las comillas y los espacios que quedan; en el archivo de clase se añade un punto al imprimir con una finalidad parecida.

Sin argumento, estos métodos retiran caracteres de espacio, incluidos tabuladores y saltos de línea. No eliminan ni reducen los espacios interiores.

Si indicas caracteres, como `strip(".")`, se retiran esos caracteres repetidos de los extremos. El argumento se interpreta como un conjunto de caracteres admitidos para retirar, no como una frase o prefijo literal que deba coincidir entero.

### 16.2. split: pasar de texto a lista

```python
texto = "bienvenidos al curso de Python"
palabras = texto.split()
print(type(palabras))  # <class 'list'>
print(palabras)
# ['bienvenidos', 'al', 'curso', 'de', 'Python']

fecha = "24/11/2026"
partes = fecha.split("/")
print("Día:", partes[0])
print("Mes:", partes[1])
print("Año:", partes[2])
```

`split()` sin argumentos trata espacios en blanco consecutivos como separadores y no conserva elementos vacíos de los extremos. Con un separador explícito, el comportamiento es distinto:

```python
texto = " a  b "
print(texto.split())     # ['a', 'b']
print(texto.split(" "))  # ['', 'a', '', 'b', '']
```

Los elementos de `partes` siguen siendo cadenas: `"24"`, `"11"` y `"2026"`. Separar una fecha no comprueba que exista ni la transforma en un objeto `datetime`. Si faltan separadores, acceder a una posición supuesta podría producir `IndexError`.

### 16.3. join: pasar de textos a una cadena

```python
palabras = ["bienvenidos", "al", "curso", "de", "Python"]
print("-".join(palabras))
# bienvenidos-al-curso-de-Python

print(" ".join(palabras))
# bienvenidos al curso de Python
```

Se llama al método sobre la cadena que actuará como separador. Los elementos que se unen deben ser textos; `join` no convierte automáticamente una lista de enteros. Sobre una colección vacía produce texto vacío.

### 16.4. Reducir separaciones a espacios simples

```python
entrada = "  Python   es útil\npara automatizar  "
limpio = " ".join(entrada.split())
print(limpio)  # Python es útil para automatizar
```

Esta regla descarta saltos de línea y diferencias de espaciado. Resulta útil para algunas comparaciones o entradas de formularios; en un manuscrito puede destruir separación entre párrafos. Conserva el original cuando esa estructura sea información que necesites.

## 17. Sustituir, buscar y contar

### 17.1. replace

```python
texto = "bienvenidos al curso de Python"
print(texto.replace("e", "E"))
# biEnvEnidos al curso dE Python

print(texto.replace("o", "O", 2))
# bienvenidOs al cursO de Python

print(texto)  # La cadena original sigue igual.
```

El primer argumento es la cadena buscada y el segundo la sustituta; el tercero, opcional, limita la cantidad de sustituciones. Funciona también con fragmentos de más de un carácter. Si no hay coincidencia, el contenido no cambia.

La búsqueda es exacta y distingue mayúsculas de minúsculas. `replace("Java", "Python")` no sustituye `JAVA`. Tampoco decide por sí mismo si la coincidencia forma una palabra completa.

### 17.2. find y rfind

```python
texto = "bienvenidos al curso de Python"

print(texto.find("o"))          # 9
print(texto.find("o", 11))      # 19
print(texto.find("o", 10, 20))  # 19
print(texto.find("W"))          # -1
print(texto.rfind("o"))         # 28
```

`find` devuelve el índice de la primera coincidencia dentro de la zona solicitada; el final del intervalo se excluye. `rfind` localiza la última coincidencia, pero su índice se sigue contando desde el comienzo de la cadena.

| Resultado | Significado |
|---|---|
| Cero o positivo | Posición donde se encontró. |
| −1 | No se encontró. |

**Fallo típico:** usar directamente `if texto.find("b"):`. En el ejemplo la b está en el índice cero, que se interpreta como falso; una ausencia daría menos uno, que se interpreta como verdadero. Para comprobar existencia utiliza `"b" in texto` o compara expresamente el índice con `-1`.

### 17.3. count, startswith y endswith

```python
texto = "bienvenidos al curso de Python"
print(texto.count("e"))            # 3
print(texto.startswith("b"))       # True
print(texto.endswith("Python"))    # True
print(texto.endswith("python"))    # False
```

`count` cuenta apariciones no solapadas del fragmento. No es un contador lingüístico de palabras: puede encontrar un fragmento dentro de una palabra mayor. `startswith` y `endswith` devuelven booleanos sobre el comienzo y el final exactos.

Estas comprobaciones no eliminan automáticamente espacios. Por ejemplo, un texto que acaba en `"Python "` no termina exactamente en `"Python"` hasta aplicar una regla de limpieza apropiada.

## 18. Caracteres, orden y funciones incorporadas

```python
texto = "bienvenidos al curso de Python"

print(len(texto))        # 30
print(max(texto))        # y
print(repr(min(texto)))  # ' ': un espacio.
print(ord("A"))         # 65
print(chr(65))          # A
print(sorted(texto))
```

### 18.1. Longitud y orden

`len(texto)` cuenta los elementos de la cadena, incluidos espacios y signos. No cuenta palabras ni tokens de un modelo. En estos textos sencillos coincide con la cantidad habitual de caracteres que ves; Unicode permite casos en que un símbolo visual contiene más de un elemento de cadena.

`max` y `min` comparan caracteres por sus códigos, no el significado de las palabras. `sorted(texto)` devuelve una lista de caracteres ordenados, no una lista de palabras. El espacio queda antes que las letras en el ejemplo.

`min("")` y `max("")` producen `ValueError`: no hay ningún elemento que seleccionar. `len("")`, en cambio, devuelve cero.

### 18.2. ASCII y Unicode

El archivo dice «tabla ASCII». Sus ejemplos A y 65 pertenecen a ese subconjunto, pero Python utiliza Unicode para las cadenas. `ord` recibe un carácter y devuelve su punto de código; `chr` hace la conversión inversa para un código válido.

```python
print(ord("ñ"))   # 241
print(chr(241))   # ñ
```

No necesitas memorizar códigos. Lo importante es no dar por hecho que el orden numérico de los caracteres equivale a la ordenación lingüística del español, especialmente con mayúsculas y tildes.

## 19. Ejercicio completo de Java y Python

**Fuente:** `Ejemplo13_Manejo_Texto/ejercicio1.py`. El enunciado pide sustituir, contar, comprobar extremos, medir longitud y cambiar el caso.

```python
frase = "Me gusta Java porque Java es divertido"

print(frase.replace("Java", "Python"))
print(frase.count("Java"))
print(frase.startswith("Me gusta"))
print(frase.endswith("divertido"))
print(len(frase))
print(max(frase))
print(repr(min(frase)))
print(frase.upper())
print(frase.lower())
```

Resultados:

```text
Me gusta Python porque Python es divertido
2
True
True
38
v
' '
ME GUSTA JAVA PORQUE JAVA ES DIVERTIDO
me gusta java porque java es divertido
```

El original imprime directamente el espacio del mínimo; aquí se usa `repr` para poder verlo. El resto de las operaciones conserva el comportamiento de clase.

### 19.1. Por qué siguen apareciendo dos Java

La primera llamada crea y muestra otro texto, pero no reasigna `frase`. Por eso las consultas posteriores utilizan la cadena original y su longitud es treinta y ocho.

```python
frase = "Me gusta Java porque Java es divertido"
frase = frase.replace("Java", "Python")

print(frase.count("Java"))    # 0
print(frase.count("Python"))  # 2
print(len(frase))             # 42
```

Cada sustitución cambia cuatro letras por seis y añade dos caracteres; al haber dos, la longitud aumenta en cuatro. Mostrar un resultado, devolverlo y guardarlo siguen siendo operaciones distintas, igual que en el módulo de funciones.

## Parte IV · Aplicación y repaso

## 20. Aplicaciones a tus proyectos

**Complementos opcionales.** Este módulo refuerza el Python práctico de tu máster y prepara el tratamiento de errores y la observabilidad. Los ejemplos son locales y usan datos ficticios; no conectan servicios ni modifican aplicaciones.

### 20.1. Preparar una versión de texto para comprobaciones

```python
def describir_texto(texto: str) -> dict:
    palabras = texto.split()
    limpio = " ".join(palabras)
    return {
        "original": texto,
        "limpio": limpio,
        "palabras": len(palabras),
        "caracteres": len(limpio),
    }

resultado = describir_texto("  Python   es útil\npara automatizar  ")
print(resultado["limpio"])
print(resultado["palabras"])  # 5
```

La función conserva el original y añade una versión con separación uniforme. La cantidad es un conteo de fragmentos obtenidos con `split`, no una estimación fiable de tokens ni una evaluación de calidad literaria.

En tu pipeline editorial conviene decidir qué versión utiliza cada comprobación. Normalizar para una comparación no implica que debas sustituir por ese texto el manuscrito con sus párrafos.

### 20.2. Procesar una tanda y devolver incidencias concretas

La siguiente función recibe textos con importes ficticios. Define dos reglas: formato decimal con punto y valores no negativos. Los errores se devuelven como datos, de forma que el programa principal pueda mostrarlos o enviarlos a revisión.

```python
def sumar_importes_texto(entradas: list) -> dict:
    total = 0.0
    validos = 0
    incidencias = []

    for indice in range(len(entradas)):
        entrada = entradas[indice]
        try:
            importe = float(entrada.strip())
            if importe < 0:
                raise ValueError("El importe debe ser no negativo")
        except ValueError as error:
            incidencias.append({
                "indice": indice,
                "entrada": entrada,
                "tipo": type(error).__name__,
                "mensaje": str(error),
            })
        else:
            total += importe
            validos += 1

    return {"total": total, "validos": validos, "incidencias": incidencias}

resultado = sumar_importes_texto([" 12.50 ", "dos", "-3", "4"])
print(resultado["total"])              # 16.5
print(resultado["validos"])            # 2
print(len(resultado["incidencias"]))   # 2
```

La captura está dentro del recorrido: un dato inválido no impide procesar los siguientes. El `else` solo incorpora importes aceptados. El mensaje del negativo procede de una regla del programa; el del texto no convertible, de Python.

**Contrato del ejemplo:** todas las entradas son cadenas y se trabaja con números decimales ordinarios. No se contemplan aquí valores especiales como infinito o NaN, reglas completas de precisión monetaria ni formatos con separadores de miles. Si la entrada pudiera contener otros tipos, habría que decidir cómo validarlos, sin ocultar automáticamente cualquier error con una captura genérica.

### 20.3. Qué trasladar a automatizaciones y agentes

| Aprendizaje | Aplicación posterior |
|---|---|
| Capturar errores concretos | Distinguir datos inválidos de fallos de una integración. |
| Conservar incidencias con contexto | Revisar qué registro falló y por qué. |
| Lanzar una excepción al incumplir una regla | Impedir que se continúe con un dato que el cálculo no admite. |
| Separar módulos | Reutilizar y comprobar funciones desde distintas partes del proyecto. |
| Precisar fechas y formatos | Evitar confundir presentación con significado o zona horaria. |
| Normalizar textos con una regla explícita | Preparar entradas de formularios o búsquedas comparables. |
| Comprobar resultados esperados | Detectar regresiones en cambios hechos con IA. |

Capturar una excepción no significa que se deba reintentar cualquier acción. En una API habrá que distinguir fallos recuperables, límites y posibles duplicados. Ese puente se desarrollará con HTTP, timeouts e idempotencia. Por ahora, identifica el error y decide de forma explícita si continuar, parar o solicitar revisión.

## 21. Repaso, correcciones y fuentes

### 21.1. Lo que deberías poder explicar

- Qué diferencia hay entre un error de sintaxis, una excepción y un error lógico.
- Qué ocurre con el resto del `try` cuando falla una instrucción.
- Qué recibe `as error` y cuándo existe ese nombre.
- Cuándo se ejecutan `else` y `finally` y por qué no son equivalentes.
- Por qué una captura genérica no es obligatoria.
- Qué cambia al poner el `try` dentro o fuera de un bucle.
- Qué hace `raise` y por qué una regla inválida no tiene que convertirse en un resultado numérico.
- Por qué apareció `global saldo` y cómo evitar esa dependencia recibiendo y devolviendo el estado.
- Qué nombres dejan disponibles las tres formas de importación.
- Qué herramientas están ya en Python y para qué se utiliza pip.
- Cómo distinguir una transformación de texto del guardado de su resultado.
- Qué tipo devuelve cada método: texto, entero, booleano o lista.

### 21.2. Casos de referencia

| Práctica | Caso | Resultado esperado |
|---|---|---|
| División | 8 y 2 | 4.0, seguido de FIN. |
| División | 8 y 0 | Captura de división, sin resultado, y FIN. |
| Conversión | `dos` | Captura de valor; no se completan las instrucciones posteriores del try. |
| Suma de lista | `1`, `dos`, `3`, `4`, `5` y un índice extra | Suma 13; una conversión fallida y un índice fuera de rango. |
| Edad | −3 | Excepción de la regla de edad. |
| Saldo original | Retirar 1200 desde 1000 | No se retira y el saldo sigue en 1000. |
| Saldo adaptado | Retirar 200 desde 1000 | Devuelve 800. |
| Calculadora importada | Datos del ZIP | 8; 5; 2.0. |
| Logaritmo | `log(1000)` frente a `log10(1000)` | Aproximadamente 6.907755; 3.0. |
| Redondeos negativos | −3.19 | ceil −3; floor −4; trunc −3. |
| Fecha fija | 26 de enero de 2027, 8:30 | Formatos 26/01/2027, 26/01/27 y 08:30:00. |
| Bisiestos | Intervalos 2010–2024 y 2010–2025 | 3 y 4; final excluido. |
| Muestra de lotería | `sample(range(1, 50), 6)` | Seis valores distintos de 1 a 49. |
| Texto principal | Longitud, mínimo y máximo | 30, espacio e y. |
| Texto principal | find o; siguiente o; última o | 9, 19 y 28. |
| Buscar ausencia | find W | −1. |
| split | Fecha 24/11/2026 | Tres textos: 24, 11 y 2026. |
| Java original | Reemplazo solo impreso | La variable conserva Java dos veces y mide 38. |
| Java reasignado | Reemplazo guardado | Java cero veces, Python dos veces y longitud 42. |
| Lote ficticio | 12.50, dos, −3 y 4 | Total 16.5, dos válidos y dos incidencias. |

Los mensajes detallados de excepciones pueden variar entre versiones de Python. Comprueba el tipo, el comportamiento y los datos, no únicamente una frase exacta del intérprete. Los resultados aleatorios se comprueban por sus propiedades.

### 21.3. Correcciones del material y de tus notas

| Detalle encontrado | Explicación |
|---|---|
| Todas las excepciones derivan de Exception. | Muchas habituales sí; la base general es BaseException. |
| Siempre hay que terminar con un except genérico. | Es opcional y debe responder a una política concreta. |
| `except:` y `except Exception` son lo mismo. | El primero también captura interrupciones que el segundo no captura. |
| Agrupar IndexError, ValueError y Exception. | Añadir Exception hace redundantes los dos tipos anteriores en esa captura. |
| Imprimir error dentro de una captura que no lo vincula. | Esa rama debe tener su propio `as error` si necesita el objeto. |
| Global es necesario para acceder a saldo. | En el ejemplo se necesita para reasignar el nombre del módulo; leerlo no exige global por sí solo. |
| Importar un módulo descarga todas sus funciones. | Importar y descargar o instalar son operaciones distintas. |
| Logaritmo base diez con math.log de un argumento. | Esa llamada calcula el natural; para base diez se utiliza log10. |
| Choice evita duplicados. | Las llamadas pueden repetirse; sample selecciona sin reemplazo en una misma llamada. |
| Capitalize solo cambia la primera letra. | También pone el resto en minúsculas. |
| Isdigit demuestra que int aceptará el texto. | No en todos los casos Unicode; tampoco admite signos o puntos decimales. |
| Min y max buscan letras por orden lingüístico. | Comparan los caracteres por su código. |
| Python utiliza solo una tabla ASCII para texto. | Las cadenas son Unicode; ASCII es un subconjunto. |
| Replace modifica la cadena original. | Devuelve un resultado; necesitas conservarlo o reasignarlo. |
| Split de una fecha valida una fecha. | Solo separa cadenas; no comprueba sus reglas de calendario. |

### 21.4. Mapa de los 14 archivos de clase

| ZIP | Archivo | Desarrollo principal |
|---|---|---|
| 11 | `errores.py` | Secciones 2–3: división, capturas, else y finally. |
| 11 | `ejercicio1.py` | Sección 4: conversión por registro y errores separados. |
| 11 | `multiples_capturas.py` | Sección 4.1: agrupar tipos y revisar el alcance. |
| 11 | `lanzar_excepciones.py` | Sección 5: edad y raise. |
| 11 | `ejercicio2.py` | Sección 6: retirada, excepción y global. |
| 11 | `ejercicio3.py` | Sección 7: juego y conversión recuperable. |
| 12 | `operaciones.py` | Sección 8: código reutilizable en un módulo. |
| 12 | `calculadora.py` | Sección 8: tres formas de importación. |
| 12 | `modulo_math.py` | Sección 10: cálculos y políticas de redondeo. |
| 12 | `modulo_datetime.py` | Sección 11: fecha, hora y formatos. |
| 12 | `modulo_calendar.py` | Sección 12: calendarios, región y bisiestos. |
| 12 | `modulo_random.py` | Sección 13: números y muestras. |
| 13 | `metodos_funciones.py` | Secciones 14–18: herramientas de texto. |
| 13 | `ejercicio1.py` | Sección 19: práctica integrada de Java y Python. |

Los archivos compilados de `__pycache__` no se cuentan como ejercicios adicionales. Tus cuatro `.py` se integran en las secciones de sus temas y se conservan sin cambios.

### 21.5. Fuentes y continuidad

- [Guía IFCD0062 Fundamentos programacion Python.pdf](<../../IFCD0062 Fundamentos programacion Python.pdf>): pp. 44–67; el módulo 5 empieza en p. 68.
- [Ejemplo11_Excepciones.zip](../../Ejemplo11_Excepciones.zip).
- [Ejemplo12_Modulos.zip](../../Ejemplo12_Modulos.zip).
- [Ejemplo13_Manejo_Texto.zip](../../Ejemplo13_Manejo_Texto.zip).
- Tus [notas originales](modulo4.md), [ejercicio4-1.py](ejercicio4-1.py), [ejercicio4-2.py](ejercicio4-2.py), [ejercicio4-3.py](ejercicio4-3.py) y [ejercicio4-4.py](ejercicio4-4.py).
- [Apuntes ampliados del módulo 3](../modulo3/modulo3_apuntes_ampliados.md): funciones, colecciones, retornos y mutabilidad.
- [MASTER-PERSONALIZADO-IA.md](../../../../MASTER-PERSONALIZADO-IA.md) y [ENCAJE-TECNOFOR-MASTER.md](../../../../ENCAJE-TECNOFOR-MASTER.md): orientación de los complementos.

Referencias oficiales de apoyo, sin lectura adicional obligatoria:

- [Errores y excepciones](https://docs.python.org/es/3.14/tutorial/errors.html).
- [Módulos e importación](https://docs.python.org/es/3.14/tutorial/modules.html).
- [Declaración global](https://docs.python.org/es/3.14/reference/simple_stmts.html#the-global-statement).
- [Guía de pip](https://pip.pypa.io/en/stable/user_guide/).
- [math](https://docs.python.org/es/3.14/library/math.html), [datetime](https://docs.python.org/es/3.14/library/datetime.html), [calendar](https://docs.python.org/es/3.14/library/calendar.html) y [random](https://docs.python.org/es/3.14/library/random.html).
- [Tipos incorporados y métodos de texto](https://docs.python.org/es/3.14/library/stdtypes.html#string-methods).

El módulo 5 desarrollará clases, objetos y archivos. Aquí se reconocen objetos de la biblioteca estándar y la necesidad de liberar recursos, pero se pospone el desarrollo completo de orientación a objetos, persistencia y clases propias de excepción. Las integraciones reales y su tratamiento de fallos se incorporarán después en el itinerario del máster.
