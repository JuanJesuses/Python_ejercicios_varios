""" Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
    pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en
    el diccionario. """

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("¿Qué simbolo de moneda quieres visualizar? "
               "Euro, Dollar o Yen: ")

print(f'El símbolo del {divisa} es {monedas.get(divisa)}.') if monedas.get(divisa) != None\
    else print("Esa moneda no existe.")

# --------- SOLUCIÓN DE LA WEB --------- #

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))