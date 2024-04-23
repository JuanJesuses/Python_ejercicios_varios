""" Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el
    programa debe mostrar un error. """

num1 = int(input("Introduzca el dividendo: "))
num2 = int(input("Introduzca el divisor: "))

if num2 == 0:
    print("ERROR: no se puede dividir entre CERO.")
else:
    print('El resultado de la división es: ', round((num1/num2), 2))
