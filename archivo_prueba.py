# class Auto:
#     def __init__(self):
#         self.marca = 'Ford'
#         self.modelo = 'K'
#         print(f'Se creo {self}')

# auto = Auto()

# print(f'Su auto {auto.marca} es {auto.modelo}')

#================================================
#================================================

# class Motor:
#     def __init__(self, numero_serie, cant_cilindros = 6):
#         self.numero_serie = numero_serie
#         self.cant_cilindros = cant_cilindros
        
# class Auto:
    
#     def __init__ (self, marca, modelo, color='Blanco', **datos_de_motor):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color
#         self.motor = Motor(**datos_de_motor)
#         print(f'Se creo el auto {self}')
    
#     def __str__(str):
#         return f'Return de el __str__ {}'
    
#     def tocar_bocina(self):
#         print("PIIIIIIPIIIIIIIII", self)

#     def encender(self, metros_a_avanzar):
#         print("Encendiendo", self, 'avanzó', metros_a_avanzar, 'metros')

# auto1 = Auto('Ford', 'K', 'Rojo', numero_serie = 123456, cant_cilindros = 12)

# print(auto1)fff