'''
    solicitar el año (2026, 1996, 2005) y mostrar si es bisiesto o no.
    Es bisiesto:
        - si es divisible entre 400
        - o, es divisible entre 4 pero no entre 100
'''
anyo = int(input("Introduce un año: "))

if anyo % 400 == 0:
    print("El año es bisiesto")
elif anyo % 4 == 0 and anyo % 100 != 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")