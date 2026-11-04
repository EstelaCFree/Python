'''solicitar el importe en euros
solicitar a cómo está el cambio a dólares
mostrar la conversión a dólares con 2 decimales
'''

importe = float(input('Dime el importe e euros: '))
cambio = float(input('Dime a cuánto está el cambio a dólares:'))
dolars = importe * cambio
print(f'{importe} euros son {dolars:.2f} dólares')
