""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
    (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez
    que se añada un nuevo dato debe imprimirse el contenido del diccionario. """

diccio_persona = {}
seguir = 's'

while seguir == 's':

    nombre = input("Introduzca el nombre: ")
    diccio_persona['nombre'] = nombre
    edad = int(input("Introduzca la edad: "))
    diccio_persona['edad'] = edad
    sexo = input("Introduzca el sexo: ")
    diccio_persona['sexo'] = sexo
    telefono = input("Introduzca el número de teléfono: ")
    diccio_persona['teléfono'] = telefono
    email = input("Introduzca la dirección de correo electrónico: ")
    diccio_persona['email'] = email

    for clave, valor in diccio_persona.items():
        print(f'{clave.upper()}: {valor}')

    seguir = input('¿Quiere introducir más datos (s/n)?: ')

# --------- SOLUCIÓN DE LA WEB --------- #

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"