'''SET (Conjunto)'''

# lista = ['soy', 'una', 'lista', 2, True] # Lista
# tupla = ('soy', 'una', 'tupla', 2, True) # Tupla
# conjunto = {'soy', 'un', 'conjunto', 1, True} # Set

#==================================================================

'''Set vacio'''

# lista = []
# tupla = ()
# diccionario = {}
# conjunto = set()
# print(type(lista))       #  <class 'list'>
# print(type(tupla))       # <class 'tuple'>
# print(type(diccionario)) # <class 'dict'>
# print(type(conjunto))    # <class 'set'>

#==================================================================

'''Asignacion en un set'''

# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjunto = {'soy', 'un', 'conjunto', 1, True}

# lista[1] = 'uno'
# print(lista)
# tupla[1] = 'uno'
# print(tupla) # las tuplas no se pueden modificar
# conjunto[1] = 'uno'
# print(conjunto) # los sets no se pueden modificar

# print(lista[1])
# print(tupla[1])
# print(conjunto[1]) # podriamos decir que no se puede imprimir ya que no tienen un orden
# print(conjunto)

#==================================================================

'''Objetos mutables y los sets'''

# prueba = {1, 2, 3, 'hola', 'como', 'estas'}
# otra_prueba1 = [(1,2,3), [6,7,8]] #lista ()
# otra_prueba2 = ((1,2,3), [6,7,8]) #tupla []
# otra_prueba3 = {(1,2,3), [6,7,8]} #sets  {} # dentro de los sets no se pueden guardan listas
# print(otra_prueba1)
# print(otra_prueba2)
# print(otra_prueba3)

# otra_prueba1[1][2] = 5
# print(otra_prueba1)
# otra_prueba2[1][2] = 5
# print(otra_prueba2)
# otra_prueba2[1] = 5
# print(otra_prueba2)

#==================================================================

'''Set generado con iterables'''

# # lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ['otra', 'lista']]
# lista_prueba = [1, 2, 3, 'hola', 'como', 'estas', ('otra', 'lista')]
# # lista_prueba = [1, 2, 3, 'hola', 'como', 'estas']
# conjunto_prueba = set(lista_prueba)
# lista_prueba_2 = list(conjunto_prueba) #se guarda en el orden que aparecio en el set
# # conjunto_prueba2 = set(range(10))
# print(conjunto_prueba)
# # print(lista2)
# # print(conjunto_prueba2)
# print(type(lista_prueba))
# print(type(conjunto_prueba))
# # print(type(conjunto_prueba2))

#==================================================================

'''No se repiten valores'''

# lista = [1,2,3,4,5,6,6,6,6,1,2,3]
# conjunto = {1,2,3,4,5,6,6,6,6,1,2,3} #en los sets no se repite ninguna variable
# print(lista)
# print(conjunto)
# print(set(lista))

# string = 'pepito corre solo por la calle'
# print(set(string)) # no se repite ninguna variable

#==================================================================
#==================================================================
'''Funciones Integradas'''

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto) # {'v8', (6, 'blindadas'), 'Negro'}

#==================================================================

'''Método add'''
# Agrega la tupla completa (1, 2, 3, 'probando'), con parentesis y todo

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # lista = [1, 2, 3, 'probando'] # no funciona ya que es una lista
# tupla = (1, 2, 3, 'probando')

# auto.add('descapotable')
# # auto.add(lista) ERROR
# auto.add(tupla) # add es para anadir lo que este dentro del parentisis
# print(auto)

#==================================================================

'''Método update'''
# El update agrega lo que hay dentro de la lista, variable, conjunto

# auto = {'v8', 'Negro', (6, 'blindadas')}
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# conjunto = {'soy', 'un', 'set'}
# cadena = 'soy una cadena'
# # rango = range(15)
# auto.update(lista) 
# print(auto) 
# auto.update(tupla)
# print(auto) 
# # auto.add(cadena)
# auto.update(cadena)
# print(auto) 
# auto.update(cadena)
# print(auto)
# # auto.update(rango)
# # print(auto)

#==================================================================
'''Función len'''
# Sirve para ver la cantidad de variables que tiene un set(conjunto)

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(len(auto))

#==================================================================
'''Método discard'''

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.discard('tupla') # aunque no este el elemento lo intenta eliminar y no se rompe el codigo
# print(auto)
# auto.add('tupla') # se anade el elemento tupla
# print(auto)
# auto.discard('tupla') # se elimina el elemento tupla
# print(auto)

