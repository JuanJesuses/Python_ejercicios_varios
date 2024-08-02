""" Escribir un programa que almacene las matrices

        1  2  3              -1  0
    A =            y    B =   0  1
        4  5  6               1  1


    en una lista y muestre por pantalla su producto.
    Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una
    lista. """

A = (1,2,3),(4,5,6)
B = (-1,0),(0,1),(1,1)
producto = 0
print(len(A), len(B))

for i in range(len(A)-1):
    #print(A)
    for j in range(len(B)-1):
        print(A[i], B[j])
        #producto += A[i]*B[j]

print(f"El producto de los vectores {str(A)} y {str(B)} es {str(producto)}")

# SOLUCIÓN DE LA WEB. NO HE CONSEGUIDO SACAR EL EJERCICIO

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])