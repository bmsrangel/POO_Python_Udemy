class TransacaoInvalida(Exception):
    def __init__(self, saldoAtual, quantidade):
        super().__init__(f'Sua conta não tem R${quantidade}')
        self.quantidade = quantidade
        self.saldoAtual = saldoAtual

    def excesso(self):
        return self.quantidade - self.saldoAtual

try:
    raise TransacaoInvalida(10, 20)
except TransacaoInvalida as e:
    print(f'Você não tem saldo suficiente! Faltam R${e.excesso():.2f}')
# raise TransacaoInvalida('Você não tem dinheiro')

# Exception.__init__ args