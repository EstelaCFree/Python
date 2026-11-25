
class Cliente:
    def __init__(self, nombre, cif, vip : bool):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip

    def mostrarInfo(self):
        print(f'Cliente {self.nombre}, con CIF {self.cif}: VIP {self.vip}')

cli1 = Cliente('Adolfo Ruiz', '1321527L', False)
cli2 = Cliente('Andy Pain', '78935614T', True)

'''
print(cli1.mostrarInfo)
print(cli2.mostrarInfo)
puse esto pero da fallo porque ese método ya es un print
'''

cli1.mostrarInfo()
cli2.mostrarInfo()

'''
ahora va el ejemplo de composición: una clase que una propiedad es un objeto de otra clase
'''

class Direccion:
    def __init__(self, calle, numero, poblacion):
        self.calle = calle
        self.numero = numero
        self.poblacion = poblacion

class Cliente:
    def __init__(self, nombre, cif, vip : bool, direccion):
        self.nombre = nombre
        self.cif = cif
        self.vip = vip
        self.direccion = direccion

    def mostrarInfo(self):
        print(f'Cliente {self.nombre}, con CIF {self.cif}: VIP {self.vip},' + 
              f' Dirección: {self.direccion.calle}, número {self.direccion.numero}, {self.direccion.poblacion}')

dir = Direccion('Mayor', 7, 'Rivas')
cli1 = Cliente('Adolfo Ruiz', '1321527L', False, dir)
cli2 = Cliente('Andy Pain', '78935614T', True, Direccion('Leganitos', 15, 'Madrid'))

cli1.mostrarInfo()
cli2.mostrarInfo()

print(cli1.direccion.poblacion) #son como punteros continuados, como entrar en subcarpetas