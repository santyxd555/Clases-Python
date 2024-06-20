# import operaciones
# import sys
# print(sys.argv)

# valores = sys.argv[1:]

# if len(valores) == 2:
#     print(f'La suma de {valores[0]} y {valores[1]} es {int(valores[0]) + int(valores[1])}')
# else:
#     print('No me podes pasar ni mas ni de menos de 2 valores numericos')
    

# print(operaciones.suma)

#=============================================
#=============================================

# from operaciones import suma

# print(suma(5,8))

#=============================================
#=============================================

# from operaciones import suma as sumatoria

# print(sumatoria(6,9))

#=============================================
#=============================================

from matematica.operaciones import suma as sumatoria

print(sumatoria(6,9))