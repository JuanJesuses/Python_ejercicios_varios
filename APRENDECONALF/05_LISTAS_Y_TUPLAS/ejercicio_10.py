""" Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por
    pantalla el menor y el mayor de los precios. """

precios = [50,75,46,22,80,65,8]

print(f"El precio más alto es {max(precios)} y el más bajo es {min(precios)}.")

# SOLUCIÓN DE LA WEB

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo es " + str(min))
print("El máximo es " + str(max))