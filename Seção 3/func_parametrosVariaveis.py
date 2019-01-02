# def funcao(*args):
#     print(args)
#
#
# funcao(1, 2, 3, 'Bruno')

def funcao(**kwargs):
    for k, v in kwargs.items():
        print(f'{k.capitalize()}: {v}')


funcao(nome='Bruno', idade=28, linguagem='Python')