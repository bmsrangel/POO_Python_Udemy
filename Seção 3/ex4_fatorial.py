def meu_decorator(fat):
    def fat(x):
        if x > 0:
            return x * fat(x-1)
        else:
            return 1
    return fat


@meu_decorator
def dobro(x):
    return 2 * x


print(dobro(6))
