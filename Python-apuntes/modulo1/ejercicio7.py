'''
Salgo a cenar con mis amigos y hay que repartir la cuenta.
Datos que necesito: cuenta, personas y propina
Mostrar cánto tenemos que pagar cada uno
'''

cuenta = float(input('Dime el total de la cuenta: '))
amigos = int(input('Dime cuántos sois: '))
propina = float(input('Dime la propina que queréis dejar: '))

total = cuenta + propina
cada_uno = total / amigos

print(f'Cada uno tiene que pagar {cada_uno:.2f} euros')