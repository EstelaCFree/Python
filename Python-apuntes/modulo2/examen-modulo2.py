'''
Un comercio minorista necesita un programa que determine si un cliente tiene derecho a un descuento basado en el importe de su compra.
Requerimientos de Ejecución:
1. Solicitar por teclado el importe de la compra.
2. Si el importe es superior a 100€, aplicar un descuento del 10%.
3. Si es menor o igual, no aplicar descuento.
4. Mostrar por pantalla el importe final a pagar.
Evidencias Obligatorias a Entregar: Código fuente en .py y captura del terminal con un caso de prueba de 150€.
'''

compra = float(input('Introduzca el importe de la compra: '))

if compra > 100:
    precio = compra * 0.90
    print(f'El precio final con el 10% de descuento es {precio:.2f} €')
else:
    print('No cumple el mínimo para aplicar descuento.')