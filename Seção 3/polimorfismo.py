import math
class Forma():
    def __init__(self):
        print('Construtor da forma')

    def area(self):
        print('Área da forma')

    def perimetro(self):
        print('Perímetro da forma')

    def descricao(self):
        print('Descrição da forma')


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.raio

    def descricao(self):
        print('Descrição do círculo')

# quad = Quadrado(2)
# print(f'Área: {quad.area()}')
# print(f'Perímetro: {quad.perimetro()}')

circulo = Circulo(3)
print(f'Área: {circulo.area():.2f}')
print(f'Perímetro: {circulo.perimetro():.2f}')
circulo.descricao()