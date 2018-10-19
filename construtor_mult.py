class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # Construtor alternativo
    @classmethod
    def outro_construtor(cls, nome):
        return cls(nome)

p = Pessoa('Bruno')
print(p.nome)

p2 = Pessoa.outro_construtor('Pedro')
print(p2.nome)