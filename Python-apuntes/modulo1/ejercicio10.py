'''
una persona tiene en su cuenta 1250€
recibe una transferencia de 375
paga 3 facturas de 85 cada una
recibe un bizum de 200
retira el 10% del saldo
mostrar saldo final
'''

saldo = 1250
saldo += 375
saldo -= (3 * 85)
saldo += 200
saldo -= saldo * 0.10
print(f'El saldo final es {saldo}€') 

#corrección profesora:

saldo = 1250
saldo += 375
saldo -= 85 * 3 
#porque cuando hay un operador de asignación (=) primero se calcula todo lo de la derecha y luego se asigna
saldo += 200
retiro = saldo * 10/100
saldo -= retiro
print(f'El saldo final es {int(saldo)}€') 
#lo convierte a entero para quitarle los decimales
