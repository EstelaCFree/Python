
usuario = input('introduce tu usuario: ')
contraseña = input('introduce la contraseña: ')
print('abre la puerta?', usuario == 'admin' and contraseña == 'python123')

'''añadido de otra compi:
usuario=input("Ingrese su usuario: ")
usuario=="admin"
pasword=input("ingrese su pasgord: ")
pasword=="python123"
if usuario=="admin" and pasword=="python123":
print("Bienvenido al sistema" )
else:
print("Usuario o pasword incorrecto")'''

#para que no se vea el password:
#import getpass
#password = getpass.getpass("Ingrese su password: ")    
