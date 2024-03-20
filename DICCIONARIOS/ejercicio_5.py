""" Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
    {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el
    formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y
    <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso. """

creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0

for clave, valor in creditos.items():
    print(f'{clave} tiene {valor} créditos.')
    total_creditos = total_creditos + valor

print(f'\nEl curso tiene un total de {total_creditos} créditos.')

# --------- SOLUCIÓN DE LA WEB --------- #

curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0
for asignatura, creditos in curso.items():
    print(asignatura, 'tiene', creditos, 'créditos')
    total_creditos += creditos
print('Número total de créditos del curso: ', total_creditos)