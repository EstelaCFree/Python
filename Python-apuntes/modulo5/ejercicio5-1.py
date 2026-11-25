'''
clase calculadora con 4 métodos (sumar, restar, mult y dividir)
Solicitar dos números al usuario
llamar a los 4 métodos y mostrar el resultado
hacer control de errores
'''

class Calculadora: #Los nombres de clase empiezan por mayus por convención
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def sumar(self, num1, num2) -> float:
        return self.num1 + self.num2
    #Las anotaciones -> es informativa

    def restar(self, num1, num2) -> float:
        return self.num1 - self.num2

    def multiplicar(self, num1, num2) -> float:
        return self.num1 * self.num2

    def dividir(self, num1, num2) -> float:
        return self.num1 / self.num2

try:
    numero1 = float(input('Introduce un número: '))
    numero2 = float(input('Introduce otro número: '))

    calc = Calculadora(numero1, numero2)

    print(f'La suma es {calc.sumar(numero1, numero2)}')
    print(f'La resta es {calc.restar(numero1, numero2)}')
    print(f'La multiplicación es {calc.multiplicar(numero1, numero2)}')
    print(f'La división es {calc.dividir(numero1, numero2)}')
except ValueError as error:
    print('Debe de ser un número.')
except ZeroDivisionError as error:
    print('No se puede dividir por cero.')
except Exception as error:
    print('Ha dado un error', error)