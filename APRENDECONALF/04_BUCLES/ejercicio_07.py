""" Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(11):
    print(f"1 x {i} = {1*i}") """

for i in range(1,11):
    print(f"\nTABLA DEL {i}\n")
    for j in range(11):
        print(f"{i} x {j} = {i*j}")


