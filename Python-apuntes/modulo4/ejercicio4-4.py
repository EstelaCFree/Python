def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar (n1, n2):
    return n1 * n2

def dividir (n1, n2 ):
    return n1 / n2
 
#Eso estaría en un archivo y en otro.py llamado calculadora.py queremos usar esas funciones

#calculadora.py:

#importar el módulo completo
import operaciones
print(operaciones.sumar(6, 2))

#importar sólo el recurso que necesito

from operaciones import restar
print(restar(8, 3))

#Importar un recurso pero con un alias
from operaciones import dividir as div
#print(dividir(9, 3)) no funcionaría
print(div(9, 3))