# class Auto:
    
#     def ___init__ (self):
#         self.marca = 'Ford'
#         self.modelo = 'K'
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto()
# auto2 = Auto()

# print('Este el es auto 1', auto1)
# print(auto1.marca, auto1.modelo)

# print('Este el el auto 2', auto2)
# print(auto2.marca, auto2.modelo)

#===========================================================================
#===========================================================================

# class Auto:
    
#     def ___init__ (self, marca, modelo, color = 'Blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')


# print('Este el es auto 1', auto1)
# print(auto1.marca, auto1.modelo)

# print('Este el el auto 2', auto2)
# print(auto2.marca, auto2.modelo)

# print('Este el el auto 2', auto3)
# print(auto3.marca, auto3.modelo)

#===========================================================================
#===========================================================================

# class Auto:
    
#     def __init__ (self, marca, modelo, color = 'Blanco'):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.cant_ruedas = 4
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')
#         # Se creo el auto <__main__.Auto object at 0x70cbe9f3fe20>
#         # Se creo el auto <__main__.Auto object at 0x70cbe9f3fdc0>
#         # Se creo el auto <__main__.Auto object at 0x70cbe9f3fca0>

# auto1 = Auto('Ford', 'K', 'Rojo')
# auto2 = Auto('Fiat', 'Uno', 'Verde')
# auto3 = Auto('Renault', '18')

# auto1.cant_ruedas = 5 
# print(auto1.cant_ruedas) # 4
# print(auto2.cant_ruedas) # 4
# print(auto3.cant_ruedas) # 4

#===========================================================================
#===========================================================================

#v1
# class Motor:
#     def __init__(self, cant_cilindros = 6):
#         self.cant_cilindros = cant_cilindros

# class Auto:
#     def __init__ (self, marca, modelo, color = 'Blanco', cant_cilindros = 6):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(cant_cilindros)
#         print(f'Se creo el auto {self}')

#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo')

# print(auto1.motor)
# print(auto1.motor.cant_cilindros)

#===========================================================================
#===========================================================================

#v2
# class Motor:
#     def __init__(self, numero_serie, cant_cilindros = 6):
#         self.numero_serie = numero_serie
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     def __init__ (self, marca, modelo, color = 'Blanco', **kwargs):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**kwargs)
#         print(f'Se creo el auto {self}')
    
#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo', n_serie = 123456, cant_cilindros = 12)

# print(auto1.motor)
# print(auto1.motor.numero_serie)
# print(auto1.motor.cant_cilindros)

#===========================================================================
#===========================================================================


class Motor:
    def __init__(self, numero_serie, cant_cilindros = 6):
        self.numero_serie = numero_serie
        self.cant_cilindros = cant_cilindros
        
class Auto:
    
    def __init__ (self, marca, modelo, color='Blanco', **datos_de_motor):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = Motor(**datos_de_motor)
        print(f'Se creo el auto {self}')
    
    def tocar_bocina(self):
        print("PIIIIIIPIIIIIIIII", self)

    def encender(self, metros_a_avanzar):
        print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo', numero_serie = 123456, cant_cilindros = 12)

# print(auto1)

#===========================================================================
#===========================================================================

class Concesionaria:
    def __init__(self, concesionaria):
        self.concesionaria = concesionaria
    
    def __str__(self):
        return f'Listado de autos en la concesionaria {self.concesionaria}'
    
    def __len__(self):
        return len(self.autos)
    
    def agregar_autos():
        if auto and auto.color.capitalize() == 'Negro':
            self.autos.append(auto)
        else:
            print('Te falto el auto de color negro')

concesionaria = Concesionaria('Pepito')
print(concesionaria)
print(len(concesionaria))
