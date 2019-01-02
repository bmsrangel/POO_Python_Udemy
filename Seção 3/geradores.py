# def fib(max):
#     x, y = 1, 1
#     while x < max:
#         yield x
#         x, y = y, x + y
#
#
# gen = fib(10)
# for i in gen:
#     print(i, end=' ')


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


lista_primos = get_primes(1)
for i in range(0, 20):
    print(next(lista_primos), end=' ')