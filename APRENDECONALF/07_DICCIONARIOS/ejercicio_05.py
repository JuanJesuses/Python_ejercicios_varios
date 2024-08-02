""" Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6,
    'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato
    <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos>
    son sus créditos. Al final debe mostrar también el número total de créditos del curso. """

asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos = 0

for clave, valor in asignaturas.items():
    creditos += valor
    print(f"{clave} tiene {valor} créditos.")

print(f"\nEl total de créditos es: {creditos}")

# SOLUCIÓN DE LA WEB

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)