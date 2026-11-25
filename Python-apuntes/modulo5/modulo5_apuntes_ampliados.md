# Módulo 5 · Introducción a la programación orientada a objetos

Apuntes ampliados de la parte de POO trabajada el 25 de noviembre de 2026, a partir del PDF general de Ana Isabel Vegas, los ejemplos de la profesora y tus notas y ejercicios. Actualización: 25 de noviembre de 2026.

**Estado:** primera parte del módulo 5, centrada en clases, objetos, atributos, métodos y composición. Es lo que aparece desarrollado en tus notas de hoy y en los tres archivos Python del ZIP de POO disponible. El documento se podrá ampliar cuando haya material nuevo.

**Aclaración sobre los archivos:** el ejemplo de POO está en `Ejemplo14_POO.zip`, aunque en la petición se mencionaba el ejemplo 11. `Ejemplo11_Excepciones.zip` corresponde al módulo 4. Para estos apuntes se han revisado los tres archivos del ejemplo 14: `clases_objetos.py`, `ejercicio1.py` y `ejercicio2.py`, junto con tus dos ejercicios del módulo 5.

**Alcance en el PDF general:** el módulo 5 comienza en la p. 68; clases y objetos están en pp. 69–70 y composición en pp. 71–72. Después aparecen encapsulamiento, pp. 73–75; herencia y herencia múltiple, pp. 76–79; y ficheros, pp. 80–83. Aquí se desarrollan las pp. 69–72 y se deja un mapa breve de continuación. No se da por explicado en clase todo lo que figura después en el PDF.

**Cómo leerlo:** **Aclaración** precisa una idea; **Corrección** señala un detalle del material que puede llevar a confusión; **Complemento opcional** conecta con tus proyectos o amplía el tema. Los ejemplos adaptados no sustituyen los originales. Se conservan [modulo5.md](modulo5.md), [ejercicio5-1.py](ejercicio5-1.py) y [ejercicio5-2.py](ejercicio5-2.py).

Los bloques `python` son completos y se pueden ejecutar por separado. Algunas clases se repiten deliberadamente para que no tengas que ejecutar bloques anteriores. Las salidas y los fragmentos usados solo para comparar sintaxis van en bloques `text`. En los ejercicios con `input`, escribe un número en cada pregunta.

## Índice

