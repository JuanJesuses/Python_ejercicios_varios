""" Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene
    y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una
    tupla con la palabra más repetida y su frecuencia. """

def frecuencia_palabras(cadena):
    # Función que devuelve diccionario con una palabra como clave y su frecuencia de aparición como valor

    diccionario = {}
    palabras = cadena.split()
    print(palabras)

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1


    return diccionario

texto = """la Ley 39/2015, de 1 de octubre, de la Ley de Procedimiento Administrativo Común de las
        Administraciones Públicas, una vez concluida la instrucción del procedimiento de desahucio administrativo sobre
        vivienda protegida,  DAD-AL-2024-0048  en el que ustedes están afectados y antes de redactar la Propuesta de Resolución,
        por la presente se le otorga Trámite de Audiencia, con objeto de que en el plazo de quince días hábiles, pueda ver el
        expediente, formular alegaciones y presentar documentos que a su derecho convenga.
        La consulta del expediente administrativo podrá realizarla en la sede de esta Dirección Provincial, sita en calle
        Canónigo Molina Alonso, n.º 8, 6ª planta en Almería, previa solicitud de cita en el teléfono  950.15.36.16.
        Del mismo modo, les volvemos a remitir modelo de AUTORIZACIÓN a esta Agencia de Vivienda y Rehabilitación de Andalucía
        para que, en el caso de que lo consideren oportuno, lo devuelvan firmado, con el objetivo de dar conocimiento a los
        Servicios Públicos en materia de política social, a los efectos oportunos."""
print(frecuencia_palabras(texto))
