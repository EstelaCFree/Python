# try-except-else-finally

try:

    # aqui colocamos las instrucciones que pueden provocar un error

    numero1 = int(input("Introduce dividendo: "))

    numero2 = int(input("Introduce divisor: "))

    division = numero1 / numero2

except ValueError as error:

    print("El valor introducido no es numerico", error)

except ZeroDivisionError as error:

    print("No se puede dividir por cero", error) 

except:

    # El bloque except mas generico, va al final

    print("Ha ocurrido un error")  

else:

    # Se ejecuta cuando no hay ningun error

    print("Resultado:", division)

finally:

    # Siempre se ejecuta, haya o no errores

    print("***** FIN *****")




