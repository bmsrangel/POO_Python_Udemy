def tupla_par(tupla):
    lista = list()
    for c in range(0, len(tupla)):
        if c % 2 == 0:
            lista.append(tupla[c])
    return tuple(lista)

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8)
print(tupla_par(tupla))
