# if True:
#     ...
# print('Hola mundo')

#==============================================================================

# def dividir(a,b):
#     if b == 0:
#         return 'No se puede dividir por cero'
#     elif type(b) in [int,float]:
#         return 'No se puede dividir pot algo que no es numerico'
#     return a,b

# print(dividir(2,'f'))

#==============================================================================

def dividir(a,b):
    try: # se ejecuta, si es incorrecto ejecuta el except sin producir un error en el codigo
        return a/b
    except: # solo se ejecuta si el try produce un error
        return 'No se puede dividir porque el divisor no es correcto'
    
print(dividir(5,1))

#==============================================================================

# def dividir(a,b):
#     try:
#         return a/b
#     except:
#         print('No se puede dividir porque el divisor no es correcto')
#     return 'Chinvenguencha'

# try:
#     print(dividir(5,1))
    
# except:
#     print('Mensaje del except de afuera')

#==============================================================================

# def dividir(a,b):
#     # try:
#     return a/b
#     # except:
#         # print('No se puede dividir porque el divisor no es correcto')
#     # return 'Chinvenguencha'

# try:
#     print(dividir(5,'a'))

# except:
#     print('Mensaje del except de afuera')

#==============================================================================

# bandera = True
# while bandera:
#     print('''
# Seleccione una opcion:
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir.
# ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else: 
#             raise Exception() # exception es para hacer aparecer un error, el raise hace que se active el exception
#     except:
#         print('\nIngresaste algo incorrecto. \nVolve a seleccionar una opcion.')
        
#==============================================================================

# bandera = True
# while bandera:
#     print('''
# Seleccione una opcion:
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir.
# ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else: 
#             raise Exception() # exception es para hacer aparecer un error, el raise hace que se active el exception
#     except:
#         print('\nIngresaste algo incorrecto. \nVolve a seleccionar una opcion.')
#     else: # cuando no pase por el except para por su else
#         print('Pase por el else')

#==============================================================================

# bandera = True
# while bandera:
#     print('''
# Seleccione una opcion:
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir.
# ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else: 
#             raise Exception() # exception es para hacer aparecer un error, el raise hace que se active el exception
        
#     except: # cuando haya un error en el try entra al except
#         print('\nIngresaste algo incorrecto. \nVolve a seleccionar una opcion.')
#     else: # cuando no pase por el except para por su else
#         print('Pase por el else')
#     finally: # aunque haya o no un error en el try pasa por el finally
#         print('Pase por el finally')

#==============================================================================

# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError: # selecciona los erros que no se puedan dividir entre 0
#         return 'No podes dividir por cero'
#     except TypeError:
#         return 'El tipo no es correcto'
#     except Exception: # selecciona todos lo errores, el exception tiene que ir al final ya que es mas gefnerico y puede tapar a los otros errores
#         return 'Pase por el except'

# print(dividir(5,'a'))
# print(dividir(5,0))

#==============================================================================

# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error: # guarda el error en la variable llamada error
#         return f'No podes dividir por cero, {error}'
#     except TypeError as letra:
#         return f'El tipo no es correcto, {letra}'
#     except Exception as total: # selecciona todos lo errores, el exception tiene que ir al final ya que es mas gefnerico y puede tapar a los otros errores
#         return f'Pase por el except, {total}'

# print(dividir(5,'a'))
# print(dividir(5,0))

#==============================================================================

# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error: # guarda el error en la variable llamada error
#         return f'No podes dividir por cero, {type(error)}'
#     except TypeError as letra:
#         return f'El tipo no es correcto, {type(letra)}'
#     except Exception as total: # selecciona todos lo errores, el exception tiene que ir al final ya que es mas gefnerico y puede tapar a los otros errores
#         return f'Pase por el except, {type(total)}'

# print(dividir(5,'a'))
# print(dividir(5,0))

#==============================================================================

# def dividir(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as error: # guarda el error en la variable llamada error
#         return f'No podes dividir por cero, {type(error).__name__}'
#     except TypeError as letra:
#         return f'El tipo no es correcto, {type(letra).__name__}'
#     except Exception as total: # selecciona todos lo errores, el exception tiene que ir al final ya que es mas gefnerico y puede tapar a los otros errores
#         return f'Pase por el except, {type(total).__name__}'

# print(dividir(5,'a'))
# print(dividir(5,0))

#==============================================================================

""" PreEntrega_1"""
'''
Subimos un colab
Nombre del archivo: Mi nombre y apellido o apellido y nombre+Entrega1 o PrimeraEntrega
'''
'''
Que tenga funciones
Que se pida regitrar un usuario con nombre y contraseña
Una funion para almacenar(guardar la informacion) y otra para mostrar la informacion
Qsar un diccionario para guardae el usuario-contraseña(clave-valor)
Que haya un for para mostrar todos lo usuarios y cointraseñas 
o que pongas tu nombre y te indique la contraseña
quie haya otra funcion que pida ingresar el usuario y contraseña, y que coincidan con los datos guardados
'''
# Ejemplo para utilizar: 
# bandera = True
# while bandera:
#     print('''
# Seleccione una opcion:
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir.
# ''')
#     try:
#         opcion = input('Ingrese la opcion:')
#         if opcion == '1':
#             print('Retirar efectivo')
#         elif opcion == '2':
#             print('Cambiar contraseña')
#         elif opcion == '3':
#             bandera = False
#         else: 
#             raise Exception() # exception es para hacer aparecer un error, el raise hace que se active el exception
        
#     except: # cuando haya un error en el try entra al except
#         print('\nIngresaste algo incorrecto. \nVolve a seleccionar una opcion.')
#     else: # cuando no pase por el except para por su else
#         print('Pase por el else')
#     finally: # aunque haya o no un error en el try pasa por el finally
#         print('Pase por el finally')

































