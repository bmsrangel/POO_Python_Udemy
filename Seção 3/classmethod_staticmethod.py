class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_string(cls, data_string): # Formato da data: 10-10-2016
        # print(cls) Mostra que cls referencia a classe Data
        dia, mes, ano = map(int, data_string.split('-'))
        data = cls(dia, mes, ano)
        return data

    @staticmethod
    def is_date_valid(data_string):
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2100


data = Data(10, 10, 2016)
data1 = Data.de_string('10-10-2016')
print(data1)
print(data1.is_date_valid('10-10-2016'))