class MinhaLista(list):
    def append(self, *args):
        self.extend(args)


l = MinhaLista()
l.append(1)
print(l)
l.append(2, 3, 4, 5, 6, 7)
print(l)


class MyList(list):
    def sort(self):
        return 'opa, você quer ordenar?'


lista = [10, 5, 20]
lista.sort()
print(lista)
lista = MyList()
print(lista.sort())