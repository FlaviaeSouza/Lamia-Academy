#! python 3 

class Contador:
    contador = 0 #atributo de classe

    @classmethod #metodo de classe
    def inc(cls):
        cls.contador += 1 #aumenta em um o contador
        return cls.contador
    

    @classmethod #metodo de classe
    def dec (cls):
        cls.contador -= 1 #diminui em 1 o contador
        return cls.contador

    @staticmethod #metodo estatico
    def mais_um(n):
        return n+1


#quando tenho metodo de classe n precisa criar a instancia
# a mesma coisa n pode ser feita com inst pois nesse caso ele precisa de uma instancia


print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())
print(Contador.mais_um(7))

#a partir da instancia de uma classe é possivel acessar a classe, ou seja para ter instancia precisa ter classe

#cuidado se a partir de um metodo de instancia vc tentar ler um valor vai conseguir ler, contudo ele pega o valor da classe 
#(caso n tenha, que é o caso desse codigo), que é zero no nosso caso, e incrementaria errado. Os atributos de instancia são unicos a cada instancia, já os de classe se compartilham entre classes  
