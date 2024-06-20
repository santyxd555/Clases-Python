# from collections import namedtuple, Counter

# instancia_de_counter = Counter('abcabc123')
# print(instancia_de_counter)
# # Counter({'a': 2, 'b': 2, 'c': 2, '1': 1, '2': 1, '3': 1})
# print(Counter((1,2,3,4,5,6,7,8,9,1,2,3,4,3,2,1,6,8,9,5,4)))
# # Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 2, 6: 2, 8: 2, 9: 2, 7: 1})

# Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])
# pescado1 = Pescado('pescesin', 'payaso', 200)
# # pescado2 = Pescado('pescesin', 'payaso')

# print(Pescado)
# # <class '__main__.Pescado'>
# print(pescado1)
# # Pescado(nombre='pescesin', especie='payaso', peso=200)
# print(pescado1.nombre)
# # pescesin
# print(pescado1[0])
# # pescesin
# print(pescado1._asdict())
# # {'nombre': 'pescesin', 'especie': 'payaso', 'peso': 200}

#======================================================================
#======================================================================

# from datetime import datetime, timedelta

# dt = datetime.now
# print(dt)

# dt_custom = datetime(2000, 1, 1)
# print(dt_custom)

# print(dt.strftime("%A %d %B %Y %I:%M"))
# print(dt.hour)

#======================================================================
#======================================================================

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(round(3.3))
# print(round(3.5))
# print(round(3.8))
# print(math.floor(3.8))
# print(math.ceil(3.3))

#======================================================================
#======================================================================

# import random

# print(random.randrange(15))
# print(random.randrange(15, 22))
# print(random.randrange(15, 28, 2))

# lista= ['hoy', 'corri', '4', 'kilometros']
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista))
# print(random.choice(lista, k=3))
# print(random.choice(lista, k=2))
# print(random.choice(lista, k=5))
# print(random.choice(lista))

#======================================================================
#======================================================================

# nombre = input('Ingrese su nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'w') # 'w' de write, el write pisa y borra todo lo del archivo

# archivo_abierto.write(nombre)

# archivo_abierto.close()

#===================================================
#===================================================

# datos_persona = {
#     'nombre' : input('Ingrese su nombre: '),
#     'apellido' : input('Ingrese su apellido: '),
#     'edad' : input('Ingrese su edad: ')
# }

# archivo_abierto = open('archivo_de_prueba.txt', 'w') # 'w' de write

# archivo_abierto.write(f'Nombre: {datos_persona["nombre"]} \nApellido: {datos_persona["apellido"]} \nEdad: {datos_persona["edad"]}')

# archivo_abierto.close()

#===================================================
#===================================================

# nombre = input('Ingrese su nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'w') # 'w' de write

# archivo_abierto.write(nombre)

# archivo_abierto.close()

# archivo_abierto = open('archivo_de_prueba.txt', 'r') # 'r' para leer, aunque si no pongo nada es lo mismo

# valor_del_archivo = archivo_abierto.read()

# print(valor_del_archivo)
# print([valor_del_archivo])

# valor_del_archivo_segunda_lectura = archivo_abierto.read()
# print(valor_del_archivo_segunda_lectura)

# linea1 = archivo_abierto.readline()
# linea2 = archivo_abierto.readline()
# linea3 = archivo_abierto.readline(4) # la cantidad de caracteres que quiero que agarre de la primera linea

# print(linea1)
# print(linea2)
# print(linea3)

# lineas = archivo_abierto.readlines()
# print(lineas)

# archivo_abierto.close()

#===================================================
#===================================================

# archivo_abierto = open('archivo_de_prueba.txt')

# valor_del_archivo = archivo_abierto.read()

# print(valor_del_archivo)
# print('###########################################')
# print(valor_del_archivo)
# print('###########################################')
# print(archivo_abierto.read())
# print('###########################################')
# archivo_abierto.seek(5) # sirve para poner a partir de que letra queres que empiece a leer
# print(archivo_abierto.read())
# print('###########################################')

# archivo_abierto.close()

#===================================================
#===================================================

# nombre = input('Ingrese su nombre: ')

# print(nombre)

# archivo_abierto = open('archivo_de_prueba.txt', 'a') # 'a' la a es de appened, para agregar, no pisa nada sino que agrega lo que escribas 

# archivo_abierto.write(nombre)

# archivo_abierto.close()

#===================================================
#===================================================

# import json

# dicc = {
#     'key1': 'valor1',
#     'key2': True,
#     'key3': None,
#     'key4': ('valor', 123)
# }

# with open('archivo_de_no_json.json', 'w') as archivo_abierto: # context manager(manejador de contexto)
#     json.dump(dicc, archivo_abierto, indent = 4) # dump = guardar, que quiero guardar, en que archivo, los espacios(tab)    

# with open('archivo_de_no_json.json', 'r') as archivo_abierto: # context manager(manejador de contexto)
#     datos = json.load(archivo_abierto) # load = leer
#     print(datos)
# print('----------------------------------------------------------------------')
# print(datos)