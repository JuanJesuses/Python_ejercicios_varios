""" Finger exercise: Write a program that prints the sum of the prime
    numbers greater than 2 and less than 1000. Hint: you probably want
    to use a for loop that is a primality test nested inside a for loop that
    iterates over the odd integers between 3 and 999. """

coincidencias = 0
sumaPrimos = 0

for j in range(3, 999):
    for x in range(1,j+1):
        compruebaPrimo = j % x
        if compruebaPrimo == 0:
            coincidencias += 1
    if coincidencias == 2 and j % 2 != 0:
        sumaPrimos = sumaPrimos + j
    coincidencias = 0

print('La suma de los números primos impares menores que 1000 es de:', sumaPrimos)

