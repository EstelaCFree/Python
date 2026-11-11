'''
    Calculadora mejorada.
    Solicitar 2 numeros reales
    soliciar que operacion: +,-,*,/
    Mostrar el resultado
'''
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
operacion = input("Introduce la operacion (+,-,*,/): ")

if operacion == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operacion == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operacion == '*':
    print(f"{num1} x {num2} = {num1 * num2}")
elif operacion == '/':
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Operacion no valida")