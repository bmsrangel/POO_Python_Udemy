'''
Quando utilizar?
1) Se necessário reutilizar uma feature em várias classes diferentes
2) Melhorar a modularidade

Mixin é uma forma controlada de adicionar funcionalidades às classes

Propriedades:
1) não deve ser extendida
2) não deve ser instanciada

Em Python, o conceito de mixins é implementado usando herança múltipla
'''


class Livro(object):
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo


class LivroHTMLMixin(object):
    def renderizar(self):
        return (f'<html><title>{self.nome}</title><body>{self.conteudo}</body></html>')


class LivroHTML(Livro, LivroHTMLMixin):
    pass


livro_html = LivroHTML('Algum livro', 'blablabla')
print(livro_html.renderizar())