sing = '...sheep'
plur = '...sheeps'
nada = ''

ovejas = int(input('¿Cuántas ovejas quieres contar?: '))

for i in range(ovejas):
    for x in range(i):
        if x == 0:
            print(nada)
        elif x == 1:
            print(x, sing, end="")
        else:
            print(x, plur, end="")

