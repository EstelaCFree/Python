'''Conversión de grados farenheit a centígrados
Pedimos la temperatura en grados centígrados (float)
aplicamos la fórmula para convertir a farenheit
F = C * 9/5 + 32
Mostramos el resultado con 2 decimales
'''

cent = float(input('Dame la temperatura en grados centígrados: '))
farenheit = cent * 9/5 + 32
print(f'La temperatura en grados farenheit es de {farenheit:.2f} °F')
