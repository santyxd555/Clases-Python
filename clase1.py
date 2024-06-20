'''NUMEROS'''
# int -> 1, 2, 0, -15                ENTEROS
# float -> 1.5, 3.0, -4.54           FLOTANTES
# complex -> 11.5j, 33.0j, -6.74j    COMPLEJOS

'''TYPE'''
# dice que tipo de variable es, int, float, complex, etc.

# print(type(2))    # int
# print(type(2.5))  # float
# print(type(2.5j)) # complex

'''OPERACIONES ARITMETICAS'''
# # Suma
# print(3+3)
# # Resta
# print(3-3)
# # Multiplicacion
# print(3*3)
# # Division decimal
# print(5/3)
# # Division Entera
# print(5//3)
# # Potenciacion
# print(5**3)
# # Modulo ( Resto de la dicision entera de 5 y 3 )
# print(5%3)

'''Precedencia'''
# python ejecuta operacion de izquierda a derecha

"""
() -> ** -> / // * % -> + -
primero -> segundo -> tercero -> cuarto
---
1ro. ()
2do. **
3ro. * / // %
4to. + -
---

5 + 5 * 12 / 3 - 45 + 3 ** 5
5 + 5 * 12 / 3 - 45 + 243
5 + 20.0 - 45 + 243
223.0

5 + 5 * 12 / 3 - ( 45 + 3 ** 5 )
5 + 5 * 12 / 3 - ( 45 + 243 )
5 + 5 * 12 / 3 - 288
5 + 20 - 288
-263
"""

# print(type(5 + 5 * 12 / 3 - ( 45 + 3 ** 5 ))) # float
# Resuelve la cuenta y luego se fija que tipo es el resultado

'''Cadenas de texto / Strings (str)'''

# print(type("mama! cortaste la luz!")) # str
# print('mama! cortaste la luz!') # mama! cortaste la luz!
# print("mama! cortaste la luz!") # mama! cortaste la luz!

# print("It's blue") # It's blue
# print('Y Ricardo grito: "mama! cortaste la luz"') # Y Ricardo grito: "mama! cortaste la luz"

'''Escape de caracteres'''

# print('It\'s blue') # It's blue
# print("Y Ricardo grito: \"mama! cortaste la luz\"") # Y Ricardo grito: "mama! cortaste la luz"
# print("Y Ricardo grito:\n\t\"mama! cortaste la luz\"") # Y Ricardo grito:
#                                                                "mama! cortaste la luz"
# las barras son por si queres usar las mismas comillas sin que interrumpan en el texto
# \n : funciona como un enter
# \t : funciona como un tab

'''Triple comillas'''

# print('''Y Ricardo grito:
#     "mama! cortaste la luz"''')

# print('''
#     | Nombre  | Apellido | Edad |
#     |  Pepe   | Grillos  |  23  |
#     | Ricardo |   Fort   |  34  |
#     ''')

'''Raw-String'''
# la "r" hace que se vea el texto en crudo

# print(r'mama! \tcortaste la luz')
# print("C:\norma\toenillos")
# print(r"C:\norma\tornillo")

'''F-String'''
# la "f" hace que donde se agregan las llaves sea codigo y no texto

# print('pepito se saco un 5 en matematica')
# print(f'pepito se saco un {2 + 3} en matematica')

'''Splitear String'''
# por si el texto es muy largo se puede utilizar esta funcion

# print((
#     'asd'
#     "eee"
#     "eaeaeaeae"
# ))

'''Variables'''

# x = 5 + 5
# print(x)
# y = 'oso'
# print(y)

# #=================================================================##
'''Formatos para nombrar una variable'''
# #=================================================================##
# snake_case -> por cadapalabra que contenga el nombre de la variable, las vas a escribir en minuscula y para separarlas vas a poner un _
# edad_de_pepe = 25
# #=================================================================##
# PascalCase -> por cada palabra que contenga el nombre de la variable su primer letra iria en mayuscula y no tendria separacion
# EdadDePepe = 25
# #=================================================================##
# camelCase -> casi igual a PascalCase con la diferencia que la primer letra siempre va en minuscula ( se suele utilizar en otros lenguajes )
# edadDePepe = 25
# #=================================================================##


