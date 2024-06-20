'''HOLAMUNDO'''
#====================================================================

# def suma(num1, num2):
#     return num1 + num2
# print(suma(1,2))
# print(suma(2,1))

#====================================================================

# def restar(num1, num2):
#     return num1 - num2
# print(restar(1, 2))
# print(restar(2, 1))

#====================================================================

# def resta(num1, num2):
#     return num1 - num2
# print(resta(1, 2)) # -1
# print(resta(num2 = 2, num1 = 1)) # -1
# print(resta(2, num2 = 1)) # 1
# # print(resta(2, num1 = 1)) ERROR
# # print(resta(num1 = 2, 1)) ERROR

#====================================================================

# def devuelva_iterable(var1, var2, var3, var4, var5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4, var3=3, var1=1, var5=5, var2=2))
# # print(devuelva_iterable(var2=2,var4=4,3,1,5)) ERROR
# # print(devuelva_iterable(car2=2, 3,4,var1=1,5)) ERROR
# # print(devuelva_iterable(1,2,4,var3=3)) ERROR
# # print(devuelva_iterable(1,2,4,var4=3)) ERROR
# # print(devuelva_iterable()) ERROR

#====================================================================

# def devuelva_iterable(var1=10, var2=20, var3=30, var4=40, var5=50):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5)) # (1, 2, 3, 4, 5)
# print(devuelva_iterable(1,2,3,4)) # (1, 2, 3, 4, 50) 
# print(devuelva_iterable(1,2)) # (1, 2, 30, 40, 50)   
# print(devuelva_iterable()) # (10, 20, 30, 40, 50) 

# print(devuelva_iterable(15, var4=255)) # (15, 20, 30, 255, 50)
# print(devuelva_iterable(var3=255)) # (10, 20, 255, 40, 50)
# print(devuelva_iterable(var5='soy el cinco', var2=True)) # (10, True, 30, 40, 'soy el cinco')

#====================================================================

# def saludo():
#     print(variable_prueba)

# variable_prueba = 'pepe'

# saludo()

#====================================================================

# def saludo():
#     variable_prueba = 'otro gato' # otro gato # siempre se prioriza la variable local
#     print(variable_prueba)

# variable_prueba = 'pepe'

# print(variable_prueba) # pepe
# saludo()
# print(variable_prueba) # pepe # siempre se prioriza la variable local

#====================================================================

def actualizacion_de_dato(parametro):
    parametro = 5
    print(parametro)
    return parametro

dato = 2

print(dato) # 2
actualizacion_de_dato(dato)
pepe = actualizacion_de_dato(dato) # 2

#====================================================================

# def actualizacion_de_dato(parametro):
#     parametro = 'tres'

# dato = 'asd'

# print(dato) # asd
# actualizacion_de_dato(dato)
# print(dato) # asd

#====================================================================

# def actualizacion_de_dato(parametro):
#     parametro.append([1, 2, 3, 'pepito', True])

# dato = [1,2,3,'pepito']
# print(dato) # [1, 2, 3, 'pepito']
# actualizacion_de_dato(dato)
# print(dato) # [1, 2, 3, 'pepito', True]

#====================================================================

# def actualizacion_de_dato(parametro):
#     parametro.append([1, 2, 3, 'pepito', True])

# dato = [1,2,3,'pepito']
# print(dato) # [1, 2, 3, 'pepito']
# actualizacion_de_dato(dato.copy()) # .copy o [:]
# print(dato) # [1, 2, 3, 'pepito']

#====================================================================

# *args y **kwargs
# args puede ingrsar cuqlueir tipo de cantidad de datos

# def suma(*args):
#     print(type(args)) # tuple
#     print(args)
# suma()

# def suma(*datos):
#     # print(type(datos)) # tuple
#     # print(datos)
#     suma=0
#     for valor in datos:
#         suma+=valor # 0+1, 1+2, 3+4 = 7
#     return suma

# print(suma(1,2,4))

#====================================================================

# print('pepe fort se fue de viaje')
# print('pepe','fort','se','fue','de','viaje')
# print('pepe','fort','se','fue','de','viaje', sep=',') # loq eu coloques dentro del sep se coloca entre las variables de ls lista
# print('pepe','fort','se','fue','de','viaje', sep=',', end=' ')
# print('Hola mundo')

# ====================================================================

# def mostrar(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for llave, valor in kwargs.items():
#         print(f'llave: {llave} --> valor: {valor}')

# mostrar(nombre='Pepito', apellido='Grillo')

# def prueba_multiples_parametros(numero, *args, **kwargs):
#     print(numero)
#     print(args)
#     print(kwargs)    

# prueba_multiples_parametros(15,26,True,-29391,'pepito',marca='ford',kilometros=24) 
# numero: 15
# args: (26, True, -29391, 'pepito')
# kwargs: {'marca': 'ford', 'kilometros': 24}







