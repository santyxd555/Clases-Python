
'''Listas'''

# print([25, 34, 'hola', 'otro string', 3]) 
# # [25, 34, 'hola', 'otro string', 3]
# type([25, 34, 'hola', 'otro string', 3]) 
# # list

''' list.clear() ''' # para limpiar una lista

'''Listas y Strings'''

#           013456789... 
# cadena = 'esta es cadena de prueba'
# print(cadena[5]) # e

# lista = [1, 2, 3, 'pepe', 'roque']
#          0  1  2     3       4  -> Subiendo...
#         -5 -4 -3    -2      -1  
# print(lista[3])  # pepe
# print(lista[-1]) # roque

# Estos 2 accesos generan un error
# print(cadena[55]) -> Se produce un error
# print(lista[55])  -> Se produce un error

'''Slicing'''

# cadena = 'esta es cadena de prueba'
# print(cadena)
# esta es cadena de prueba
# print(cadena[4:8])
# es
# print(cadena)
# esta es cadena de prueba


# lista = [1, 2, 3, 'pepe', 'roque']
# print(lista) # [1, 2, 3, 'pepe', 'roque']
# print(lista[2:4]) # [3, 'pepe', 'roque']
# print(lista) # [1, 2, 3, 'pepe', 'roque']

# Para poder volver a utilizar el valor en el futuro

# segunda_lista = lista[2:4]
# print(segunda_lista) # [3, 'pepe']
# print(lista) # [1, 2, 3, 'pepe', 'roque']

# segunda_lista = lista[::2]
# print(segunda_lista) # [1, 3, 'roque']
# print(lista) # [1, 2, 3, 'pepe', 'roque']


'''Concatenacion'''

# cadena = 'esta es cadena de prueba'
# cadena_concatenada = cadena + ' soy pepe'
# print(cadena_concatenada) # esta es cadena de prueba soy pepe

# lista1 = [1, 2, 3, 'pepe', 'roque']
# lista_concatenada = lista1 + cadena
# lista_concatenada = lista1 + [cadena, 123]
# lista2 = [cadena]
# print(lista1) # [1, 2, 3, 'pepe', 'roque']
# print(lista2)
# lista_concatenada = lista1 + lista2
# print(lista_concatenada) # [1, 2, 3, 'pepe', 'roque', 'esta es cadena de prueba', 123]

# cadena1 = 'esta es cadena de prueba'
# cadena2 = ' otro gato'
# print(cadena1 + cadena2)
# lista1 = [1, 2, 3,'pepe', 'roque']
# lista2 = [6,7,8,1]
# print(lista1 + lista2)
# print(lista1 + [cadena1])

'''Inmutabilidad/Mutabilidad'''

# cadena = 'claro'
# cadena[3] = 's' # esto no se puede, ocurre un error
# cadena = cadena[:3] + 's' + cadena[4:]
# print(cadena) # claso

#              0          1          2
# lista = ['primero', 'segundo', 'tercero']
# print(lista) # ['primero', 'segundo', 'tercero']
# print(lista[1]) # segundo
# lista[1] = 'cuarto'
# print(lista) # ['primero', 'cuarto', 'tercero']
# print(lista[1]) # cuarto
# lista[1] = 123
# print(lista) # ['primero', 123, 'tercero']
# print(lista[1]) # 123
# lista[1] = [1,2,3,4,5,'eaea'] # agrega una lista adentro de otra lista
# print(lista) # ['primero', [1, 2, 3, 4, 5, 'eaea'], 'tercero']
# print(lista[1]) # [1, 2, 3, 4, 5, 'eaea']

'''Asignacion por slicing'''

#              0          1          2          3        4
# lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# print(lista) # ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# print(lista[1:3]) # ['segundo', 'tercero']

# lista[1:3] = [2, 3,'otro dato en string']
# print(lista) # ['primero', 2, 3, 'otro dato en string', 'cuarto', 'quinto']

# lista[1:3] = ['mas datos']
# print(lista) # ['primero', 'mas datos', 'otro dato en string', 'cuarto', 'quinto']

