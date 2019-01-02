class Ponto:

    def __init__(self, x = 0, y = 0): # o x = 0 e y = 0 -> indica q os argumentos são opcionais; parâmetros necessários
        # vêm antes dos opcionais
        self.x, self.y = x, y

    def resetar(self):
        self.x, self.y = 0, 0

    def mover(self, x, y):
        self.x, self.y = x, y


p = Ponto()
p.resetar()
print(f'({p.x},{p.y})')
p.mover(10, 20)
print(f'({p.x},{p.y})')
