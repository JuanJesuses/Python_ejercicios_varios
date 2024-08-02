""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
    Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
    teléfono es <teléfono>. """

datos_personales = {}

nombre = input("Introduzca el nombre: ")
datos_personales['Nombre'] = nombre
edad = input("Introduzca la edad: ")
datos_personales['Edad'] = edad
direccion = input("Introduzca domicilio: ")
datos_personales['Domicilio'] = direccion
telefono = input("Introduzca teléfono: ")
datos_personales['telefono'] = telefono

print(f"{datos_personales['Nombre']} tiene {datos_personales['Edad']}, vive en {datos_personales['Domicilio']} y su número de teléfono es {datos_personales['telefono']}")

# SOLUCIÓN DE LA WEB

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])

