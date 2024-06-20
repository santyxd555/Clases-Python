''' Operadores aritmeticos '''

# print(2+2) # Suma
# print(2*2) # Multiplicacion
# print(3-2) # Resta
# print(3**2) # Potencia (3 a la 2 = 3x3 = 9)
# print(3/2) # Division
# print(3//2) 
# print(3%2) # Modulo (el resto de una division entera)

# Tipo de datos logicos

# False (0)
# True (1)

# Casteando
# bool()

# print(True + 5)

# = es para igualar
# == para comparar igualdad
# !=
# !==

# print('a' == 'a') # Compara las variables
# print('a' == 'A')
# print('a' != 'A')
# print('a' < 'A')
# print('a' > 'A')

# print('a' + 1) No se puede hacer
# print(ord('a')) # el 'ord' te pone que numero es la variable que seleccionaste

# print(bool(0))

# expresiones = [
#     False == True,
#     10 >= 2*4,
#     33/3 == 11,
#     True > False,
#     1*5 == 2.5*2
# ]
# print(expresiones)


''' Operadores Logicos '''
# and or not

''' NOT: no '''
# (negar) el not va sobre el valor logico(booleano)

# print(True)
# print(not True)
# print(not 5) # -> print(not bool(5))
# print(not {1,2,3,4,'pepito'}) # -> print(not bool({1,2,3,4,'pepito'}))
# print(not {}) # -> print(not bool({}))
# si la lista, diciionario o cualquiera esta vacio es false


''' AND: y '''
# (si el primer valor es falso no revisa el segundo, si es verdadero revisa el segundo)

# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False

# print(True and True)
# print(5 == 1 and 4 < 3)
# print(5 == 1 and 'asdfq' != 'a')

# print(True and 4/0)
# print(False and 4/0)

# print(5 and {1,2,3,4,'pepito'})


''' OR: o '''
# (si el primero es verdadero para ahi y no revisa lo que sigue, si es falso pasa al otro valor)

# True and True -> True
# True and False -> True
# False and True -> True
# False and False -> False

# print(55 == 60 or 1.5 == 1.5)
# print(60 == 60 or 1.5 == 1.5)
# print(55 == 60 or 1.5 == 1.4)

# print(True and 4/0)
# print(False and 4/0)

# print(5 or {1,2,3,4,'pepito'})

'''
## EXPRESIONES ANINADADAS
1. Expresiones de cualquier tipo entre parentesis.
2. Expresiones aritmeticas por sus propias reglas.

()  ->  ** ->  / // * %  ->  + -
primero -> segundo -> tercero -> cuarto

3. Expresiones relacionales de izquierda a derecha.
4. Operadores logicos (not tiene prioridad ya que afecta al operador)
'''

# suma = 0
# suma += 1
# suma += 2
# suma += 3
# suma += 6

# print(suma) # 12

# texto = 'pepito'
# texto += ' corre'
# texto += ' solo'

# print(texto) # pepito corre solo

# suma = 0
# suma += 1
# print(suma)
# suma -= 2
# print(suma)
# suma *= 3
# print(suma)
# suma /= 6
# print(suma)
# suma %= 6 # modulos
# print(suma)

# texto = 'pepito'
# texto += ' corre-'
# texto *= 5
# print(texto)


## Ejercicio 3 

nombre = input('Ingrese su nombre:')
edad = int(input('Ingrese su edad:'))

resultado = nombre != '****' and 5 < edad < 20 and 4 <= len(nombre) < 8 and edad * 3 > 35

print(resultado)








