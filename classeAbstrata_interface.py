'''from abc import ABCMeta, abstractmethod

class MinhaClasseAbstrata(metaclass=ABCMeta):
    @abstractmethod
    def fazer_algo(self):
        pass

    @abstractmethod
    def fazer_algo_novamente(self, o_que_fazer):
        pass


obj = MinhaClasseAbstrata()
'''
# from abc import ABCMeta, abstractmethod
#
# class Animal(metaclass=ABCMeta):
#     @abstractmethod
#     def dizer_algo(self):
#         pass
#
#
# class Cachorro(Animal):
#     def dizer_algo(self):
#         return 'AU AU'
#
#
# c = Cachorro()
# print(c.dizer_algo())

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def dizer_algo(self):
        return 'Eu sou um animal'


class Cachorro(Animal):
    def dizer_algo(self):
        s = super(Cachorro, self).dizer_algo()
        return f'{s} - AU AU'


c = Cachorro()
print(c.dizer_algo())

#Usar classes abstratas com cuidado em Python