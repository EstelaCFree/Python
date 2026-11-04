'''
Solicitar el precio como número real de un producto
aplicar el 10% de descuento
aplicar el 21% de IVA
Mostrar el desglose: precio inicial, importe dto, importe IVA, importe total
'''

precio = float(input('Dame el precio del producto: '))
descuento = precio * 0.10
precio_dto= precio - descuento
iva = precio_dto * 0.21
precio_total = precio_dto + iva

print(f'El producto cuesta {precio} €, pero con el descuento se queda en {precio_dto} €')
print(f'El IVA es de {iva} €, por lo que el precio final es de {precio_total} €')