# lista[1:3] = []
# print(lista) # ['primero', 'cuarto', 'quinto']

# print(lista[1:3]) # ['cuarto', 'quinto']
# lista[1:3] = ['soy', 'mas', 'de', 'un', 'valor']
# print(lista) # ['primero', 'soy', 'mas', 'de', 'un', 'valor']

# lista[1:3] = 'hola'
# print(lista) # ['primero', 'h', 'o', 'l', 'a', 'de', 'un', 'valor']

# print(list('hola')) # ['h', 'o', 'l', 'a']
# print(list(2)) # un numero no te lo puede transformar en lista

# lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# lista[1:3] = ['soy', 'mas', 'de', 'un', 'valor']
# print(lista) # ['primero', 'soy', 'mas', 'de', 'un', 'valor', 'cuarto', 'quinto']


# lista[1:5] = []
# print(lista) # ['primero', 'valor', 'cuarto', 'quinto']

# lista[1:3] = 'pepe'
# print(list('hola')) # -> ['h', 'o', 'l', 'a']
# print(lista) # ['primero', 'p', 'e', 'p', 'e', 'cuarto', 'quinto']

# # lista[1:3] = 4 # genera un error
# lista[1:3] = [4] # remplaza las variables 1 y 2 por el numero 4
# print(lista) # ['primero', 4, 'cuarto', 'quinto']


'''Borrar valores con slicing o vaciar lista'''

# lista = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# print(lista) # ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
# lista[1:3] = [] # borra los datos 1 y 2
# print(lista)# ['primero', 'cuarto', 'quinto'] 
# lista[1:3] = []
# print(lista) # ['primero']
# # lista[::2] = [] # Genera error ya que no les permite la asignación con el salto de valores
# lista = [] 
# print(lista)# []

'''Funciones de listas'''

'''Appened'''
# Agrega un elemento al final de la lista.

# lista = [1, 2, 3, 'pepe', 'roque']
# print(lista) # [1, 2, 3, 'pepe', 'roque']

# [1, 2, 3, 'pepe', 'roque'].append('otro valor')
# lista.append('otro valor') # El punto sirve para pedir algo
# print(lista) # [1, 2, 3, 'pepe', 'roque', 'otro valor'] 

# Estas son dos maneras
# lista.append(['otro valor', 2]) # utilizando la funcion appened
# print(lista) # [1, 2, 3, 'pepe', 'roque', 'otro valor', ['otro valor', 2]]
# lista = lista + ['otro valor', 2] # utilizando el signo de suma
# print(lista) # [1, 2, 3, 'pepe', 'roque', 'otro valor', ['otro valor', 2]]

'''Len'''
# Se utiliza para contar cuantas variables tiene una lista

#        0  1  2     3       4   = 5 (hay 5 en total)
# lista = [1, 2, 3, 'pepe', 'roque']
# print(len(lista)) # 5

'''Pop'''
# Elimina y devuelve el elemento en una posición específica de la lista.

# lista = [1, 2, 3, 'pepe', 'roque']  # elimina la ultima variable de la lista o el elemento que selecciones
# lista.pop(2) # elimina lo quue hay en la posision 2
# print(lista) # [1, 2, 'pepe', 'roque']

# valor_extraido = lista.pop() # elimina la ultima variable de la lista y se guarda la variable en otra (valor_extraido)
# print(lista) # [1, 2, 3, 'pepe']
# print(valor_extraido) # roque
# valor_extraido = lista.pop(3) # se elimina la variable numero 3 y se guarda en otra variable (valor_extraido)
# print(lista) # [1, 2, 3]
# print(valor_extraido) # pepe

'''Count'''
# cuantas veces aparece la variable en una lista

# lista = [1, 2, 3, 'pepe', 2, 'roque', 2]
# print(lista.count()) -> no funciona ya que no se selecciona ninguna variable
# print(lista.count(2)) # cuantas veces aparece el numero 2 en la lista
# print(lista.count(4)) # cuantas veces aparece el numero 4 en la lista
# print(lista.count('pepe')) # cuantas veces aparece el nombre pepe en la lista

