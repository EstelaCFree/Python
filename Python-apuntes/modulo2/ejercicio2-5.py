'''
    Nos preparamos para Black Friday y estos son los descuentos:
        - si el precio es mayor de 50€ se aplica el 10%
        - si el precio es mayor de 100€ se aplica un 20%
    solicitar el precio por teclado y mostrar el precio final
'''
#print(f"{if 2%2 == 0: "Es par"}")

precio = float(input("Introduce el precio: "))
descuento = 0

if precio > 50 and precio < 100:
    descuento = precio *  0.10
elif precio >= 100:
    descuento = precio *  0.20
    
print( f"Precio inicial: {precio}, dto aplicado: {descuento:.2f}, precio final: {precio-descuento:.2f}")


