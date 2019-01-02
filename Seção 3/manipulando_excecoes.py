# def algo():
#     print('Antes da exceção')
#     # raise Exception('exceção')
#     print('Depois da exceção')
#
# def algo2():
#     try:
#         algo()
#     except:
#         print('Eu peguei uma exceção')
#
#     print('Executado após a exceção e ainda dentro de algo 2')
#
# algo2()


def divisao(divisor):
    try:
        if divisor == 13:
            raise ValueError('13 não é um número legal')
        return 10 / divisor
    except ZeroDivisionError:
        return 'Entre com um número diferente de zero'
    except TypeError:
        return 'Entre com um valor numérico'
    except ValueError:
        print('Não utilize o número 13')
        # raise
    finally:
        print('Isso sempre será executado')


print(divisao(13))


# try:
#     raise ValueError('Argumento')
# except ValueError as e:
#     print(f'Os argumentos da exceção foram {e.args}')
# finally:
#     print('Isso sempre será executado')