1. [Qué aporta la POO y qué ya conocías](#1-qué-aporta-la-poo-y-qué-ya-conocías)
2. [Clase, objeto, instancia y referencia](#2-clase-objeto-instancia-y-referencia)
3. [Definir una clase e inicializar sus objetos](#3-definir-una-clase-e-inicializar-sus-objetos)
4. [Entender self y el acceso con punto](#4-entender-self-y-el-acceso-con-punto)
5. [Métodos: datos, acciones y valores devueltos](#5-métodos-datos-acciones-y-valores-devueltos)
6. [El ejemplo Persona de la profesora, paso a paso](#6-el-ejemplo-persona-de-la-profesora-paso-a-paso)
7. [Mostrar un método, llamarlo y mostrar su resultado](#7-mostrar-un-método-llamarlo-y-mostrar-su-resultado)
8. [Ejercicio 1: calculadora de la profesora](#8-ejercicio-1-calculadora-de-la-profesora)
9. [Tu calculadora: guardar datos en el objeto](#9-tu-calculadora-guardar-datos-en-el-objeto)
10. [Ejercicio 2: la clase Cliente](#10-ejercicio-2-la-clase-cliente)
11. [Composición: Cliente tiene una Direccion](#11-composición-cliente-tiene-una-direccion)
12. [Recorrer atributos encadenados y compartir referencias](#12-recorrer-atributos-encadenados-y-compartir-referencias)
13. [Punto y Triangulo: los ejemplos del PDF](#13-punto-y-triangulo-los-ejemplos-del-pdf)
14. [Unir objetos con listas y diccionarios](#14-unir-objetos-con-listas-y-diccionarios)
15. [Errores frecuentes y cómo reconocerlos](#15-errores-frecuentes-y-cómo-reconocerlos)
16. [Aplicación a tu ámbito: un borrador editorial](#16-aplicación-a-tu-ámbito-un-borrador-editorial)
17. [Práctica guiada con soluciones](#17-práctica-guiada-con-soluciones)
18. [Qué viene después en el módulo 5](#18-qué-viene-después-en-el-módulo-5)
19. [Repaso de ideas y correcciones](#19-repaso-de-ideas-y-correcciones)
20. [Fuentes y mapa del material integrado](#20-fuentes-y-mapa-del-material-integrado)

## 1. Qué aporta la POO y qué ya conocías

La **programación orientada a objetos**, o **POO**, permite organizar un programa alrededor de objetos que reúnen información y operaciones relacionadas con ella.

Hasta ahora habías aprendido a guardar datos en variables y colecciones, y a agrupar acciones en funciones. Una clase permite dar un nombre a un tipo de entidad de tu programa y describir sus datos y su comportamiento.

Por ejemplo, una persona puede tener nombre y edad, y ofrecer una operación que devuelva su nombre en mayúsculas. Un cliente puede tener un nombre, un identificador, una condición VIP y una dirección. Un borrador editorial puede tener título, texto, autora y estado de revisión.

| Concepto | Pregunta que responde | Ejemplo |
|---|---|---|
| Dato o atributo | ¿Qué información tiene? | El nombre de una persona. |
| Método | ¿Qué operación ofrece? | Obtener ese nombre en mayúsculas. |
| Estado | ¿Qué valores tiene ahora? | Nombre `"María José"`, edad `36`. |
| Clase | ¿Cómo es ese tipo de objeto? | `Persona`. |
| Instancia | ¿Cuál es el objeto concreto? | Una persona creada con esos valores. |

La POO es una forma de organizar el código. No necesitas transformar en clases todas las funciones que escribas: una suma o una limpieza breve de texto pueden seguir siendo funciones. Una clase empieza a aportar más cuando hay datos relacionados que se conservan y operaciones que trabajan con ellos.

### 1.1. Ya estabas utilizando objetos

Cuando haces `texto.upper()` o `lista.append(...)`, utilizas métodos de objetos creados a partir de tipos que Python ya proporciona.

```python
texto = "python"
colores = ["azul", "verde"]
coordenadas = (4, 6)

print(type(texto))
print(type(colores))
print(type(coordenadas))
print(texto.upper())

try:
    int("dos")
except ValueError as error:
    print(type(error))
```

Salida:

```text
<class 'str'>
<class 'list'>
<class 'tuple'>
PYTHON
<class 'ValueError'>
```

Tu nota sobre los errores es acertada: `ValueError` es una clase; el error concreto que se captura con `as error` es un objeto de esa clase. Lo nuevo de esta parte es definir tus propios tipos con `class`.

**Aclaración:** que los valores de Python sean objetos no significa que todos los programas deban escribirse siguiendo un diseño orientado a objetos. Puedes combinar funciones, módulos, colecciones y clases.

### 1.2. Abstracción: elegir lo que importa para el programa

En tus notas aparece la idea de hacer abstracción al decidir cómo será una persona. Consiste en seleccionar las características relevantes para el problema, dejando fuera detalles que no necesitas representar.

Para explicar métodos basta una `Persona` con nombre y edad. Para gestionar una inscripción quizá solo necesites el nombre y un identificador; para enviar correspondencia añadirías una dirección. No hace falta representar todos los rasgos posibles de una persona ni copiar el mundo real por completo.

## 2. Clase, objeto, instancia y referencia

Una **clase** define un tipo de objeto. Una **instancia** es un objeto concreto creado a partir de esa clase. En este contexto, decir «objeto de `Persona`» e «instancia de `Persona`» expresa la misma relación.

La comparación de tus notas con una plantilla, o con la idea de algo frente a sus ejemplos concretos, sirve para empezar. Conviene añadir un matiz: una instancia no contiene una copia completa del código de la clase. Tiene sus propios datos de instancia y utiliza los métodos definidos en su clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("María", 35)
persona2 = Persona("Juan", 28)

print(persona1.nombre)
print(persona2.nombre)
print(type(persona1))
print(isinstance(persona1, Persona))
print(persona1 is persona2)
```

Las dos primeras líneas muestran `María` y `Juan`; la comprobación de tipo muestra una clase cuyo nombre termina en `Persona`. `isinstance(...)` devuelve `True`; `persona1 is persona2`, `False`, porque se han creado dos objetos distintos.

| Expresión | Qué representa |
|---|---|
| `Persona` | La clase; también es un objeto de Python. |
| `Persona("María", 35)` | Una llamada que crea e inicializa una instancia. |
| `persona1` | Un nombre que referencia esa instancia. |
| `persona1.nombre` | El atributo `nombre` de esa instancia. |
| `persona2` | Otro nombre que aquí referencia otra instancia. |

**Precisión de vocabulario:** habitualmente diremos «el objeto `persona1`», pero `persona1` es el nombre que permite acceder a él. Esta distinción importa cuando dos nombres apuntan al mismo objeto; lo veremos con las direcciones.

## 3. Definir una clase e inicializar sus objetos

### 3.1. La forma mínima

```python
class Persona:
    pass

persona = Persona()
print(isinstance(persona, Persona))
```

`class` inicia la definición; `Persona` es el nombre elegido; `:` abre el bloque. `pass` permite dejarlo vacío de momento. La convención es usar nombres de clase como `Persona`, `Direccion` o `ArticuloEditorial`, y nombres de métodos como `mostrar_info`.

No es obligatorio escribir un `__init__` vacío. La clase mínima anterior se puede instanciar sin que lo definas. Más adelante, cuando haya herencia, podrá utilizarse un inicializador heredado.

### 3.2. Añadir un estado inicial con __init__

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona = Persona("María", 35)
print(persona.nombre)
print(persona.edad)
```

Al hacer `Persona("María", 35)`, Python prepara una instancia y llama a `__init__` para inicializarla. En esta llamada, `nombre` recibe `"María"` y `edad` recibe `35`.

| Parte | Función |
|---|---|
| `def __init__(...)` | Define el inicializador. Son dos guiones bajos antes y después de `init`. |
| `nombre`, `edad` | Parámetros que reciben valores durante la llamada. |
| `self.nombre`, `self.edad` | Atributos que conservan los valores en la instancia. |
| `Persona("María", 35)` | Llama a la clase con los argumentos de inicialización. |

**Aclaración al término «constructor»:** en clase se utiliza ese nombre para `__init__`. Técnicamente, `__init__` inicializa una instancia ya creada; la creación corresponde a `__new__`. Basta conocer esta distinción: para estos ejercicios debes escribir `__init__`, no implementar `__new__`.

`__init__` no devuelve el objeto mediante `return self`. Su retorno debe ser `None`, como ocurre al terminar sin `return` explícito. La expresión `Persona(...)` es la que entrega la instancia al código que la llama.

### 3.3. No poner los parámetros de instancia en la cabecera de class

La redacción de la p. 70 puede inducir a mezclar dos sintaxis:

```text
class Persona:                         # Definición de la clase.
    def __init__(self, nombre, edad):  # Parámetros de inicialización.
        ...

persona = Persona("María", 35)         # Argumentos al crear la instancia.
```

En estas clases sencillas, `nombre` y `edad` se declaran en `__init__`, no en `class Persona(nombre, edad)`. Los paréntesis de la cabecera de una clase se utilizarán, entre otras cosas, para indicar clases base cuando estudiéis herencia.

### 3.4. «Solo se permite un constructor»

La idea útil para el curso es que no puedes definir varios métodos llamados `__init__` y esperar que Python elija uno según el número o el tipo de argumentos. Si escribes dos definiciones con ese mismo nombre en el cuerpo de la clase, la última sustituye a la anterior.

Para admitir distintas formas de llamada puedes empezar usando parámetros con valores por defecto:

```python
class Persona:
    def __init__(self, nombre, edad=None):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("María", 35)
persona2 = Persona("Juan")

print(persona1.edad)  # 35
print(persona2.edad)  # None
```

Es un único inicializador con un argumento opcional. `None` significa aquí «edad no indicada». No hace falta estudiar otras formas de construcción todavía.

## 4. Entender self y el acceso con punto

`self` es el nombre convencional del primer parámetro de un método de instancia. Referencia el objeto concreto sobre el que se está trabajando; no la clase en general.

La imagen de «señalarse a sí mismo» que anotaste es útil. Para escribir Python, piensa en una **referencia al objeto**, sin necesitar operaciones con direcciones de memoria.

Cuando llamas a un método a través de una instancia, Python proporciona esa instancia como primer argumento. Por eso escribes `persona.mostrar_info()` y no tienes que pasar `self` manualmente.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, edad: {self.edad}")

persona1 = Persona("María", 35)
persona2 = Persona("Juan", 28)

persona1.cambiar_nombre("María José")
persona1.mostrar_info()
persona2.mostrar_info()
```

Salida:

```text
Nombre: María José, edad: 35
Nombre: Juan, edad: 28
```

En la primera llamada, `self` referencia `persona1`. En la segunda, referencia `persona2`. El código del método es el mismo, pero consulta los datos de la instancia que recibe.

### 4.1. nombre y self.nombre cumplen papeles diferentes

En `self.nombre = nombre`, lo que está a la derecha es el parámetro recibido; lo que está a la izquierda es el atributo que creas o actualizas.

```text
def __init__(self, nombre):
    self.nombre = nombre
```

`self.nombre` es el atributo; `nombre`, el parámetro local.

No tienen que llamarse igual, aunque usar el mismo nombre suele ser claro. También podría escribirse `def __init__(self, nombre_inicial)` y después `self.nombre = nombre_inicial`.

Si escribes solo `nombre = nombre_inicial`, no estás guardándolo como atributo de la instancia. Esa variable local no te dará después acceso mediante `persona.nombre`.

### 4.2. Leer y modificar con punto

Fuera de los métodos escribes `persona.nombre`; dentro, para la instancia actual, `self.nombre`.

```text
persona.nombre                 # Leer el atributo.
persona.nombre = "María José"  # Asignarle otro valor.
persona.mostrar_info()         # Acceder al método y llamarlo.
```

El punto es el operador de acceso a atributos. En un caso obtienes un dato; en otro obtienes un método que puedes ejecutar con `()`.

**Matiz de vocabulario:** la profesora utiliza «propiedad», «atributo», «campo» o «variable de instancia» para estos datos. Aquí usamos principalmente **atributo de instancia**. En Python existe además `property`, un mecanismo específico que no se ha utilizado en estos ejemplos.

## 5. Métodos: datos, acciones y valores devueltos

Un método de instancia se parece a una función, pero recibe como primer argumento la instancia sobre la que opera. En las clases del curso se define con `def` dentro de la clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def nombre_mayusculas(self) -> str:
        return self.nombre.upper()

    def cumplir_anios(self) -> None:
        self.edad += 1

    def mostrar_info(self) -> None:
        print(f"Nombre: {self.nombre}, edad: {self.edad}")

persona = Persona("María", 35)
nombre_transformado = persona.nombre_mayusculas()
print(nombre_transformado)
print(persona.nombre)
persona.cumplir_anios()
persona.mostrar_info()
```

Salida:

```text
MARÍA
María
Nombre: María, edad: 36
```

| Método | Qué hace | ¿Cambia el estado? | ¿Qué devuelve? |
|---|---|---|---|
| `nombre_mayusculas()` | Calcula una versión del nombre. | No. | Un `str`. |
| `cumplir_anios()` | Incrementa la edad. | Sí. | `None`. |
| `mostrar_info()` | Escribe la información en pantalla. | No. | `None`. |

Que un método utilice datos del objeto no implica que los modifique. `upper()` devuelve una cadena nueva; `self.nombre` sigue siendo `"María"` porque no le hemos asignado el resultado.

### 5.1. Anotaciones de tipo

En `def nombre_mayusculas(self) -> str:`, `-> str` indica el tipo de retorno previsto. En `def mostrar_info(self) -> None:`, `-> None` indica que no se espera un resultado útil de retorno.

La anotación no realiza la operación: `return` entrega un valor y `print` lo muestra. Tampoco convierte automáticamente datos ni impide por sí sola que se pase otro tipo. Lo mismo ocurre con un parámetro anotado como `vip: bool`.

Las anotaciones ayudan a leer el código y a las herramientas de análisis. Las validaciones que necesites durante la ejecución deben programarse.

### 5.2. Un método puede utilizar otros métodos

Dentro de un método puedes llamar a otro de la misma instancia con `self.otro_metodo()`. En el ejemplo editorial lo utilizaremos para separar la comprobación de un texto de la acción que cambia su estado.

## 6. El ejemplo Persona de la profesora, paso a paso

**Fuente:** `Ejemplo14_POO/clases_objetos.py` y tus notas de `modulo5.md`. Se conservan la estructura y las operaciones; se normalizan las tildes de los nombres en este ejemplo de estudio.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def nombre_mayusculas(self) -> str:
        return self.nombre.upper()

    def mostrar_info(self) -> None:
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

persona1 = Persona("María", 35)
persona2 = Persona("Juan", 28)

persona1.nombre = "María José"
persona1.edad = 36

print(persona1.nombre_mayusculas())
persona1.mostrar_info()
persona2.mostrar_info()
```

Salida:

```text
MARÍA JOSÉ
Nombre: María José, Edad: 36
Nombre: Juan, Edad: 28
```

Recorrido de ejecución:

1. Se ejecuta la definición de `Persona`. Queda disponible la clase con sus métodos; aún no se ha creado ninguna persona.
2. `Persona("María", 35)` crea e inicializa una instancia; el nombre `persona1` queda asociado a ella.
3. La segunda llamada crea otra instancia con otros datos.
4. Las dos asignaciones cambian atributos de `persona1`; no afectan a `persona2`.
5. `nombre_mayusculas()` devuelve un texto y `print(...)` lo muestra.
6. Cada llamada a `mostrar_info()` imprime los datos de su propia instancia.

**Corrección de tus notas:** primero creas `persona1`, pero una de las llamadas anotadas utiliza `persona.mostrar_info()`. Debe usarse el nombre que realmente esté definido. Si no existe `persona`, obtendrás `NameError`; en el ejemplo anterior es `persona1.mostrar_info()`.

Tampoco hace falta afirmar que un método solo puede encontrarse después de crear una instancia: puede consultarse en la clase. Para estos métodos de instancia, lo normal es llamarlos desde el objeto para que Python aporte `self`. Como aclaración, `Persona.mostrar_info(persona1)` produce aquí el mismo resultado que `persona1.mostrar_info()`.

## 7. Mostrar un método, llamarlo y mostrar su resultado

Esta es la duda que aparece comentada en tu `ejercicio5-2.py`. Las tres formas siguientes son válidas, pero hacen cosas diferentes:

```python
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Cliente: {self.nombre}")

cliente = Cliente("Cliente de ejemplo")

print("1. Mostrar el método:")
print(cliente.mostrar_info)

print("2. Llamar al método:")
cliente.mostrar_info()

print("3. Mostrar lo que devuelve:")
print(cliente.mostrar_info())
```

| Expresión | Qué ocurre |
|---|---|
| `print(cliente.mostrar_info)` | Muestra una representación del método, parecida a `<bound method ...>`. No ejecuta su cuerpo. |
| `cliente.mostrar_info()` | Llama al método; aparece `Cliente: Cliente de ejemplo`. |
| `print(cliente.mostrar_info())` | Primero se ejecuta el método y aparece la información; después el `print` exterior muestra `None`. |

**Corrección:** `print(cli1.mostrarInfo)` no falla simplemente porque el método contenga un `print`. La expresión funciona, pero muestra el objeto método en lugar de llamar a su contenido. El problema es la ausencia de `()` para ejecutarlo.

El `None` de la tercera forma aparece porque `mostrar_info` termina sin `return` explícito. No es una segunda información del cliente ni una excepción.

### 7.1. Alternativa para reutilizar la información

Si quieres usar la descripción en una pantalla, un mensaje o un informe, puede ser más útil devolver un texto:

```python
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_info(self) -> str:
        return f"Cliente: {self.nombre}"

cliente = Cliente("Cliente de ejemplo")
descripcion = cliente.obtener_info()
print(descripcion)
print(descripcion.upper())
```

Ambos diseños sirven. En el ejercicio de clase, `mostrarInfo()` imprime directamente. En una aplicación suele interesar separar la obtención de datos de su presentación.

## 8. Ejercicio 1: calculadora de la profesora

**Fuente:** `Ejemplo14_POO/ejercicio1.py`.

**Enunciado:** crear una clase `Calculadora` con métodos para sumar, restar, multiplicar y dividir; pedir dos números; llamar a los cuatro métodos y mostrar los resultados. La solución de la profesora incorpora capturas para entradas no numéricas y división entre cero.

En su diseño, la calculadora no guarda los dos números como atributos. Cada método recibe los operandos al llamarlo.

```python
class Calculadora:
    def sumar(self, n1, n2):
        return n1 + n2

    def restar(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1 / n2

try:
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))

    calculadora = Calculadora()
    print(f"Suma: {calculadora.sumar(numero1, numero2)}")
    print(f"Resta: {calculadora.restar(numero1, numero2)}")
    print(f"Multiplicación: {calculadora.multiplicar(numero1, numero2)}")
    print(f"División: {calculadora.dividir(numero1, numero2)}")
except ValueError:
    print("Debes introducir números enteros.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

Con `8` y `2` obtienes:

```text
Suma: 10
Resta: 6
Multiplicación: 16
División: 4.0
```

### 8.1. Por qué no aparece __init__

Esta clase no necesita una inicialización propia. Se puede crear con `Calculadora()` y después pasar operandos a sus métodos. No es necesario añadir un inicializador que solo contenga `pass`.

`self` aparece en los métodos porque son métodos de instancia, aunque en esta versión no lean atributos de la calculadora. Para una aplicación real, estas operaciones tan sencillas también podrían implementarse como funciones. La clase se utiliza aquí para practicar la sintaxis de POO.

### 8.2. Conexión con las excepciones del módulo 4

| Entradas | Qué sucede |
|---|---|
| `8`, `2` | Se muestran las cuatro operaciones. |
| `8`, `0` | Se muestran suma, resta y multiplicación; al dividir se captura `ZeroDivisionError`. |
| `ocho` | Falla la primera conversión; se captura `ValueError` y no se pregunta el segundo número. |
| `8.5` | `int("8.5")` produce `ValueError`; esta versión pide enteros. |

Para admitir decimales puedes usar `float(input(...))`, como hiciste tú. La entrada debe utilizar el formato que acepta `float`, por ejemplo `8.5`; `8,5` no se convierte directamente.

El `try` no repite las preguntas. Para volver a intentarlo habría que añadir un bucle. Tampoco recupera las instrucciones que quedaran después del punto donde se produjo el error.

**Pequeña corrección de presentación:** el original repite «Introduce numero1» en las dos preguntas. Aquí se distingue entre primer y segundo número; el cálculo original no dependía del texto del mensaje.

## 9. Tu calculadora: guardar datos en el objeto

**Fuente:** tu [ejercicio5-1.py](ejercicio5-1.py).

Tu solución utiliza otra idea válida: el objeto conserva los operandos desde su creación.

```text
def __init__(self, num1: float, num2: float):
    self.num1 = num1
    self.num2 = num2

def sumar(self, num1, num2) -> float:
    return self.num1 + self.num2
```

En el método `sumar` declaras `num1` y `num2`, pero no los utilizas. La operación usa `self.num1` y `self.num2`, los atributos que guardaste antes.

**No impide que tu programa se ejecute**, porque pasas otra vez los mismos números. El inconveniente aparece si pasas otros: un objeto creado con `8` y `2`, al llamar a tu versión de `sumar(100, 200)`, devuelve `10`, no `300`. Los argumentos `100` y `200` se ignoran.

### 9.1. Versión coherente con tu diseño

Si los números pertenecen al estado del objeto, los métodos no necesitan recibirlos otra vez:

```python
class Calculadora:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def sumar(self) -> float:
        return self.num1 + self.num2

    def restar(self) -> float:
        return self.num1 - self.num2

    def multiplicar(self) -> float:
        return self.num1 * self.num2

    def dividir(self) -> float:
        return self.num1 / self.num2

try:
    numero1 = float(input("Introduce un número: "))
    numero2 = float(input("Introduce otro número: "))

    calculadora = Calculadora(numero1, numero2)
    print(f"La suma es {calculadora.sumar()}")
    print(f"La resta es {calculadora.restar()}")
    print(f"La multiplicación es {calculadora.multiplicar()}")
    print(f"La división es {calculadora.dividir()}")
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

Con `8` y `2` aparecen `10.0`, `6.0`, `16.0` y `4.0`. La diferencia respecto a la solución de la profesora está en dónde se reciben y conservan los datos, no en el significado de las cuatro operaciones.

### 9.2. Comparar ambos diseños

| Decisión | Versión de la profesora | Tu versión ajustada |
|---|---|---|
| Crear el objeto | `Calculadora()` | `Calculadora(numero1, numero2)` |
| Conservar operandos | No los guarda en atributos. | Usa `self.num1` y `self.num2`. |
| Sumar | `calculadora.sumar(8, 2)` | `calculadora.sumar()` |
| Reutilizar con otros números | Pasarlos en la siguiente llamada. | Cambiar el estado o crear otro objeto. |

La pregunta para decidir es: **¿estos valores deben permanecer asociados al objeto, o solo se necesitan para esta operación?** Evita pedirlos dos veces si uno de los juegos de datos no se utiliza.

Tu captura final `except Exception as error` es una captura amplia. Puede resultar útil para mostrar un fallo inesperado, pero no es obligatoria y puede esconder un error de programación durante el aprendizaje. En esta versión basta atender las dos excepciones esperadas.

## 10. Ejercicio 2: la clase Cliente

**Fuentes:** primera parte del enunciado de `Ejemplo14_POO/ejercicio2.py` y primera versión de tu [ejercicio5-2.py](ejercicio5-2.py).

Se pide representar un cliente con nombre, CIF y condición VIP, y mostrar dos clientes. Conservamos la etiqueta `cif` utilizada en clase; los identificadores de los ejemplos son datos ficticios sin validación.

```python
class Cliente:
    def __init__(self, nombre: str, cif: str, vip: bool):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip

    def mostrar_info(self) -> None:
        print(f"Cliente: {self.nombre}, CIF: {self.cif}, VIP: {self.vip}")

cliente1 = Cliente("Frutería Paco", "B-12345678", False)
cliente2 = Cliente("Ferretería Amparo", "B-98765432", True)

cliente1.mostrar_info()
cliente2.mostrar_info()
```

La profesora y tu ejercicio llaman al método `mostrarInfo`. En estos apuntes se emplea `mostrar_info`, siguiendo la convención habitual de Python. Ambos nombres son válidos, pero hay que usar el mismo al definir y llamar: Python no los considera equivalentes.

### 10.1. Los booleanos son valores, no etiquetas

`True` y `False` no llevan comillas. `"False"` es una cadena no vacía y se considera verdadera en una condición. Tampoco `bool("False")` devuelve `False`: devuelve `True`.

Por tanto, escribir `vip: bool` no transforma automáticamente el texto que venga de un formulario. Si en el futuro lees una respuesta textual tendrás que interpretarla, por ejemplo comparando `respuesta.strip().lower()` con `"sí"` o con el conjunto de respuestas que decidas admitir.

### 10.2. Dos definiciones de Cliente en el mismo archivo

En tu ejercicio aparece primero una clase `Cliente` sin dirección y después otra versión con dirección. Es comprensible al tomar apuntes de forma progresiva, pero debes tener en cuenta el orden:

1. Los primeros objetos se crean con la primera clase.
2. La segunda definición asocia el nombre `Cliente` a una clase nueva.
3. Los objetos que ya existían no se transforman automáticamente para adquirir una dirección.
4. Las siguientes llamadas a `Cliente(...)` utilizan la nueva definición.

En la versión final de un programa conservarías una definición de `Cliente` y crearías los objetos con su estructura definitiva. Aquí las dos versiones se presentan como bloques independientes para estudiar la ampliación.

## 11. Composición: Cliente tiene una Direccion

La **composición**, en el sentido práctico utilizado por la profesora, consiste en construir un objeto usando otros objetos como parte de sus atributos.

Un cliente **tiene una** dirección. Por eso `Cliente` puede conservar una instancia de `Direccion` en su atributo `direccion`.

| Objeto | Atributos |
|---|---|
| `Direccion` | `calle`, `numero`, `poblacion`. |
| `Cliente` | `nombre`, `cif`, `vip`, `direccion`. |
| `cliente.direccion` | Es el objeto `Direccion`, no solo el nombre de la calle. |

La p. 71 introduce la idea de dividir un problema en componentes manejables. La p. 72 la concreta mediante objetos que contienen referencias a otros objetos. No necesitas herencia para hacerlo.

### 11.1. Solución completa

**Fuente:** solución de la profesora y ampliación de tu `ejercicio5-2.py`. Se añaden anotaciones y se unifican nombres; el funcionamiento es el mismo.

```python
class Direccion:
    def __init__(self, calle: str, numero: int, poblacion: str):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

class Cliente:
    def __init__(self, nombre: str, cif: str, vip: bool, direccion: Direccion):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip
        self.direccion = direccion

    def mostrar_info(self) -> None:
        print(
            f"Nombre: {self.nombre}, CIF: {self.cif}, VIP: {self.vip}. "
            f"Dirección: {self.direccion.calle}, "
            f"{self.direccion.numero} ({self.direccion.poblacion})"
        )

direccion1 = Direccion("Mayor", 5, "Madrid")
cliente1 = Cliente("Frutería Paco", "B-12345678", False, direccion1)

cliente2 = Cliente(
    "Ferretería Amparo",
    "B-98765432",
    True,
    Direccion("Diagonal", 36, "Barcelona"),
)

cliente1.mostrar_info()
cliente2.mostrar_info()
print(cliente1.direccion.poblacion)
```

Salida:

```text
Nombre: Frutería Paco, CIF: B-12345678, VIP: False. Dirección: Mayor, 5 (Madrid)
Nombre: Ferretería Amparo, CIF: B-98765432, VIP: True. Dirección: Diagonal, 36 (Barcelona)
Madrid
```

Hay dos formas de preparar la dirección: crearla antes y pasar el nombre `direccion1`, o crearla directamente dentro de la llamada a `Cliente`. En ambos casos el argumento es un objeto `Direccion`.

La anotación `direccion: Direccion` describe lo esperado; no comprueba por sí sola que se reciba ese tipo. Si pasas una cadena, la asignación se hará, pero después la búsqueda de `.calle` en esa cadena fallará.

### 11.2. Composición y agregación: una precisión opcional

En diseño de software se puede distinguir entre una composición con relación de propiedad y una agregación que permite compartir partes independientes. El curso llama composición a este ejemplo. Para seguirlo, quédate con «un objeto tiene otro objeto como atributo»; el código de Python mostrado no impone por sí solo un ciclo de vida exclusivo a la dirección.

## 12. Recorrer atributos encadenados y compartir referencias

### 12.1. Qué significa cliente1.direccion.poblacion

Se evalúa de izquierda a derecha:

1. `cliente1` permite acceder al objeto cliente.
2. `.direccion` obtiene el objeto dirección que tiene asociado.
3. `.poblacion` obtiene el atributo de ese segundo objeto.

Tu comparación con entrar en subcarpetas ayuda a visualizar los pasos, pero no se están recorriendo carpetas del ordenador: se accede a atributos de objetos.

Para modificarlo usarías `cliente1.direccion.poblacion = "Rivas"`. No has cambiado el cliente entero; has cambiado un atributo del objeto al que conduce su dirección.

### 12.2. Asignar no hace una copia automática

```python
class Direccion:
    def __init__(self, calle, numero, poblacion):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

direccion = Direccion("Mayor", 5, "Madrid")
cliente1 = Cliente("Cliente A", direccion)
cliente2 = Cliente("Cliente B", direccion)

print(cliente1.direccion is cliente2.direccion)
cliente1.direccion.poblacion = "Rivas"
print(cliente2.direccion.poblacion)

cliente2.direccion = Direccion("Diagonal", 36, "Barcelona")
print(cliente1.direccion.poblacion)
print(cliente2.direccion.poblacion)
```

Salida:

```text
True
Rivas
Rivas
Barcelona
```

Al principio ambos clientes referencian la misma dirección. Por eso el cambio de población se ve a través de los dos. Después se asigna a `cliente2.direccion` una dirección nueva y dejan de compartir esa parte.

**Regla de estudio:** asignar un objeto a una variable o atributo no implica duplicarlo. Esta idea conecta con las listas mutables del módulo 3.

### 12.3. Elegir nombres que no oculten funciones de Python

El original y tus notas utilizan `dir` como nombre para una dirección. Es válido, pero oculta en ese ámbito la función incorporada `dir()`. Utiliza `direccion`, `direccion1` o `direccion_cliente` para que el nombre sea claro y no se produzca esa coincidencia.

Lo mismo conviene recordar con nombres como `list`, `str`, `sum` o `input`.

## 13. Punto y Triangulo: los ejemplos del PDF

**Fuente:** pp. 70 y 72. Parte del código está incrustado como imagen en las diapositivas; se ha revisado visualmente. Aquí se adapta a minúsculas para atributos y métodos y se usan f-strings para que la salida resulte clara.

### 13.1. Un punto conserva dos coordenadas

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_punto(self):
        print(f"El punto es ({self.x}, {self.y})")

punto = Punto(4, 6)
punto.mostrar_punto()
```

Salida: `El punto es (4, 6)`.

El PDF utiliza atributos `X`, `Y` y un método `MostrarPunto`. Son nombres válidos, pero distintos de `x`, `y` y `mostrar_punto`: no se pueden mezclar las dos convenciones al llamar.

### 13.2. Un triángulo contiene tres puntos

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar_punto(self):
        print(f"El punto es ({self.x}, {self.y})")

class Triangulo:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def mostrar_vertices(self):
        self.vertice1.mostrar_punto()
        self.vertice2.mostrar_punto()
        self.vertice3.mostrar_punto()

v1 = Punto(3, 4)
v2 = Punto(6, 8)
v3 = Punto(9, 2)
triangulo = Triangulo(v1, v2, v3)

triangulo.mostrar_vertices()
print(triangulo.vertice2.x)
```

Salida:

```text
El punto es (3, 4)
El punto es (6, 8)
El punto es (9, 2)
6
```

La estructura es la misma que con cliente y dirección: `triangulo.vertice2` obtiene otro objeto; después puedes consultar su atributo `.x` o llamar a su método `.mostrar_punto()`.

Este ejemplo representa tres vértices. No calcula el área ni comprueba que los puntos formen un triángulo válido: esas operaciones requerirían código adicional.

## 14. Unir objetos con listas y diccionarios

Los objetos no sustituyen a las colecciones del módulo 3. Puedes guardar objetos en una lista, recorrerlos y utilizar sus atributos en condiciones.

```python
class Cliente:
    def __init__(self, nombre, cif, vip):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip

clientes = [
    Cliente("Frutería Paco", "B-12345678", False),
    Cliente("Ferretería Amparo", "B-98765432", True),
]

for cliente in clientes:
    if cliente.vip:
        print(f"Cliente VIP: {cliente.nombre}")

clientes_por_cif = {cliente.cif: cliente for cliente in clientes}
print(clientes_por_cif["B-12345678"].nombre)
```

Salida:

```text
Cliente VIP: Ferretería Amparo
Frutería Paco
```

| Necesidad | Estructura útil |
|---|---|
| Reunir los datos y operaciones de un cliente | Una clase `Cliente`. |
| Mantener varios clientes y recorrerlos | Una lista de objetos. |
| Buscar un cliente por identificador | Un diccionario cuya clave sea ese identificador. |
| Representar datos sencillos recibidos de un JSON | Un diccionario puede ser suficiente. |

La comprensión de diccionario utiliza sintaxis ya estudiada. Si dos clientes tienen el mismo CIF, el último sustituirá al anterior en ese diccionario: crear la clase no impone automáticamente identificadores únicos.

### 14.1. Complemento opcional: una lista propia de cada instancia

Cuando un objeto deba conservar una lista que le pertenece, inicialízala para cada instancia:

```python
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def matricular(self, nombre):
        self.alumnos.append(nombre)

curso_python = Curso("Python")
curso_ia = Curso("IA")
curso_python.matricular("Ana")

print(curso_python.alumnos)
print(curso_ia.alumnos)
```

Salida: `['Ana']` y `[]`.

Si declarases `alumnos = []` directamente dentro de la clase, fuera de `__init__`, estarías creando una lista como atributo de clase. Una mutación de esa lista a través de una instancia podría verse en las demás. No necesitas profundizar ahora en atributos de clase: recuerda colocar en `self` los datos que quieras conservar por instancia.

## 15. Errores frecuentes y cómo reconocerlos

| Situación | Resultado habitual | Qué revisar |
|---|---|---|
| `Persona("María")` cuando se exige también `edad` | `TypeError` por argumento ausente. | Firma de `__init__` y llamada. |
| Definir `init` o `_init_` en lugar de `__init__` | No se utiliza como inicializador; al pasar argumentos puede aparecer `TypeError`. | Dos guiones bajos a cada lado. |
| Olvidar `self` en un método de instancia | `TypeError` al llamar con una instancia. | Primer parámetro del método. |
| Guardar `nombre = ...` sin `self` y luego leer `persona.nombre` | `AttributeError` si no se creó ese atributo. | Dónde se guarda el dato. |
| Usar `persona` cuando el objeto se llamó `persona1` | `NameError`, si `persona` no está definido. | Nombre de la variable. |
| Llamar a `mostrar_info` cuando se definió `mostrarInfo` | `AttributeError`. | Coincidencia exacta del nombre. |
| Escribir `cliente.mostrar_info` sin paréntesis | Se obtiene el método; no se ejecuta. | Añadir `()` cuando quieres llamarlo. |
| Usar `print` sobre el resultado de un método que solo imprime | Aparece también `None`. | Diferencia entre imprimir y devolver. |
| Pasar texto donde se espera una `Direccion` | Puede aparecer `AttributeError` al buscar `.calle`. | Tipo real del argumento. |
| Mezclar atributos guardados y parámetros que no se usan | Puede ejecutarse con resultados inesperados. | Qué valores usa realmente el cálculo. |

### 15.1. No poner el mismo nombre a un dato y a un método

Esto conecta con el error de «objeto no invocable» que puede aparecer al diseñar clases:

```python
class Coche:
    def __init__(self):
        self.arrancar = False

    def arrancar(self):
        print("Motor encendido")

coche = Coche()

try:
    coche.arrancar()
except TypeError:
    print("El atributo booleano ha ocultado el método arrancar.")
```

`self.arrancar = False` crea un atributo que oculta el método con ese mismo nombre al acceder desde la instancia. Entonces se intenta llamar a `False` con `()` y aparece `TypeError`.

Una versión clara separa el nombre del estado y el de la acción:

```python
class Coche:
    def __init__(self):
        self.encendido = False

    def arrancar(self):
        self.encendido = True

coche = Coche()
coche.arrancar()
print(coche.encendido)
```

Salida: `True`. `encendido` describe un dato; `arrancar` describe una acción.

### 15.2. Preguntas para depurar sin cambiarlo todo

1. ¿Estoy usando la clase o una instancia?
2. ¿El nombre y las mayúsculas coinciden con la definición?
3. ¿Tengo un dato, un método o el resultado de llamar al método?
4. ¿Qué recibe la llamada y qué datos consulta su cuerpo?
5. ¿Este atributo pertenece al objeto actual o a otro objeto contenido?
6. ¿Estoy cambiando un objeto compartido por varias referencias?

Usa `print(type(objeto))` o muestra un atributo concreto para comprobar tus suposiciones. No hace falta añadir una captura genérica de excepciones para cada error de diseño: conviene ver el traceback y corregir su causa.

## 16. Aplicación a tu ámbito: un borrador editorial

**Complemento opcional.** Este ejemplo conecta clases, composición, listas, cadenas y excepciones con tu trabajo de escritura y automatización. Representa un borrador, sin servicios externos ni modelos de IA.

La idea es que un borrador **tiene una** autora, conserva título y texto, y puede pasar de «borrador» a «revisado» cuando cumple una comprobación mínima definida para el ejercicio.

```python
class Autora:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Articulo:
    def __init__(self, titulo, texto, autora):
        self.titulo = titulo
        self.texto = texto
        self.autora = autora
        self.estado = "borrador"

    def contar_palabras(self) -> int:
        return len(self.texto.split())

    def tiene_contenido(self) -> bool:
        return bool(self.titulo.strip()) and bool(self.texto.strip())

    def marcar_revisado(self) -> None:
        if not self.tiene_contenido():
            raise ValueError("Faltan el título o el texto.")
        self.estado = "revisado"

    def obtener_ficha(self) -> str:
        return (
            f"{self.titulo} | Autora: {self.autora.nombre} | "
            f"Palabras: {self.contar_palabras()} | Estado: {self.estado}"
        )

autora = Autora("Estela", "Divulgación y narrativa")
articulos = [
    Articulo("Primera revisión", "Texto de prueba para revisar hoy.", autora),
    Articulo("Segundo borrador", "   ", autora),
]

for articulo in articulos:
    try:
        articulo.marcar_revisado()
    except ValueError as error:
        print(f"Pendiente: {articulo.titulo}. {error}")
    else:
        print(articulo.obtener_ficha())
```

Salida:

```text
Primera revisión | Autora: Estela | Palabras: 6 | Estado: revisado
Pendiente: Segundo borrador. Faltan el título o el texto.
```

| Parte del código | Concepto que practica |
|---|---|
| `self.titulo`, `self.texto`, `self.estado` | Atributos de instancia. |
| `self.autora = autora` | Composición mediante otro objeto. |
| `self.autora.nombre` | Acceso encadenado. |
| `self.contar_palabras()` | Un método que devuelve un cálculo. |
| `self.tiene_contenido()` | Un método que consulta el estado y devuelve un booleano. |
| `self.estado = "revisado"` | Cambio de estado. |
| `raise ValueError(...)` | Comunicar que no se cumple una condición. |
| Lista y bucle | Procesar varios objetos. |

Esta comprobación solo exige que título y texto no estén vacíos. No verifica la calidad, la exactitud ni la revisión editorial real; aquí «revisado» es un estado didáctico que cambiamos por una regla muy simple. `split()` cuenta grupos separados por espacios en blanco, no realiza un análisis lingüístico avanzado.

### 16.1. Cómo conecta con lo que estudiarás después

El encapsulamiento ayudará a definir cómo se permiten los cambios de estado. La lectura y escritura de archivos permitirá guardar datos entre ejecuciones: por ahora, crear un objeto no lo guarda automáticamente en disco. Los módulos permitirán separar `Articulo` y `Autora` en archivos importables, como ya hiciste con las funciones del módulo 4.

En aplicaciones y agentes también encontrarás clases que representan mensajes, documentos, clientes de servicios o resultados. No necesitas aprender ahora una biblioteca concreta: saber leer `objeto.metodo(...)` y reconocer sus atributos ya te permitirá orientarte mejor en esas APIs.

## 17. Práctica guiada con soluciones

Estas prácticas consolidan la parte de hoy. Intenta resolverlas antes de leer la solución; no son preguntas confirmadas de examen.

### 17.1. Predecir una salida: alias o copia

¿Qué muestra el siguiente programa? ¿Cuántas instancias de `Persona` se han creado?

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

persona1 = Persona("Ana")
persona2 = persona1
persona2.nombre = "Eva"

print(persona1.nombre)
print(persona1 is persona2)
```

**Solución:** muestra `Eva` y `True`. Se ha creado una instancia; los dos nombres la referencian. `persona2 = persona1` no crea una segunda persona ni una copia.

### 17.2. Un taller que conserva sus datos

**Enunciado:** crea `Taller` con `nombre`, `plazas` e `inscritos`. Al crearlo, hay cero inscritos. Añade `plazas_libres()` y `reservar_plaza()`. El segundo método debe lanzar `ValueError` si ya está completo. Usa un taller de dos plazas e intenta reservar tres veces.

```python
class Taller:
    def __init__(self, nombre, plazas):
        if plazas < 0:
            raise ValueError("El número de plazas no puede ser negativo.")
        self.nombre = nombre
        self.plazas = plazas
        self.inscritos = 0

    def plazas_libres(self) -> int:
        return self.plazas - self.inscritos

    def reservar_plaza(self) -> None:
        if self.plazas_libres() <= 0:
            raise ValueError("El taller está completo.")
        self.inscritos += 1

taller = Taller("Introducción a la acuarela", 2)

for intento in range(3):
    try:
        taller.reservar_plaza()
    except ValueError as error:
        print(error)
    else:
        print(f"Reserva confirmada. Quedan {taller.plazas_libres()} plazas.")
```

Salida:

```text
Reserva confirmada. Quedan 1 plazas.
Reserva confirmada. Quedan 0 plazas.
El taller está completo.
```

El ejemplo da por hecho que `plazas` es un entero. La comprobación de valores negativos no es una validación de todos los tipos posibles. Tampoco impide que otro código modifique directamente `inscritos`; ese problema conecta con encapsulamiento.

### 17.3. Una inscripción que utiliza otros objetos

**Enunciado:** crea `Participante`, `Taller` e `Inscripcion`. La inscripción debe conservar un participante y un taller. Su método `obtener_resumen()` devolverá un texto como `Ana se ha inscrito en Python inicial`.

```python
class Participante:
    def __init__(self, nombre):
        self.nombre = nombre

class Taller:
    def __init__(self, titulo):
        self.titulo = titulo

class Inscripcion:
    def __init__(self, participante, taller):
        self.participante = participante
        self.taller = taller

    def obtener_resumen(self) -> str:
        return (
            f"{self.participante.nombre} se ha inscrito "
            f"en {self.taller.titulo}"
        )

participante = Participante("Ana")
taller = Taller("Python inicial")
inscripcion = Inscripcion(participante, taller)
print(inscripcion.obtener_resumen())
```

**Solución razonada:** `Inscripcion` conserva dos objetos. No necesita copiar en atributos separados el nombre del participante y el título del taller: accede a ellos a través de las referencias. Si esos objetos cambian, el resumen consultará sus valores actuales. La creación de esta inscripción no implementa por sí sola un sistema de reservas ni controla plazas.

### 17.4. Explicar la calculadora sin mirar

Responde en voz alta:

1. ¿Por qué la profesora escribe `Calculadora()` y tú escribiste `Calculadora(numero1, numero2)`?
2. Si utilizas `self.num1`, ¿de dónde salió ese valor?
3. Si el método solo usa `self.num1` y `self.num2`, ¿necesita parámetros adicionales para los mismos operandos?
4. ¿Qué ocurre con las operaciones anteriores cuando se divide entre cero dentro del mismo `try`?

**Respuestas:** la primera versión recibe los operandos en cada método; la segunda los conserva desde `__init__`. Los atributos proceden de la inicialización. No hacen falta los parámetros adicionales si no se utilizan. Las operaciones ya ejecutadas y mostradas permanecen; la captura del error no deshace lo anterior.

## 18. Qué viene después en el módulo 5

Este es el mapa del PDF, no una afirmación de que ya se haya explicado oralmente. Tus notas de hoy terminan en composición y el ZIP disponible no contiene archivos de encapsulamiento, herencia o ficheros.

| Tema | Páginas | Idea inicial | Relación con lo de hoy |
|---|---|---|---|
| Encapsulamiento | 73–75 | Ofrecer operaciones para gestionar datos y mantener reglas del objeto. | Que un método controle un cambio, como reservar una plaza. |
| Herencia | 76–77 | Definir una clase a partir de otra y ampliar o adaptar su comportamiento. | Diferenciar «es un tipo de» de «tiene un». |
| Herencia múltiple | 78–79 | Una clase puede tener varias clases base. | Habrá que entender qué comportamiento se busca en cada base. |
| Ficheros | 80–83 | Leer, escribir y gestionar archivos de texto. | Conservar información más allá de una ejecución. |

### 18.1. Encapsulamiento: atención al término «privado»

El PDF presenta atributos y métodos con prefijo `__` como privados. **Aclaración:** en Python ese prefijo provoca una transformación del nombre para evitar colisiones; no crea una barrera absoluta de acceso ni protege información sensible. El prefijo simple `_` expresa por convención que algo es interno. `__init__`, con guiones bajos también al final, es un método especial y no un ejemplo de atributo privado.

Este matiz se ampliará con los ejemplos correspondientes. Encapsular no consiste solo en añadir guiones bajos: también implica definir qué operaciones ofrece un objeto para conservar sus reglas.

### 18.2. Composición frente a herencia

Un cliente **tiene una dirección**: composición en el vocabulario del curso. Una clase especializada que **es un tipo de otra** podría plantearse con herencia. No conviene usar herencia solo porque dos clases se relacionen.

Por ejemplo, una inscripción tiene un participante y un taller; no es un subtipo de participante ni de taller. Esa estructura encaja con los atributos que acabas de practicar.

## 19. Repaso de ideas y correcciones

### 19.1. Qué deberías poder hacer con esta parte

- Definir una clase sencilla y crear dos instancias con datos distintos.
- Explicar qué referencia `self` durante una llamada.
- Distinguir un parámetro local de un atributo de instancia.
- Acceder a un atributo, modificarlo y llamar a un método.
- Explicar la diferencia entre `print`, `return` y el retorno implícito `None`.
- Resolver la calculadora con uno de los dos diseños coherentes.
- Añadir una dirección como objeto dentro de un cliente.
- Leer una expresión como `cliente.direccion.poblacion`.
- Reconocer cuándo dos nombres o atributos referencian el mismo objeto.
- Combinar listas y diccionarios con objetos de tus clases.

### 19.2. Correcciones y precisiones del material

| Idea que puede confundir | Formulación para estudiar |
|---|---|
| «Cada objeto es una copia de la clase». | Cada instancia tiene sus datos y utiliza los métodos de su clase; no copia todo su código. |
| «Self es la clase misma». | En un método de instancia, `self` referencia la instancia que recibe la llamada. |
| «Los parámetros van en los paréntesis de class». | Aquí se declaran en `__init__` y se pasan al llamar a la clase. |
| «Init es el constructor». | En clase se llama así a `__init__`; técnicamente inicializa una instancia ya creada. |
| «Solo puede haber un constructor». | No se eligen automáticamente varias definiciones de `__init__`; puedes usar parámetros opcionales en una definición. |
| «Sin __init__ no se puede crear el objeto». | Una clase sencilla puede instanciarse sin definir su propio inicializador. |
| «No puedo acceder al método desde la clase». | Puede consultarse; al llamarlo a través de una instancia, Python proporciona esta como `self`. |
| «Print del método falla porque dentro ya hay un print». | Sin `()` muestras el método; con `()` lo llamas; si no devuelve un valor útil, un `print` exterior muestra `None`. |
| «Las anotaciones obligan al tipo». | Describen lo esperado; no validan ni convierten por sí solas. |
| «Asignar una dirección la copia». | Se conserva una referencia al objeto recibido. |
| «Crear un objeto lo guarda». | Los ejemplos conservan estado en memoria; guardar en archivos requerirá otras instrucciones. |

### 19.3. Chuleta de sintaxis

```text
class NombreClase:
    def __init__(self, dato):
        self.dato = dato

    def obtener_dato(self):
        return self.dato

objeto = NombreClase("valor")
objeto.dato                       # Obtener un atributo.
objeto.dato = "otro valor"        # Modificar el atributo.
resultado = objeto.obtener_dato() # Llamar y recoger el retorno.
```

Si sabes explicar de dónde sale cada nombre de esa plantilla y qué objeto se consulta en cada punto, tienes la base necesaria para seguir con composición, encapsulamiento y herencia.

## 20. Fuentes y mapa del material integrado

| Fuente | Contenido utilizado | Dónde se desarrolla |
|---|---|---|
| `IFCD0062 Fundamentos programacion Python.pdf`, p. 68 | Inicio y alcance del módulo 5. | Introducción y mapa de continuación. |
| PDF, pp. 69–70 | Clase, objeto, instancia, inicialización y ejemplo `Punto`. | Apartados 1–6 y 13. |
| PDF, pp. 71–72 | Composición y ejemplo `Triangulo` con tres puntos. | Apartados 11–13. |
| PDF, pp. 73–79 | Encapsulamiento, herencia y herencia múltiple. | Solo orientación en el apartado 18. |
| PDF, pp. 80–83 | Ficheros. | Solo ubicación para una ampliación posterior. |
| `Ejemplo14_POO/clases_objetos.py` | `Persona`, atributos, cambio de valores, método con retorno y método que imprime. | Apartados 2–7. |
| `Ejemplo14_POO/ejercicio1.py` | Calculadora con operandos por llamada y gestión de errores. | Apartado 8. |
| `Ejemplo14_POO/ejercicio2.py` | `Cliente`, `Direccion` y composición. | Apartados 10–12. |
| [modulo5.md](modulo5.md) | Tus explicaciones y analogías de clase. | Integradas y precisadas en el documento. |
| [ejercicio5-1.py](ejercicio5-1.py) | Calculadora con estado y parámetros redundantes. | Apartado 9. |
| [ejercicio5-2.py](ejercicio5-2.py) | Dos versiones de `Cliente`, duda sobre la llamada al método y composición. | Apartados 7 y 10–12. |

Se han comprobado además tres precisiones con la documentación oficial de Python: el papel de `__init__` frente a `__new__`, el enlace entre método e instancia y el alcance del prefijo `__`.

- [Tutorial oficial: objetos método](https://docs.python.org/es/3/tutorial/classes.html#method-objects).
- [Referencia oficial: object.__init__](https://docs.python.org/es/3/reference/datamodel.html#object.__init__).
- [Tutorial oficial: variables privadas](https://docs.python.org/es/3/tutorial/classes.html#private-variables).

Los ejemplos de curso, borrador editorial, taller e inscripción y el diagnóstico del coche son ampliaciones didácticas. Las soluciones adaptadas se ofrecen para estudiar; no se ha modificado ningún archivo original de la profesora ni tus ejercicios.
