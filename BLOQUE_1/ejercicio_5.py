""" Escribe una función que tome tres números y devuelva el más grande. """

def mayorQue(num1, num2, num3):

    mayor = 0

    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    elif num3 > num1 and num3 > num2:
        mayor = num3

    return mayor

print(mayorQue(21,709,2))