'''Index'''
# Devuelve el índice de la primera aparición de un elemento específico en la lista.

# lista = ['pepe', 1, 2, 3, 'pepe', 'roque', 'pepe']
# print(lista.index('pepe')) # 0 (devuelve un 0 ya que aparece en la primera variable)
# print(lista.index('pepe', 3)) # 4 (devuelve el 4 ya que empieza desde la tercer variable)
# print(lista.index('pepe', 5, 7)) # 6 (busca desde la variable 5 a la variable 7)
# print(lista.index('pepe', 7)) -> se rompe el programa ya que no existe  

# print(lista.index('salto')) # genera error al no encontrar el dato que se busca


'''Tuplas'''
# Las tuplas no se pueden modificar

# lista = [1,2,3,'pepe','gato']
# tupla = (1,2,3,'pepe','gato')   
# tupla1 = 1,2,3,'pepe','gato' # si no se colocan los parentesis lo toma como si fuese una tupla

# print(type(lista))  # <class 'list'>
# print(type(tupla))  # <class 'tuple'>
# print(type(tupla1)) # <class 'tuple'>


# lista = [2]
# tupla = ('2') # string (cuando hay solo un valor lo toma como un string)
# tupla = ('2',) # tupla (si hay una coma lo cuenta como si hubiese mas de una variable y lo toma como una tupla)
# tupla = ('pepe',) # tupla 
# tupla = (2,) # tupla
# tupla = (2) # int
# tupla = 2, # tupla
# tupla = 2, 3, 4, 5 # tupla
# print(tupla)
# print(type(lista))
# print(type(tupla))

'''Inmutabilidad'''
# las tuplas no se pueden modificar

# lista = [1,2,3,'pepe','gato']
# lista[1] = 'otro valor'
# print(lista)

# tupla = (1,2,3,'pepe','gato')
# tupla[1] = 'otro valor' # aparece un error ya que las tuplas no se pueden modificar
# print(tupla)

'''Vaciar'''

# tupla = (1,2,3,'pepe','gato')
# print(tupla) # (1,2,3,'pepe','gato')
# print(type(tupla)) # <class 'tuple'>
# tupla = () # asi se vacia una tupla
# print(tupla) # () (no hay nada)
# print(type(tupla)) # <class 'tuple'>
# tupla = tuple() # estas poniendo que la variable "tupla" sea una tuple
# print(type(tupla)) # <class 'tuple'>

# tupla = tuple([2,3,4]) # se modifica la lista y se transforma a una tupla y se guarda en una variable
# print(type(tupla)) # <class 'tuple'>
# print(tupla) # (2, 3, 4) (es una tupla)
# lista_nueva = list(tupla) # convierte la tupla a una lista
# print(lista_nueva) # [2, 3, 4]

# lista = list()
# print(type(lista)) # <class 'list'>

# print(list('ricardo'))  # ['r', 'i', 'c', 'a', 'r', 'd', 'o']
# print(tuple('ricardo')) # ('r', 'i', 'c', 'a', 'r', 'd', 'o')

'''Index y Slicing'''

# #        0 1 2    3     4  
# tupla = (1,2,3,'pepe','gato')
# print(tupla[2])   # 3
# print(tupla[1:])  # (2, 3, 'pepe', 'gato')
# print(tupla[::2]) # (1, 3, 'gato')
# print(tupla)      # (1, 2, 3, 'pepe', 'gato')

'''Concatenacion'''

# tupla1 = (1,2,3)
# tupla2 = ('pepe','gato')
# tupla3 = tupla1 + tupla2
# print(tupla3) # (1, 2, 3, 'pepe', 'gato')
# tupla1 = tupla1 + tupla3
# print(tupla1) # (1, 2, 3, 1, 2, 3, 'pepe', 'gato')

'''Fucnion de Tuplas'''

'''Len'''

# #          0 1 2   3      4 
# tupla34 = (1,2,3,'pepe','gato')
# print(len(tupla34)) # 5

'''Count'''
# cuantas veces aparece la variable en una tupla

