class Pato:
    def quack(self):
        print('Quack, quack')


class Pessoa:
    def quack(self):
        print('Eu faço quack igual a um pato')

'''
Isso não é pythônico
def fazer_quack(obj):
    if isinstance(obj, Pato):
        obj.quack()
    else:
        print('Isso tem que ser um pato')

def fazer_quack(obj):
    # LYBL - Não pythonico -> testes de pré-condições antes de fazer chamadas
    if hasattr(obj, 'quack'):
        if callable(obj.quack):
            obj.quack()
'''

def fazer_quack(obj):
    # EAFP - Easier to ask for forgiveness than permission
    try:
        obj.quack()
    except AttributeError as e:
        print(e)

pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)