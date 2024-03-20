""" Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
    (peso / estatura) y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc>
    donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. """

peso = float(input('Introduce tu peso: '))
estatura = float(input('Introduce tu estatura: '))
estatura = pow(estatura,2)
imc = round((peso/estatura),2)

print(f'Tu índice de masa corporal es {imc}.')