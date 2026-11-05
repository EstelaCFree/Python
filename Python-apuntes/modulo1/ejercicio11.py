'''
una fábrica priduce 350 productos al días
aumenta la producción en 75 unidades
duplica la producción
divide la producción entre 5
calcula cuántas unidades soban al agrupar la producción en lotes de 12 unidades
'''

produ = 350
produ += 125
produ -= 75
produ *= 2
produ /= 5
sobran = produ % 12
print(f'El número de unidades que sobran es {int(sobran)} unidades')
