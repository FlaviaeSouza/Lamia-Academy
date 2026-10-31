#! python3

class carro:
    def __init__(self):
        self.__velocidade = 0

    @property #define getter
    def velocidade(self):
        return self.__velocidade

    def acelerar(self): # define uma função para acelerar
        self.__velocidade += 5
        return self.__velocidade

    def frear(self):# define uma função para frear
        self.__velocidade -= 5
        return self.__velocidade 

class kwid(carro): # carro é a classe pai
    pass

class ferrari(carro): #pega a herança de carro contudo sobrescreve o acelerar.
    def acelerar(self):
        super().acelerar()
        return super().acelerar()
    


c1 = ferrari() # qual carro vai ser chamado
print(c1.acelerar())
print(c1.acelerar())
print(c1.acelerar())
print(c1.frear())
print(c1.frear())
print(c1.frear())