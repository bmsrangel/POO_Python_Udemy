'''
Decorator - Função que recebe outra função como parâmetro, gera uma nova função
que adiciona algumas funcionalidades à função original e retorna essa nova função
'''


def modificar(funcao):
    def somar_pares(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a+b
        return a-b
    return somar_pares


@modificar
def somar(a, b):
    return a+b


print(somar(11, 4))
