from database import BancoDeDados

if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conectar()
    banco.desconectar()
