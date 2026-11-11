'''
    Calcular la nomina de 2027
        - sueldo actual bruto hay pedirlo al usuario
        - nº de hijos 
        - solicitar el ipc en %
        
    sobre el sueldo actual incrementarlo segun el ipc
    calcular el irpf a pagar:
        - si es inferior a 22.000 el irpf sera 5%
        - si es inferior a 35.000 el irpf sera del 12%
        - si es inferior a 55.000 el irpf sera del 25%
        - si es superior a 55.000 el irpf sera del 35%
        
    descontar por cada hijo se descuenta un 2% del IRPF
    
    El sueldo se distrubuye en 14 pagas y queremos mostrar el sueldo neto al mes
'''
sueldo_bruto_2026 = float(input("Introduce tu sueldo bruto anual del 2026: "))
ipc = float(input("Introduce la tasa de IPC: "))
num_hijos = int(input("Dinos cuantos hijos tienes? "))

sueldo_bruto_2027 = sueldo_bruto_2026 + (sueldo_bruto_2026 * ipc / 100)

if sueldo_bruto_2027 < 22000:
    irpf = 5/100 - (2/100 * num_hijos)
elif sueldo_bruto_2027 < 35000:
    irpf = 12/100 - (2/100 * num_hijos)
elif sueldo_bruto_2027 < 55000:
    irpf = 25/100 - (2/100 * num_hijos)
else:
    irpf = 35/100 - (2/100 * num_hijos)
    
sueldo_neto_2027 = sueldo_bruto_2027 - (sueldo_bruto_2027 * irpf)
sueldo_mensual = sueldo_neto_2027 / 14

print(f"Tu sueldo bruto actual {sueldo_bruto_2026} con un ipc {ipc} y un irpf {irpf}")
print(f"El sueldo bruto anual para 2027 es {sueldo_bruto_2027:.2f}")
print(f"El sueldo neto anual para 2027 es {sueldo_neto_2027:.2f}")
print(f"Tu nomina del mes {sueldo_mensual:.2f}")