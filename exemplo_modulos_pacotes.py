# import poligono
# from poligono import Quadrado
# from poligono import Retangulo
# Pacotes = coleção de módulos; __init.py__ são necessários para que o Python trate os diretórios como pacotes
import modulos.poligono
# from modulos.poligono import Quadrado, Retangulo

q = modulos.poligono.Quadrado(5)
print(q.perimetro())
print(q.area())

r = modulos.poligono.Retangulo(5, 10)
print(r.area())
