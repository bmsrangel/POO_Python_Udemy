# import pickle
#
# meus_dados = ['Bruno', 3.14, [1, 2, 3]]
#
# with open('arquivo.txt', 'wb') as file:
#     pickle.dump(meus_dados, file)
#
# with open('arquivo.txt', 'rb') as file:
#     dados_carregados = pickle.load(file)
#
#
# print(dados_carregados)

# Serializando objetos: JSON - Java Script Object Notation

import json

class Contato:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return (f'{self.primeiro_nome} {sobrenome}')


c = Contato('Bruno', 'Rangel')
print(json.dumps(c.__dict__))
