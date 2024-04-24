""" Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no. """

num = int(input("Introduza un número entero: "))
contador = 0
resultado = 0

if num % 2 == 0:
    print("El número introducido no es primo.")
else:
    for i in range(num):
        resultado = num % (num - i)
        if resultado == 0:
            contador += 1

if contador > 2:
    print(f"El número {num} no es primo")
else:
    print((f"El número {num} es primo"))


# SOLUCIÓN 1 DE LA WEB

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

# SOLUCIÓN 2 DE LA WEB

n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")