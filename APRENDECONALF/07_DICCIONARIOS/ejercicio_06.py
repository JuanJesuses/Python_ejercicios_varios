""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo
    nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo
    dato debe imprimirse el contenido del diccionario. """

datos_personales = {}

nombre = input("Introduzca nombre: ")
datos_personales['Nombre'] = nombre
for clave, valor in datos_personales.items():
    print(f"{clave}: {valor}")
edad = input("Introduzca edad: ")
datos_personales['Edad'] = edad
for clave, valor in datos_personales.items():
    print(f"{clave}: {valor}")
sexo = input("Introduzca sexo: ")
datos_personales['Sexo'] = sexo
for clave, valor in datos_personales.items():
    print(f"{clave}: {valor}")
telefono = input("Introduzca telefono: ")
datos_personales['Teléfono'] = telefono
for clave, valor in datos_personales.items():
    print(f"{clave}: {valor}")
email = input("Introduzca correo electrónico: ")
datos_personales['e-mail'] = email
for clave, valor in datos_personales.items():
    print(f"{clave}: {valor}")

# SOLUCIÓN DE LA WEB - NO SABÍA QUE SE PODÍA HACER ESTO CON EL INPUT 'valor = input(clave + ': ')'

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"