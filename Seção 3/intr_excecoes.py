class SomentePares(list):
    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError('Somente números inteiros podem ser adicionados')
        if inteiro % 2:
            raise ValueError('Somente números pares podem ser adicionados')

        super().append(inteiro)


lista = SomentePares()
lista.append(2.2)
print(lista)

'''BaseException
- SystemExit
- KeyboardInterrupt
- Exception

Outras exceções'''