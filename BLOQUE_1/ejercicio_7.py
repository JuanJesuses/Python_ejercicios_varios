""" ¿Qué imprime el siguiente código? """
def f():
    print('f start')
    g()
    h()
    print('f end')

def g():
    print('g start')
    h()
    print('g end')

def h():
    print('h')

f()