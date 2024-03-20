""" Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
    Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
    teléfono es <teléfono>. """

diccionario_datos_personales = {}

name = input("¿Cual es tu nombre?: ")
age = input("¿Cual es tu edad?: ")
address = input("¿Cual es tu dirección?: ")
telephone = input("¿Cual es tu teléfono?: ")

diccionario_datos_personales['nombre'] = name
diccionario_datos_personales['edad'] = age
diccionario_datos_personales['dirección'] = address
diccionario_datos_personales['teléfono'] = telephone

print(f'{diccionario_datos_personales.get("nombre")} tiene {diccionario_datos_personales.get("edad")} años,'
      f'vive en {diccionario_datos_personales.get("dirección")} y su número de teléfono es'
      f' {diccionario_datos_personales.get("teléfono")}.')

# --------- SOLUCIÓN DE LA WEB --------- #

name = input("¿Cual es tu nombre?: ")
age = input("¿Cual es tu edad?: ")
address = input("¿Cual es tu dirección?: ")
telephone = input("¿Cual es tu teléfono?: ")

persona = {'nombre' : name, 'edad' : age, 'dirección' : address, 'teléfono' : telephone}

print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['dirección'],
      'y su número de teléfono es',persona['teléfono'],'.')