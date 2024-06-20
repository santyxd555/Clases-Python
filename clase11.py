# def nombre(param):
#     ...

# nombre('argumento')

#===============================================
#===============================================

# class NombreDeClase:
#     ...

# NombreDeClase() # -> crea un objeto de NombreDeClase

# nombre_de_clase1 = NombreDeClase()

# print(nombre_de_clase1) # es la ubicacion en donde esta el objeto: <__main__.NombreDeClase object at 0x7cde95253fd0>
# print(type(nombre_de_clase1)) # <class '__main__.NombreDeClase'>

#===============================================
#===============================================

# class Auto:
#     ...

# auto1 = Auto()
# auto2 = Auto()

# print(auto1)
# print(auto2)

#===============================================
#===============================================

# def asd():
#     ...

# class Auto:
#     def tocar_bocina(self): # siempre va el self para metodos de instancia
#         print('PIPIPIPI')
#         print('PIPIPIPI',self)
#     def avanzar(self, metros_a_avanzar): # el self siempre va a ser la ubicacion de la vatriable
#         print('El auto', self, 'avanzo', metros_a_avanzar, 'metros')

# auto1 = Auto() # <__main__.Auto object at 0x738735633fd0>
# auto2 = Auto() # <__main__.Auto object at 0x738735633dc0>

# print(auto1)
# print(auto2)
# auto1.tocar_bocina() # tocar_bocina(auto1)
# auto2.tocar_bocina() # tocar_bocina(auto2)
# auto1.avanzar(15) # tocar_bocina(auto1)
# auto2.avanzar(25) # tocar_bocina(auto2)