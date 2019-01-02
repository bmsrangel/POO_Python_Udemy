import sqlite3


class BancoDeDados:
    """Classe que representa o Banco de Dados da aplicação"""
    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conectar(self):
        # Conecta passando o nome do arquivo
        self.conexao = sqlite3.connect(self.nome)

    def desconectar(self):
        try:
            self.conexao.close()
        except AttributeError:
            pass
