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

    def criar_tabelas(self):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    senha VARCHAR(20) NOT NULL,
                    cpf VARCHAR(11) UNIQUE NOT NULL,
                    email TEXT NOT NULL
                );
            """)
        except AttributeError:
            print('Faça a conexão com o banco antes de criar as tabelas')

    def inserir_cliente(self, nome, senha, cpf, email):
        try:
            cursor = self.conexao.cursor()
            try:
                cursor.execute("""
                    INSERT INTO clientes (nome, senha, cpf, email) VALUES (?, ?, ?, ?)
                """, (nome, senha, cpf, email))
                self.conexao.commit()
            except sqlite3.IntegrityError:
                print(f'O CPF {cpf} já existe')
        except AttributeError:
            print('Faça a conexão com o banco antes de inserir clientes')

    def buscar_cliente(self, cpf):
        try:
            cursor = self.conexao.cursor()

            # obtendo todos os dados
            cursor.execute(f"""
                SELECT * FROM clientes WHERE cpf={cpf};
            """)
            cliente = cursor.fetchone()
            if cliente:
                print(f'Cliente {cliente[1]} encontrado')
            else:
                print('Cliente não encontrado!')
        except AttributeError:
            print('Faça a conexão com o banco antes de buscar clientes')

    def remover_cliente(self, cpf):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"""
                DELETE FROM clientes WHERE cpf={cpf};
            """)
            self.conexao.commit()
        except AttributeError:
            print('Faça a conexão com o banco antes de remover clientes')

    def buscar_email_cpf(self, cpf):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(f"""
                SELECT nome, email FROM clientes WHERE cpf={cpf};
            """)
            cliente = cursor.fetchone()
            if cliente:
                print(f'O e-mail do cliente {cliente[0]} é {cliente[1]}')
            else:
                print('Cliente não encontrado')
        except AttributeError:
            print('Faça a conexão com o banco antes de buscar clientes')

    def buscar_nome_email(self, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT nome FROM clientes WHERE email="{}";
            """.format(email))
            cliente = cursor.fetchone()
            if cliente:
                print(f'O nome do cliente que possui o e-mail {email} é {cliente[0]}')
            else:
                print('Cliente não encontrado')
        except AttributeError:
            print('Faça a conexão com o banco antes de buscar clientes')

    def login(self, username, senha):
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM clientes WHERE nome=? AND senha=?'
            cliente = cursor.execute(sql, [username, senha]).fetchone()
            if cliente:
                return True
            return False
        except AttributeError:
            print('Faça a conexão com o banco')
