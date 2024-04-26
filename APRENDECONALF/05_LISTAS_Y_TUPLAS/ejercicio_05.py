""" Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso
    separados por comas. """

numeros = [1,2,3,4,5,6,7,8,9,10]

for i in reversed(range(1,len(numeros))):
    print(f"{numeros[i]}", end=", ")
print("1")

# SOLUCIÓN 1 DE LA WEB

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")

# SOLUCIÓN 2 DE LA WEB

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")