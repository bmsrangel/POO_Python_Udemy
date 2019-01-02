from abc import ABCMeta
from abc import abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):
        print('auauau')


class Gato(Animal):
    def falar(self):
        print('miaumiau')


class Fabrica(object):
    def produzirSom(self, object_type):
        return eval(object_type)().falar()


if __name__ == '__main__':
    f = Fabrica()
    f.produzirSom('Cachorro')
