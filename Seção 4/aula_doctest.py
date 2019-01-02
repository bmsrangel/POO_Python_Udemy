import doctest


class Fib:
    def calculo_fib(self, n):
        """
        Método para calcular o Fibonacci
        >>> f.calculo_fib(10)
        55
        >>> f.calculo_fib(1)
        1
        >>> f.calculo_fib(-1)
        Traceback (most recent call last):
        ...
        ValueError: O número informado deve ser maior que zero.
        """
        if n < 0:
            raise ValueError("O número informado deve ser maior que zero.")
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    doctest.testmod(extraglobs={'f': Fib()})
