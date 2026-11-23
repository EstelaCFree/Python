def solicitar_edad():
    edad = int(input('introduce tu edad: '))
    if edad < 0:
        raise Exception('la edad no puede ser negativa')
    else:
        return edad

try:
    edad = solicitar_edad()
except Exception as ex:
    print(ex)
else:
    print('Edad del usuario: ', edad)