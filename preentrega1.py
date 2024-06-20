""" PreEntrega_1"""
'''
Subimos un colab
Nombre del archivo: Mi nombre y apellido o apellido y nombre+Entrega1 o PrimeraEntrega
'''
'''
Que tenga funciones
Que se pida regitrar un usuario con nombre y contraseña
Una funion para almacenar(guardar la informacion) y otra para mostrar la informacion
Usar un diccionario para guardae el usuario-contraseña(clave-valor)
Que haya un for para mostrar todos lo usuarios y cointraseñas 
o que pongas tu nombre y te indique la contraseña
quie haya otra funcion que pida ingresar el usuario y contraseña, y que coincidan con los datos guardados
'''
def almacen():
    bandera = True
    base_de_datos = {}
    
    while bandera:
        print('''
Seleccione una opcion
1. Registrar Usuario
2. Iniciar Sesion
3. Mostrar Usuario
4. Cambiar contraseña
5. Salir
''')
        opcion = input('Ingrese una opcion: ')
        
        if opcion == '1':
            usuario = input('Ingrese su nuevo nombre de usuario: ')
            contrasena = input('Ingrese la nueva contraseña: ')
            if usuario in base_de_datos:
                impre = '\nNombre de usuario ya registrado por favor registre otro:'
            else:
                base_de_datos.update({usuario: contrasena})
                impre = '\nEl usuario se a registrado de forma exitosa'
            impresion(impre)
            
        elif opcion == '2':
            usuario = input('Ingrese su nombre de usuario: ')
            contrasena = input('Ingrese la contraseña: ')
            impre = verificacion(base_de_datos, usuario, contrasena)
            impresion(impre)
            if impre == '\nIniciaste sesion\nBienvenido':
                bandera = False
                
        elif opcion == '3':
            usuario = input('Ingrese un usuario: ')
            for indice1, indice2 in base_de_datos.items():
                if indice1 == usuario:
                    impre = f'\nLa contraseña del usuario <{indice1}> es <{indice2}>'
                    break
                else:
                    impre = '\nEl usuario no existe'
            impresion(impre)
            
        elif opcion == '4':
            usuario = input('Ingrese el usuario al que desea cambiarle la contraseña: ')
            for indice1, indice2 in base_de_datos.items():
                if indice1 == usuario:
                    indice2 = input('Ingrese la nueva contraseña: ')
                    if indice2 != contrasena:
                        impre = '\nEl cambio se a hecho con exito'
                        base_de_datos.update({usuario: indice2})
                    else:
                        impre = '\nA ingresado la misma contraseña, Ingrese otra por favor: '
                        break
                else:
                    impre = '\nEl usuario no existe'
            impresion(impre)
            
        elif opcion == '5':
            impre = '\nSaliendo'
            bandera = False
            impresion(impre)
        else:
            impre = '\nOpcion no encontrada, Ingrese otra por favor:'
            impresion(impre)


def impresion(impre):
    print(impre, '\n')
    
def verificacion(datos, usuario, contrasena):
    for indice1, indice2 in datos.items():
        if indice1 == usuario and indice2 == contrasena:
            impre = '\nIniciaste sesion\nBienvenido'
            break
        elif indice1 != usuario and indice2 != contrasena:
            impre = '\nEl usuario o la contraseña son incorrectas'
        elif indice1 == usuario and indice2 != contrasena:
            impre = '\nLa contraseña es incorrecta'
            break
            
    return impre

almacen()

'''https://colab.research.google.com/drive/1q5OOtkDNXZk5N8EY4NTvhd32gtiiCnrg?usp=sharing'''
'''Agregar cosas de la clase 15 diapositiva 18'''