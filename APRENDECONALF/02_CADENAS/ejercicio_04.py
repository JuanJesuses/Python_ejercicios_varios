""" Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del
    país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un
    número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión. """

numero = input("Introduzca el número de teléfono con el formato +cod_pais-num_telefono-ext.: ")
numero_filtrado = numero.split('-')

print(f'El número de teléfono es {numero_filtrado[1]}.')

# Solución de la web

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])