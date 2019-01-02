def numero_perfeito(num):
    soma = 0
    for c in range(1, num):
        if num % c == 0:
            soma += c
            print(c)
    return soma == num

num = int(input('Informe um número: '))
print(numero_perfeito(num))