#==================================================================
'''Método remove ( discard pero con generacion de error )'''

# auto = {'v8', 'Negro', (6, 'blindadas')}
# auto.add('lista')
# print(auto)
# auto.remove('lista') 
# print(auto)
# # auto.remove('pepito') # con el metodo remove si no esta el elemento se rompe el codigo
# # print(auto)

#==================================================================
'''Operador in'''
# Sirve para ver si el elemento esta dentro del set

# auto = {'v8', 'Negro', (6, 'blindadas')}
# # for dato in auto:
# #     print(dato)
# print('descapotable' in auto) # False
# print('caño de escape' not in auto) # True (sirve para ver si el elemento no esta dentro del set)
# lista = [1,2,3,4]
# print(1 in lista) # True

# print('blindadas' in auto) # False
# print((6, 'blindadas') in auto) # True (se necesita poner toda la lista ya que el elemento esta dentro de una lista dentro del set)

#==================================================================
'''Método clear'''
# sirve para limpiar una set

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# # auto = 'soy un texto'
# # auto = set()
# # print(auto)
# auto.clear() 
# print(auto)

#==================================================================
'''Método pop'''

# auto = {'v8', 'Negro', (6, 'blindadas')}
# print(auto)
# valor = auto.pop() # al pop si no le pones nada dentro del parentisis elimina un valor aleatorio
# print(auto)
# print(valor)

# # while len(auto):
# #     print(auto)
# #     valor = auto.pop()
# #     print(valor)

#==================================================================
'''Ejercicio 1'''
'''
Crear un conjunto en Python que posea los siguientes elementos:
Colores: Rojo, Blanco, Azul.
Posteriormente, agrega nuestro set de colores, los valores de: Violeta y Dorado
Elimina a los colores: Celeste, Blanco y Dorado
Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el método discard?
'''
# colores = {'rojo', 'blanco', 'azul'}

# colores.update({'violeta', 'dorado'}) # se agrega en formato set porque sino lo agreaga como letras
# print(colores)

# colores.discard('violeta') # se utiliza el discard ya que si usamos remove se rompe el codigo ya que no esta
# print(colores)
# colores.remove('blanco')
# colores.remove('dorado')

#==================================================================
'''Ejercicio 2 Sets'''
'''
Programa las siguientes instrucciones de forma ordenada sobre la variable grupo:
Añade los usuarios: Ana, Ramón, Marta, Eric, David
Elimina los usuarios: Mario, Miguel, Esteban
grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
'''

# grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
# grupo.update({'Ana','Ramon', 'Marta', 'Eric', 'David'})
# print(grupo)
# # print(type(grupo))
# grupo.discard('Mario')
# grupo.discard('Miguel')
# grupo.discard('Esteban')
# print(grupo)


#==================================================================
'''BREAK'''
#==================================================================
'''DICCIONARIO'''
# dicc = {}  # el diccionario nos permite unificar y clasificar de una manera mas definida
#            # el diccionario es mutable
#            # lo parecido con los sets son las llaves
#==================================================================
'''
Las claves/llaves/keys pueden ser cualquier valor inmutable
los valores/values pueden ser cualquier valor posible

dicc = { clave: valor, clave2: valor2, clave3: valor3, ...}

dicc1 = {
    clave: valor,
    clave2: valor2,
    clave3: valor3,
    ...
}

dicc2 = {
    clave: dicc1,
    clave2: valor2,
    clave3: valor3,
    ...
}

dicc3 = {
    0: ['soy', 'una', 'lista'],
    'tupla': ('soy', 'una', 'tupla'),
    ('tupla', 'llave'): 'la tupla es mi llave'
}
'''
#==================================================================
# auto = {'v8', 'Negro', (6, 'blindadas')} # == set
# print(auto)
# # motor = 'v8'
# # color = 'Negro'

# auto = { # == diccionario
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(auto)
#==================================================================
'''Acceso, mutabilidad, asignación, agregado de valores'''
# El get nos permite accedes a un elemento del diccionario y si no existe no se rompe el codigo

