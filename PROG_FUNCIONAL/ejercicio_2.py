""" Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente,
    exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y mostrará
    por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función
    a esos enteros. """

def escogerOpcion():

    mostrarMenu()
    opcion = int(input("¿Qué quieres calcular?: "))

    while opcion > 0 and opcion < 6:
        if opcion == 1:
            calcularSeno()
        elif opcion == 2:
            calculaCoseno()
        elif opcion == 3:
            calcularTangente()
        elif opcion == 4:
            base = int(input("Introduce la base: "))
            exp = int(input("Introduce el exponente: "))
            print("El total es: ",calcularExponencial(base,exp))

        pregunta = input("¿Quieres realizar otro cálculo?: ")
        print()

        if pregunta == 's':
            mostrarMenu()
            opcion = int(input("Escoge una opción del menú: "))
        else:
            opcion = 7

def mostrarMenu():
    print()
    print("**************************************")
    print("*** --- CALCULADORA CIENTÍFICA --- ***")
    print("**************************************")
    print()
    print("1. CALCULAR SENO")
    print("2. CALCULAR COSENO")
    print("3. CALCULAR TANGENTE")
    print("4. CALCULAR EXPONENCIAL")
    print("5. CALCULAR LOGARITMO NEPERIANO")
    print("6. SALIR DE LA CALCULADORA")
    print()

def calcularSeno():
    hipotenusa = int(input("Introduce la hipotenusa: "))
    opuesto = int(input("Introduce el lado opuesto: "))
    seno = opuesto / hipotenusa
    return seno

def calculaCoseno():
    hipotenusa = int(input("Introduce la hipotenusa: "))
    adyacente = int(input("Introduce el lado adyacente: "))
    coseno = adyacente / hipotenusa
    return coseno

def calcularTangente():
    opuesto = int(input("Introduce el lado opuesto: "))
    adyacente = int(input("Introduce el lado adyacente: "))
    tangente = opuesto / adyacente
    return tangente

def calcularExponencial(base, exp):

        if exp == 0:
            return 0
        if exp == 1:
            return base
        else:
            return base * calcularExponencial(base, exp - 1)


def calcularLogaritmoNepe():
    pass

escogerOpcion()