#! python3
#construtor
class Produto: # classe é como se fosse um planta ou molde, donde apartir dela consegue se contruir varias casas ou objetos
    def __init__(self, nome, preco = 1.99, desc = 0):#intancia um  novo objeto
        self.nome = nome # faz nome ser um atributo dentro do objeto
        self.__preco = preco
        self.desc = desc

    @property
    def preco(self): # getter para ler
        return self.__preco

    @preco.setter # vai permitir alterar o valor do preço a partir desse setter, setter para alterar
    def preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco

    @property # decorator, permite que a função preco__final seja vista pelo codigo como uma variavel e n como metodo
    def preco_final(self):
        return (1-self.desc) * self.preco

p1 = Produto('Caneta', 5.99, 0.1)#objetos gerados apartir da classe
p2 = Produto('Caderno', 14, 0.5)

p1.preco = 10

print(p1.nome, p1.preco, p1.desc, p1.preco_final)
print(p2.nome, p2.preco, p2.desc, p2.preco_final)

#__ antes de um atributo significa que aquele atributo é privado