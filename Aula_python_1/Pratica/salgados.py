#! python 3

class recheio:
    def __init__(self):
            self.__recheio = ''

    @property
    def recheio(self):
        return self.__recheio
    
    def carne(self):
        self.__recheio  = 'Carne'
        return self.__recheio

    def Presunto_queijo(self):
        self.__recheio  = 'Presunto e Queijo'
        return self.__recheio

    def Frango(self):
            self.__recheio = 'Frango'
            return self.__recheio


Salgados = [
    {'nome': 'Coxinha', 'preco': 9.5},
    {'nome': 'Pastel', 'preco': 12.0},
    {'nome': 'Enroladinho', 'preco': 7.0},
    {'nome': 'Bauru', 'preco': 7.0},
]