# lista = ['soy', 'una', 'lista']
# print(lista[1])
# lista[1] = 24
# print(lista[1])

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(auto['motor']) # v8
# print(auto['canio de escape']) # si no existe se rompe el codigo
# print(auto.get('motor')) # busca y imprime el valor de 'motor'
# print(auto.get('canio de escape', 'ese valor no existe')) # ya que no existe el elemento responde con 'ese valor no existe'
# print(auto.get('canio de escape', input('que valor por defecto queres: '))) # ya que no existe pide que se ingrese otro valor'
# auto['motor'] = 'v12' # cambia el valor del motor a v12
# print(auto['motor'])
# # print(auto)
# auto['modelo'] = 2016 # se agreaga automaticamente el valor
# print(auto)
# auto['pasajeros'] += 1 # se le suma 1 al valor de 'pasajeros'
# print(auto)

#==================================================================
#==================================================================
'''Funciones Diccionarios'''
#==================================================================
# Método update

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# pepe = (1, 2)
# auto.update({pepe: 'valor1', 'llave2': 'valor2', 'motor': 'v8'}) # lo que no esta se agrega, ya que pepe es una variable, el nombre es lo que esta dentro de "pepe"
# print(auto)
# auto.update({pepe: 'valor1', 'llave2': 'valor2', 'motor': 'v12'}) # lo que esta se actualiza
# print(auto)
# auto.update((('llave1', 'valor1'), ('llave2', 'valor2'), ('motor', 'v12'))) # no es necesario, es mas complicado
# print(auto)

#==================================================================
# Función len

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print(len(auto)) # se fija cuantas llaves tiene el diccionario
# print(len(auto['vidrios'])) 

#==================================================================
# Operador in

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# print('motor' in auto) # 'motor' esta en auto? si (True)
# print('v8' in auto['motor']) # 'v8' esta en auto['motor']? si (True)
# print('v12' in auto) # 'v12' esta en auto? no (False)
# print('v12' not in auto) # 'v12' no esta en auto? si (True)

#==================================================================
# Método clear

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# auto.clear() # el CLEAR sirve para limpiar el diccionario borrando todo
# # auto = {}
# print(auto)

#==================================================================
# Método pop

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# print(auto)
# valor = auto.pop('color') # elimina el elemento pero guarda lo que tiene dentro (la variable)
# print(auto) # imprime todo menos el elemento color
# print(valor) # imprime la variable que tenia el elemento color (Negro)

# print(auto)
# valor = auto.pop('llave1') # ya que no existe se rompe el codigo
# print(auto)
# print(valor)

# print(auto)
# valor = auto.pop('ricardo', 'este valor sale por defecto si no se encuentra la llave buscada')
# print(auto)
# print(valor)

# valor = auto.pop('ricardo', input('dame un dato'))
# valor = auto.pop('color', 'la llave color no se encontro')
# valor = auto.pop(input('dame la key...?'), [1,2,3,45]) # pide el nombre del valor que quieras eliminar, y si no esta guarda [1,2,3,45] en la variable "valor"
# print(auto)
# print(valor)
#==================================================================
'''Ejercicio 1 (Dicc)'''
'''
Deberás crear un diccionario que almacene a los ganadores de la Copa Mundial de la FIFA desde el año 1990 al 2018. Y mostrarlo por pantalla.
Datos para la resolución:
1990: 'Alemania',
1994: 'Brasil',
1998: 'Francia',
2002: 'Brasil',
2006: 'Italia',
2010: 'España',
2014: 'Alemania',
2018: 'Francia'
'''
# ganadores = {
#     1990: 'Alemania',
#     1994: 'Brasil',
#     1998: 'Francia',
#     2002: 'Brasil',
#     2006: 'Italia',
#     2010: 'España',
#     2014: 'Alemania',
#     2018: 'Francia'
# }

# print(ganadores)

#==================================================================
'''Ejercicio 2 (Dicc)'''
'''
Programa las siguientes instrucciones de forma ordenada sobre la variable animales:
1. Inicialmente el diccionario es: animales = {"elefante": ""}
2. Añade al diccionario las claves perro, tigre y mono con sus 
respectivos valores “Bobby”, “Pepe” y “Homero”
3. Modificá las claves elefante y delfin con los valores “Trompis” y 
“Manolo” respectivamente
'''
# animales = {
#     'elefante': ''
# }

# print(animales)
# animales.update({'perro': 'Bobby','tigre': 'Pepe', 'mono': 'Homero'})
# print(animales)
# animales.update({'elefante': 'Trompis', 'delfin': 'Manolo'})
# # animales['elefante'] = 'Trompis'
# # animales['delfin'] = 'Manolo'
# print(animales)














