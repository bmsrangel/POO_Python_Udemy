class Funcionario:

    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf
        # self.__x = x  __ antes do atributo indica "privado"/ atributos protegidos não são herdados pelas subclasses

    def get_bonificacao(self):
        return self.salario * 0.20


class Gerente(Funcionario):

    def __init__(self, nome, salario, cpf, senha):
        super().__init__(nome, salario, cpf)
        self.senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000.00

g = Gerente('Thomas', 3000.00, '233321234', 3333)
print(g.nome)
print(g.get_bonificacao())
print(g.senha)