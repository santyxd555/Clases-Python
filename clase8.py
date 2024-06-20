# def nuestro_len(param1,param2,otro_parametro):
#     ... # Bloque de codigo
#     return ... # Devolucion de un valor, los puntos suspensivos representan cualquier dato
# nuestro_len(argumento)

# cadena = 'Hola soy el kiosquero'

# def nuestro_len(cadena_de_afuera):
#     contador = 0
#     for _ in cadena_de_afuera: # el _ se utiliza para las variables en las que no se usa su valor
#         contador += 1
    
#     return contador # se podria decir que el return guarda la variable dentro de cadena si colocas nuestro_len(cadena), contador = cadena_de_afuera = cadena
    
# print(nuestro_len(cadena))

# cadena2 = 'Mira, compre una tele y no funciona'

# # nuestro_len(cadena)  # 21
# print(nuestro_len(cadena2)) # 35


# Ejemplo 1

def nuestro_len(datos):
    contador = 0
    for dato in datos:
        contador += 1
        if dato == 55:
            return 'El dato es 55, no te voy a terminar de contar los elementos'
    
    return contador

lista = [1,2,3,4,55,6,7,8,9]
print(nuestro_len(lista))

# Ejemplo 2

# def suma(num1, num2):
#     return num1 + num2

# print(suma(int(input('Ingrese un valor:')), int(input('Ingrese otro valor: '))))

'''
Welcome
Escribir una funcion que se le pase una cadena del nombre de una ciudad <ciudad>
y muestre por la pantalla el saludo ¡Hola bienvenido a <nombre>!
'''

# def welcome(ciudad):
#     print(f'¡Hola bienvenido a {ciudad}!')

# welcome(input('Ingrese el nombre de la ciudad: '))

'''
Media
Escribir una función que reciba una muestra de números
en una lista y devuelva su media.
'''
