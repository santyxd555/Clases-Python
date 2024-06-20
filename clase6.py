
'''IF'''

# esta_lloviendo = input('Esta lloveindo?? (si/no) ').lower() # el lower lo transforma a minuscula

# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga')
# print('Mi programa termino!')

'''IF - ELSE'''

# esta_lloviendo = input('Esta lloveindo?? (si/no) ').lower() # el lower lo transforma a minuscula

# if esta_lloviendo == 'si':
#     print('Pase por la sentencia IF')
#     print('Entonces voy a usar paraguas cuando salga')
# else:
#     print('Pase por la sentencia IF')
#     print('Entonces no voy a llevar paraguas')
# print('Mi programa termino!')

''' IF - ELIF - ELSE '''

# esta_lloviendo = input('Esta lloveindo?? (si/no) ').lower() # el lower lo transforma a minuscula

# if esta_lloviendo == 'si':
#     print('Entonces voy a usar paraguas')
# elif esta_lloviendo == 'no':
#     print('Entonces no voy a usar paraguas cuanbdo salga')
# else:   
#     print('No entiendo que me queres decir con eso')
# print('Mi programa termino!')


# primer_numero = int(input('Ingrese un numero: '))

# if primer_numero < 20:
#     print('es menor a 20')
# elif primer_numero < 30:
#     print('es menor a 30')
# elif primer_numero < 40:
#     print('es menor a 40')
# elif primer_numero <= 50:
#     print('es menor o igual a 50')
# else:
#     print('El numero es mayor a 50')

#=====================================================

'''Ejempo 1'''

# var = 15
# primer_numero = int(input('Ingrese un numero: '))
# segundo_numero = int(input('Ingrese otro numero: '))

# if primer_numero == segundo_numero:
#     print('Son iguales')
#     if primer_numero < var:
#         print('Son menores a var')
#     else:
#         print('Son mayores a var')
# else:
#     print('No son iguales')
#     if primer_numero < var:
#         print('EL primer_numero es menor a var')
#         if segundo_numero < var:
#             print('segundo_numero es menor a var')
#         else:
#             print('El segundo_numero es mayor a var')
#     else:
#         print('El primer_numero es mayor a var')
# print('Se termino el codigo!!')

#=====================================================

'''Ejemplo 2'''

# esta_lloviendo = input('Esta lloveindo?? (si/no) ')

# #v1
# pepito = ''
# if esta_lloviendo == 'si':
#     pepito = 'Soy pepito'
# else:
#     pepito = 'No soy pepito'

# #v2
# pepito = 'Soy pepito' if esta_lloviendo == 'si' else 'No soy pepito :('

# print(pepito)

#=====================================================

'''Ejemplo 3: Marvel vs. Capcom'''

# preferencia = input('Ingrese su preferencia: (Marvel/Capcom) ').capitalize()
# nombre = input("Ingrese su nombre: ").upper()

# if preferencia == 'Marvel' and nombre < 'M' or preferencia == 'Capcom' and nombre > 'N':
#     print('Tu Grupo es el A')
# else:
#     print("Tu Grupo es el B")
























