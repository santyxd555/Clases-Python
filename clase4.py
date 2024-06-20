
"""¿Qué es un iterable?:
Un iterable es un objeto que se puede recorrer uno a uno.
Puede pasarse como parámetro a la función iter(), 
que devuelve un iterador basado en el objeto iterable.
Los tipos principales como listas, tuplas, diccionarios, 
conjuntos y cadenas son iterables en Python."""



"""Strings"""

"""
Método upper"""

# cadena1 = "soY lA pRimEr cadEnA"
# print(cadena1)

# cadena1_todo_mayusculas = cadena1.upper() #.upper() cambia todos los caracteres a mayusculas
# print(cadena1_todo_mayusculas)

"""
lower"""

# cadena1_en_minisculas = cadena1_todo_mayusculas.lower() #.lower() cambia a todos los caracteres a minusculas
# print(cadena1_en_minisculas)

"""
title"""

# cadena1_en_modo_titulo = cadena1_en_minisculas.title() #.title() pone en mayuscula la primera letra en cada palabra
# print(cadena1_en_modo_titulo)

"""
capitalize"""

# cadena1_parrafo = cadena1.capitalize() #.capitalize() pone la primer letra de la primer palabra en mayuscula
# print(cadena1_parrafo)

#=============================================================================================================
#=============================================================================================================

"""
Count"""
# Busca cuantas veces se repite el caracter buscado

# cadena1 = "soY lA pRimEr cadEnA"
# print(cadena1.count("a")) # 1
# print(cadena1.count(" ")) # 3 
# print(cadena1.count(""))  # 21
# print(cadena1.count("z")) # 0

"""
Find"""
# Busca el caracter de derecha a izquierda

# print(cadena1.find("a")) # 15 
# print(cadena1.find(" ")) # 3
# print(cadena1.find(""))  # 0
# print(cadena1.find("z")) # -1 / el find no rompe cuando no encuantra el caracter

"""
Rfind"""
# Busca el caracter de derecha de derecha a izquierda

# print(cadena1.rfind("a")) # 15
# print(cadena1.rfind(" ")) # 13
# print(cadena1.rfind(""))  #
# print(cadena1.rfind("z")) #

"""
Split"""
# el split divide la frase en variables distintas en una lista

# cadena2 = "segunda cadena al rescate"
#lista = 
# lista = cadena2.split() # si no se escribe nada dentro lo divide por los espacios
# print(lista)
# lista2 = cadena2.split("a") # en cada lugar donde haya una "a" se divide
# print(lista2)
# lista3 = cadena2.split("asd el pepe loco") # cra una lista con una variable que se ocupa con todas las palabras
# print(lista3)

"""
Join"""
# para unir todas las palabras de una lista/tuplas con lo que ingreses antes del join

# lista = ['segunda', 'cadena', 'al', 'rescate']
# cadena = " ".join(lista) # una toda la lista con espacios
# print(cadena)
# union = "-"
# cadena1 = union.join(lista) # una toda la lista con guiones "-"
# print(cadena1)

"""
Strip"""
# Borra del texto lo que esta dentro del parentesis

# cadena = "-------Hola Mundo--------"
# cadena2 = cadena.strip("-") 
# print(cadena2)

# cadena = "ssaddaHola Mundoddsaa"
# cadena2 = cadena.strip("ads") # borra todas las "ads" hasta que encuentra una variable distinta de delante para atras y de atras para adelante
# print(cadena2)

# cadena = " Hola Mundo " # ya que hay un espacio al inicio y al final no borra nada
# cadena2 = cadena.strip("Hola") # si se agrega el espacio ahí si borraria
# print(cadena2)

"""
Replace"""
# caracter.replace("variable", "remplazo")

# cadena = "Hola Mundo"
# cadena2 = cadena.replace("o", "O")
# print(cadena2)

# palabra_repetida = 'cadena pepito cadena cadena cadena'
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra') # remplaza todo
# # palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra', 3) # remplaza los primeros 3
# print(palabra_repetida)
# print(palabra_repetida_modificada)

""" # Listas """

"""
Método Clear"""
# el clear limpia la lista

# lista = [1,2,3]
# lista.clear() 
# print(lista)

"""
Método Extend""" 
# Como extender la lista

# lista2 = lista + [1,2,3] # se creo la lista dos con las variables de la lista uno y otra lista
# print(lista2)
# lista += [1,2,3] # se le agregan variables a la lista
# print(lista)
# lista.extend([1,2,3]) # extiende la lista con lo que esta dentro del parentesis
# print(lista)

"""
Insert"""
# insertar variables en una lista seleccionando su ubicacion

# lista2 = ["segunda", "lista", 2]
# dicc = {
#     "llave": "valor"
# }
# print(lista2)
# lista2.insert(1, dicc) # lo inserta delntro de la lista
# print(lista2)

"""
Método reverse"""
# da vuelta la lista

# lista2 = ['segunda', 'lista', 2]
# print(lista2)
# # lista2 = lista2[::-1] # hace lo mismo pero con el reverse te comlpicas menos
# lista2.reverse() 
# print(lista2)

"""
Método sort"""
# pone los nuemeros en orden

# lista_numeros = [5,1,2,3,4,10]
# lista_numeros.sort()
# # lista_numeros.sort(reverse=True) # con el reverse los nuemros van de atras hacie adelante en orden
# print(lista_numeros)

# [].sort()
# lista_numeros1 = ['5','1','2','3','4','10'] # estan puestos como letras (con comillas)
# lista_numeros1.sort()
# # lista_numeros1.sort(reverse=True)
# print(lista_numeros1)


"""Ejercicio - colecciones 1

Utilizando todo lo que sabes sobre cadenas, listas y
sus métodos internos, transforma este texto:

texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

En este:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies -le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.
"""

# texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'
# lista = texto.split("&") # se hace una lista dividiendo el texto en donde haya un "&"
# # print(lista)
# lista[0] += "..."
# # print(lista[0])



# texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

# texto_spliteado = texto.split('&')
# print(texto_spliteado)
# texto_spliteado[0] += '..'
# for i, x in enumerate(texto_spliteado):
#     texto_spliteado[i] = x[0].upper() + x[1:]
#     print(texto_spliteado[i])


# texto_final = '.\n- '.join(texto_spliteado) + '.'

# print(texto_final)










#========================================================================================================================
#========================================================================================================================
#========================================================================================================================


# Principios Clase 5

# Conjuntos
# Para sets o diccioanrios se utiliza la funcion copy

conjunto1 = {1, 'conjunto1', (1, True)}
# conjunto3 = conjunto1
conjunto3 = conjunto1.copy()
print(conjunto3)
conjunto1.add(456)
print(conjunto3) # se actualiza el valor ya que no guarda la variable en si sino que va a la ubicacion para verificar el dato



# Listas o Tuplas
# Para las listas o tuplas se utiliza [:]

lista1 = [1,2,3,4,5]
# lista2 = lista1
lista2 = lista1[:]
print(lista2)
lista1.append(45)
print(lista2)





