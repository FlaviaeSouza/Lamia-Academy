#! python 3

class recheio:#define uma classe chamada de recheio
    def __init__(self): #inicializa a instancia de recheio
            self.__recheio = '' #inicializa como uma string vazia

    @property #permite que a função se torne uma propriedade
    def recheio(self):
        return self.__recheio
    
    def carne(self):
        self.__recheio  = 'Carne'#define o atributo recheio como carne
        return self.__recheio#retorna o valor armazenado em recheio da instancia da classe

    def Presunto_queijo(self):
        self.__recheio  = 'Presunto e Queijo'#define o atributo recheio como Prseunto e Queijo
        return self.__recheio

    def Frango(self):
            self.__recheio = 'Frango'#define o atributo recheio como Frango
            
            return self.__recheio


Salgados = [#cria um dicionário com as informações de nome de salgados com as keys de nome e preço
     #cria os nomes e preços de cada salgado
    {'nome': 'Coxinha', 'preco': 9.5},
    {'nome': 'Pastel', 'preco': 12.0},
    {'nome': 'Enroladinho', 'preco': 7.0},
    {'nome': 'Bauru', 'preco': 7.0},
]