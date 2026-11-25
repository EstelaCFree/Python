## POO

Todo en programación orientada a objetos son objetos, pero el programador lo que crea son clases primero. Las clases son como plantillas, o lo que estaba fuera de la caverna de platón.
Una cadena de texto o una colección son objetos, que cuando les pregunto el tipo me dice que es clase tupla por ejemplo. Un error es un objeto que sale de una clase, por ejemplo clase ValueError, pero el error concreto es un objeto.
En el pdf de apuntes vienen las definiciones. 

En Python sólo se permite un constructor por clase. Un constructor es lo que hacemos para crear objetos. Tiene un nombre concreto: __init__

class Persona:
    def __init__(self):
        pass

Y luego para crear el objeto sería
persona = Persona()

Y cada vez que genero un objeto, es una copia de la clase.
Pero claro, esto es demasiedo genérico, cómo es el objeto persona? Hay que hacer abstracción, que se declaren los parámetros, atributos, propiedades o campos, que se llaman variables de instancia. Vamos a ampliar un poco el constructor.

def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

persona1 = Persona('María', 35)
El objeto es persona1, y los parámetros son sus características.
Qué significa self? es como un puntero self, que señala del objeto a sí mismo, a una de sus variables. 
Para acceder a esa variable se usa el .

persona1.nombre = 'María José'

Puedo definir métodos propios de la clase. ¿Qué es un método? Funciones declaradas dentro de la clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def nombre_mayus(self):
        return self.nombre.upper()
    
    def mostrar_info(self) -> None:
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

Si yo no me genero una instancia de la clase persona, no puedo acceder a ese método porque el método pertenece a la clase, y esa instancia (el objeto) lleva una copia de la clase.

print(persona1.nombre_mayus())
persona.mostrar_info()

##Composición

