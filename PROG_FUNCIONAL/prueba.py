lista_valores = [108, 31, 75, 87, 79, 88, 89, 118, 51, 89, 174, 95, 51, 70, 73]
lista_valores.sort()

if len(lista_valores) % 2 != 0:
    mediana1 = int((len(lista_valores) / 2) + 0.5)
    mediana = lista_valores[int(mediana1) - 1]
else:
    mediana1 = int((len(lista_valores) / 2))
    mediana = (lista_valores[int(mediana1)] + lista_valores[int(mediana1) - 1]) / 2

for i in range(len(mediana1)):
    print(lista_valores[i])

#print(mediana)
#print(lista_valores)

# [31, 51, 51, 70, 73, 75, 79, 87, 88, 89, 89, 95, 108, 118, 174]