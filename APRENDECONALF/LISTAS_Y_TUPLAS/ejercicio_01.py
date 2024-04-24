""" Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia
    y Lengua) en una lista y la muestre por pantalla. """

control = ""
asignaturas = []

while control != 'n':
    asigantura = input("Introduzca la asignatura: ")
    asignaturas.append(asigantura)
    control = input("¿Desea introducir otra asignatura? (s/n): ")

print(asignaturas)

# SOLUCIÓN DE LA WEB (ESTÁ CLARO QUE NO LO HE ENTENDIDO)

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(subjects)