#if <condicion>
#   <bloque de codigo>
#elif <condicion>
#   <bloque de codigo>

# List = []        # Lista
# Tuple = ()       # Tupla
# Dict = {}        #
# Set = set({})      #

'''WHILE'''

'''Ejemplo 1'''
# numero = 1
# numero2 = int(input("Ingrese un numero: "))


# while numero <= numero2:
#     print('Mensaje numero: ', numero)
#     numero += 1


'''Ejemplo 2'''
# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     if contador == 15:
#         dato_de_condicion = False
#     contador += 1
#     print('Estoy mostrando este mensaje numero: ', contador)

# print('Ultima linea del proyecto')

'''Ejemplo 3'''
# contador = 0
# dato_de_condicion = True
# while dato_de_condicion:
#     contador += 1
#     if contador == 15:
#         dato_de_condicion = False
#     print('Estoy mostrando este mensaje numero: ', contador)

# print('Ultima linea del proyecto')

'''WHILE - ELSE'''

'''Ejemplo 4'''
# contador = 0
# dato_de_condicion = 2 # ( 0 = False | 0 != True )
# while dato_de_condicion:
#     contador += 1
#     print('Estor mostrando este mensaje numero: ', contador)
#     dato_de_condicion -= 1
    
# else: # se ejecuta cuando se termine la funcion del while
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')

'''
PASS - ... (puntos suspensivos)
# simula como si fuese codigo
# se puede utilizar para rellenar un if hasta que lo termines para que no rompa
'''

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 2:
#         pass # sirve para rellenar un un iterador para que funcione igual el codigo
#     print('Estor mostrando este mensaje numero: ', contador)
    
# else: # se ejecuta cuando se termine la funcion del while
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


'''
CONTINUE
# sirve para saltar a la siguiente interacion, ejemplo: while, for, etc
'''

# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 2:
#         continue # empieza el while devuelta saltenado lo que hay abajo
#     print('Estor mostrando este mensaje numero: ', contador)
# else: # se ejecuta cuando se termine la funcion del while
#     print('Pase por el else')

# print('Ultima linea de mi proyecto')


'''
BREAK
# sirve para cortar un bucle, ejemplo: while, if, etc ( solo funciona dentro de un bucle )
'''

# contador = 0
# contador2 = 0

# while contador < 5:
#     contador += 1
#     if contador == 2:
#         break
#     print('Estor mostrando este mensaje numero: ', contador)
# else: # se ejecuta cuando se termine la funcion del while
#     print('Pase por el else')
    
# while contador2 == 0: # Solo funciona una vez
#     print('Terminado')
#     contador2 += 1

# print('Ultima linea de mi proyecto')


'''
COLECCIONES: string (una palabra o texto), list (lista), tuple (tupla), dict (diccionario) y set (conjuntos)
'''


'''FOR'''
# lista = [1,2,3,4,'pepito',True,('eaea','pepe')]

# print('La lista contiene el valor: ', lista[0])
# print('La lista contiene el valor: ', lista[1])
# print('La lista contiene el valor: ', lista[2])
# print('La lista contiene el valor: ', lista[3])
# print('La lista contiene el valor: ', lista[4])
# print('La lista contiene el valor: ', lista[5])
# print('La lista contiene el valor: ', lista[6])


# indice = 0
# cant_de_elementos = len(lista)
# while indice < cant_de_elementos:
#     print('La lista contiene el valor: ', lista[indice])
#     indice += 1

# for elemento in lista: # para el 1 en lista = lista[0] y asi el elemento va pasando al siguiente valor sucesivamente
#     print('La lista contiene el valor: ', elemento)
#     if lista[elemento] == 'pepito':
#         print('La lista contiene el valor: ', lista[elemento])
#         break

#===========================================================================================================

'''DICCIONARIO'''
diccionario = {
    'marca': 'Ford',
    'Modelo': 'K',
    'Ruedas': 5,
}

# # Keys
# for algo in diccionario.keys(): # con el keys imprime las variables
#     print('El diccionario contiene: ', algo)

# Values
for algo in diccionario.values(): # con values imprime lo que contiene las variables
    print('El diccionario contiene: ', algo)

# Items
# for variable1, variable2 in diccionario.items(): # con el items podemos imprimir las variables y lo que contiene un diccionario
#     print(f'{variable1}: {variable2}')


#===========================================================================================================

# lista = [1,2,3,4,'pepito',True,('eaea','pepe'), 'ochentoso']

# for valor in lista:
#     if valor == 'pepito':
#         continue
#     if valor == ('eaea','pepe'):
#         break
#     print('La lista contiene el valor: ', valor)

#===========================================================================================================

# lista = {1,2,3,4,'pepito',True,('eaea','pepe'), 'ochentoso'}
# # ya que estan declarados en set lo imprime de forma "aleatoria"

# for valor in lista:
#     print('La lista contiene el valor: ', valor)














