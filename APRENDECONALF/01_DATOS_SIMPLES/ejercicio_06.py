""" Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma
    de todos los enteros desde 1 hasta n. La suma de los primeros enteros positivos puede ser calculada de la
    siguiente forma: (n(n+1))/2 """

num = int(input('Introduce un número: '))
resultado = int((num*(num+1))/2)

print(f'La suma de todos los enteros desde 1 hasta {num} es: {resultado}.')