# tupla = (1,'pepe', 2,3,'pepe','gato','pepe')
# print(tupla.count('pepe')) # 3
# print((1,'pepe', 2,3,'pepe','gato','pepe').count('pepe')) # 3

'''Index ( salteos para buscar, inexistencia )'''

# tupla = ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')
# print(tupla.index('pepe')) # 0
# print(tupla.index(1)) # 1
# print(tupla.index('pepe', 1)) # 4
# print(tupla.index('pepe', 5, 7)) # 6
# print(tupla.index('pepe', 7)) # error ya que no esta

# print(tupla.index('salto')) # genera error al no encontrar el dato que se busca

'''Casting'''

# tupla = ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')
# print(tupla) # ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')
# lista_desde_tupla = list(tupla)
# print(lista_desde_tupla) # ['pepe', 1, 2, 3, 'pepe', 'roque', 'pepe']

# tupla_desde_lista = tuple(lista_desde_tupla)
# print(tupla_desde_lista) # ('pepe', 1, 2, 3, 'pepe', 'roque', 'pepe')

'''Anidacion (acceso)'''

# lista = [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')]
# print(lista)
# print(lista[-1][0]) # es como hacer esto --> print(('tupla, 'tupla2')[0])
# print(('tupla', 'tupla2')[0]) # esto es lo mismo que lo de arriba 
# lista[-2][0] = 2
# print(lista)

# tupla = (1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2'))
# print(tupla)
# print(tupla[-1][0])
# print(tupla[-2][0])
# print(tupla[5][0])
# tupla[-2][0] = 2
# print(tupla)

'''''' # Estas 4 opciones fncionan igual (todas imprimen t)
# print(tupla[5][1][2])
# print(['lista', 'interna'][1][2])
# print('interna'[2])
# print('t')
''''''

# lista = [1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2')]

# print(lista[-1]) # ('tupla', 'tupla2')
# print(lista[-1][1]) # tupla2
# print(len(lista[-1])) # 2 ( imprime dos ya que hay dos variables en esta lista)
# lista[-2][1] = 'otra lista'
# lista[-1][1] = 'otra lista' # Genera error
# print(lista) # [1, 2, 3, 'pepe', 'gato', ['lista', 'otra lista'], ('tupla', 'tupla2')]
# print(lista[-1]) # ('tupla', 'tupla2')

# Convierte la lista a una tupla
# print(tuple(lista)) # (1, 2, 3, 'pepe', 'gato', ['lista', 'otra lista'], ('tupla', 'tupla2'))

# tupla = (1,2,3,'pepe','gato', ['lista', 'interna'], ('tupla', 'tupla2'))
# print(tupla) # (1, 2, 3, 'pepe', 'gato', ['lista', 'interna'], ('tupla', 'tupla2'))
# tupla[-2][1] = 'otra lista'
# print(tupla) # (1, 2, 3, 'pepe', 'gato', ['lista', 'otra lista'], ('tupla', 'tupla2'))
# ya que hay una lista adentro de una tupla se puede modificar

'''
Descripción de la actividad.

En esta actividad, podrás poner en práctica todo lo aprendido durante la sesión.

Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3
'''

lista1 = [1, 2, 3, 4, 'pepe', 'hola']
lista2 = [1, 5, ('mi', 'gato'), 'richard']

lista1.append(456789)
lista1.append('Hola Mundo')

lista2[6:] = ['Hola y Adios',5555]

lista3 = lista1[:-1]

lista4 = lista2[1:-1]

lista5 = lista4 + lista3

print(lista1) # [1, 2, 3, 4, 'pepe', 'hola', 456789, 'Hola Mundo']
print(lista2) # [1, 5, ('mi', 'gato'), 'richard', 'Hola y Adios', 5555]
print(lista3) # [1, 2, 3, 4, 'pepe', 'hola', 456789]
print(lista4) # [5, ('mi', 'gato'), 'richard', 'Hola y Adios']
print(lista5) # [5, ('mi', 'gato'), 'richard', 'Hola y Adios', 1, 2, 3, 4, 'pepe', 'hola', 456789]





























