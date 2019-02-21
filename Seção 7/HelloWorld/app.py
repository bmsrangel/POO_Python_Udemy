# from bottle import route
# from bottle import run
# from bottle import request
from bottle import Bottle
from bottle import *

'''
@route('/') # Diz que a aplicação deve interpretar determinado caminho; liga parte do código a um caminho
@route('/user/<nome>')
# @route('/hello') # Diz que a aplicação deve interpretar determinado caminho; liga parte do código a um caminho
def index(nome='Desconhecido'):
    return '<center><h1>Olá, ' + nome.title() + '!</h1></center>'


# @route('/python')
# def python():
#     return '<h1>Curso de Python</h1>'

@route('/artigo/<id>')
def artigo(id):
    return '<h1>Você está lendo o artigo ' + id + '</h1>'


@route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return '<h1>Você está vendo a página ' + id + ' com o nome ' + nome + '</h1>'

'''


@route('/login') # @get('/login')
def login():
    return '''
        <form action="/login" method="post">
            username: <input name="username" type="text" />
            password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''


def check_login(username, password):
    return True


@route('/login', method='POST') # @post('/login')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return '<center><h1>Login realizado com sucesso!</h1></center>'
    else:
        return '<center><h1>Falha ao realizar o login!</h1></center>'


if __name__ == '__main__':
    run(host='localhost', port=8080)
