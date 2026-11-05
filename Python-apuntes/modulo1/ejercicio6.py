'''
Solicitar una cantidad de segundos y mostrar el equivalente a horas, minutos, segundos
'''

segundos = int(input('dime una cantidad de segundos: '))
hora = segundos // 3600
minuto = (segundos % 3600) // 60
segundo = (segundos % 3600) % 60
print(f'{segundos} segundos son {hora} horas, {minuto} minutos y {segundo} segundos')

#corrección de la profesora:
#resto = segundos % 3600
#minutos = resto // 60
#resto = resto % 60 que pisa el valor anterior, y se quedan los segundos