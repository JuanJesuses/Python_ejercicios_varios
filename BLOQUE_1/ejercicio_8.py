""" ¿Qué imprime el siguiente código? """

def g(x):
    print("G1",x)
    x = x + 1
    print("G2",x)
    return x

def f(x):
    print("F1",x)
    x = g(x)
    print("F2",x)

x = 1
print("A1",x)
f(x)
print("A2",x)