'''A tener en cuenta el significado de las variables '''
# suma = 5 + 5
# print(suma) # 10
# animal = 'oso'
# print(animal) # oso

'''Asignacion multiple'''
# numero_de_clase, cantidad_alumnos = 34655, 121
# print(numero_de_clase)  # 34655
# print(cantidad_alumnos) # 121

'''Python es case sensitive ( discrimina mayusculas de minusculas )'''
# var = 'variable'
# vaR = 'Variable'
# VaR = 'VariablE'
# print(var) # variable
# print(vaR) # Variable
# print(VaR) # VariablE
# var = 'var'
# print(var) # var
# var = 2
# print(var) # 2

'''Input'''
# el input le pide una variable al usuario

# #v1
# input('Ingrese nombre: ')
# #v2
# print(input('Ingrese nombre: '))
# #v3
# nombre = input('Ingrese nombre: ')
# print(nombre)

'''Castear'''
# nombre = 'Ricardo'
# apellido = 'Fort'
# numero1 = 5
# numero2 = 15

'''umar, Restar, Multiplicar, etc.'''
# print(numero1 + numero2 * numero1)
# print( 5    +   15    *    5   )

'''Concatenar'''
# print(nombre + apellido)       # RicardoFort
# print(nombre + " " + apellido) # Ricardo Fort
# print(f'{nombre} {apellido}')  # Ricardo Fort
# print(nombre, apellido)        # Ricardo Fort
# variable = nombre, apellido    # ('Ricardo', 'Fort') = Ricardo, Fort
# print(variable)                # ('Ricardo', 'Fort')

'''Repetir String'''
# print(nombre * numero1) # RicardoRicardoRicardoRicardoRicardo
# print('pepe ' * 4)      # pepe pepe pepe pepe

'''Index'''
# texto = 'Probando los indices'
#        0123456789...
#                  ...7654321 negativos ( todos llevan un - (menos) )

# palabra = 'roca'
#            0123 -->
#            4321 <--

# print(texto[0]) # P
# print('Probando los indices'[3]) # b
# print(texto[8]) # | | ( es un espacio )               
# print(texto[-1]) # s
# print(texto[19]) # s ( la ultima letra )
# print(texto) --> error ya que no existe ese numero de letra

'''Inmutabilidad'''
texto = 'palabras de mas'
print(texto) # palabras de mas
print(texto[3]) # a

'''
texto[2] = 's'  
texto[-2] = 'e' 
# en los strings no se puede
'''

# texto_cortado = texto[0:4] + 's' + texto[-1] 
# print(texto_cortado) # Prss
# texto_distinto = texto[:-3] + 'menos'
# texto = texto[:-3] + 'menos'
# print(texto_distinto) # Probando los indimenos
# print(texto)          # Probando los indimenos

'''Len'''
# la funcion len cuenta cuantos caracteres tiene una variable contando los espacios, len(valor a contar)

# palabra = 'roca'
# print(len('Probando los indices')) # 20
# print(len(palabra)) # 4

'''Slicing'''

# texto = 'Probando el slicing'
#        0123456789......... 
# print(texto) # Probando el slicing
# print(texto[4]) # a

#texto[< inicio >:< final >:< el salto(este es opcional) >]
# print(texto[4:])   # ando el slicing ( empieza desde la cuarta letra hasta el final)
# print(texto[:8])   # Probando (desde el inicio hasta la letra 7 ya que la 8 no cuenta)
# print(texto[4:19]) # ando el slicing ( si la palabra ocupa 20 espacios pones 21, ya que siempre selecciona un numero antesdel que pusiste )
# print(texto[4:10]) # ando e ( empieza por la letra 4 y termina en la letra 9)

# print(texto[< principio incluido >:< final sin incluir >:< salto >])
# print(texto[3:12:2]) # ---b-n-d-e-|| (el ultimo es un espacio)
# print(texto[-5:-2]) # ici
# print(-2:-5) # no toma nada porque quiere ir de un valor para el anterior de la cadena de caracteres
# print(texto[::-1]) # gnicils le odnaborP (Esta al revez porque tiene un -1)
# print(texto) # Probando el slicing

