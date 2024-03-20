"""
def factorial_r(n): #Declaro una función llamada factorial
  if (n==1) or (n==0): #Controlo los dos valores que siempre dan uno en un factorial, el 1 y el 0
    return 1 #Si esto se cumple siempre devuelve el valor 1
  else: #Si es cualquier otro valor , retorno la función recursiva
    return n * factorial_r(n-1) #Función recursiva

numFactorial = int(input("Introduce el factorial: "))
print(factorial_r(numFactorial))"""
"""
def imprimir(x):
  if x > 0:
    print(x)
    imprimir(x-1)

imprimir(5)

"""
print()


def imprimir2(x):
  if x > 0:
    imprimir2(x - 1)
    print(x)


imprimir2(5)