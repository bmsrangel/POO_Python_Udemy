from database import BancoDeDados

if __name__ == '__main__':
    banco = BancoDeDados()
    banco.conectar()
    banco.criar_tabelas()
    # banco.inserir_cliente('Marcos', 'python', '11111111111', 'mcastrosouze@live.com')
    banco.inserir_cliente('Tomas', 'javascript', '22222222222', 'tomas@gmail.com')
    # banco.buscar_cliente('11111111111')
    # banco.remover_cliente('22222222222')
    # banco.buscar_cliente('22222222222')
    # banco.buscar_nome_email('mcastrosouze@live.com')
    print(banco.login('Marcos', 'python'))
    banco.desconectar()

'''
SQLite Browser: visualizador gráfico dos arquivos DB
https://sqlitebrowser.org/
'''
