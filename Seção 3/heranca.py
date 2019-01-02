class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaFisica(Pessoa):

    def __init__(self, cpf, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf

p1 = Pessoa('Marcos', 28)
print(p1.nome)
print(p1.idade)
p_fisica = PessoaFisica('111111-11', 'Marcos', 28)
print(p_fisica.cpf)
print(p_fisica.nome)
print(p_fisica.idade)