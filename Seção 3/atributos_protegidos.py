class P:
    def __init__(self, x):
        self.__x = x


obj = P(10)
print(obj.__x)

'''O uso de 1 underscore indica que certo atributo ou método é privado, mas fica como um "acordo de cavalheiros".
Para que o interpretador de fato trate o atributo/método como privado, é necessário utilizar 2 underscores'''