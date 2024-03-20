""" Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética.
    (3+2/2-5)**2"""

numerador = 3+2
denominador = 2-5
resultado = pow((numerador/denominador),2)

print(f'El resultado es {round(resultado,2)}')