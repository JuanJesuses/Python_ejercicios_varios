""" Escribir una función que reciba un número entero positivo y devuelva su factorial. """

def factorial(num):
    "Función que devuelve el factorial del número pasado por parámetro"
    facto = 1
    for i in range(1,num):
        facto = facto + (facto*i)

    return facto

numero = int(input("Introduzca un número para su factorial: "))
print(factorial(numero))
