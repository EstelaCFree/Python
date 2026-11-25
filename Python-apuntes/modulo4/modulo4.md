##EXCEPCIONES O CONTROL DE ERRORES

Como al darse un error el script para, es importante prevenirlos y hacer lo que se llama manejo de errores.

Try-except-else-finally

Lo mínimo es try-except, los otros son opcionales

- Try: colocamos las instrucciones que pueden ocurrir un error. El script o código.
- Except: vas indicando qué hacer cuando sale x error. Pones un except para cada error. 
except ValueError as error:
    print('El valor introducido no es numérico', error)
El segundo parámetro del print no es obligatorio, es si quieres que se vea.
Al final siempre se pone el bloque except más genérico para los errores que no tengas identificados y es simplemente
except:
    print('Ha ocurrido un error')
O lo que sea.
- else: es lo que se ejecuta cuando no hay ningún error.
- Finally: siempre se ejecuta haya o no errores. A veces es necesario, por ejemplo si abro un fichero hay que cerrarlo, si abro una conexión a una base de datos hay que desconectar, etc.

Ejemplo:
ejercicio4-1

- Múltiples capturas
En un sólo except meter varios errores. Puedes poner un mensaje genérico, usar Exception como uno de ellos que son excepciones genéricas, y puedes usar opcionalmente type(error) para que imprima el tipo de error que es o el mensaje que da.

except (IndexError, ValueError, Exception) as error:
    print('Tipo de error', type(error))
    print('Mensaje de error:', error)

ejemplo ejercicio4-2

- Lanzar excepciones
Crear tus propios mensajes de error
ejercicio4-3 y el ejercicio2 de la profesora en el ejemplo11
en ese ejercicio daba un error porque saldo se había declarado antes y no era una variable global, y ha tenido que poner global saldo dentro de la función

##MÓDULOS EN PYTHON
Un conjunto de funciones o "herramientas" que usas muy habitualmente, las metes en una caja y las llevas siempre que vayas a trabajar. En Python eso son los módulos, que son exportables, y así puedes usarlas no sólo en ese archivo en el que declaras la función sino en todos.
Formas de importar un módulo:
- Importar el módulo completo:
import operaciones (en el ejercicio4-4)
print(operaciones.sumar(5, 3))
- Importar el recurso del módulo que necesito
from operaciones import restar
print(restar(8, 3))
Con esta forma no hace falta poner operaciones. antes de la función
- Importar un recurso pero con un alias, por ejemplo si tuvieras dos funciones que se llaman igual y evitar conflictos o tienen un nombre poco friendly o recordable
from operaciones import dividir as div
print(div(9, 3))

La primera forma tiene la desventaja de requerir el prefijo del módulo, aunque a la vez eso es útil para saber de dónde sale esa función si de repente aparece 200 líneas más abajo. Pero a la vez tienes que descargar todas, que no siempre hace falta.





