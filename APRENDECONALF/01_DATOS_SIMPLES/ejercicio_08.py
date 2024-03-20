""" Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente
    <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el
    resto de la división entera respectivamente. """

num1 = int(input("Introduzca el número 1: "))
num2 = int(input("Introduzca el número 2: "))
cociente = round((num1 / num2),2)
resto = num1 % num2

print(f'{num1} entre {num2} da un cociente de {cociente} y un resto de {resto}.')