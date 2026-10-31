from functools import reduce

def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc
#o caso acima  é para poder somar qualquer valor e n necesáriamente apenas um e meio, mas sim 2 , 2 e meio e por assim vai

notas = [6.4, 7.2, 5.8, 8.4]

nota_final = list(map(somar_nota(1.5), notas))
nota_final_2 = list(map(somar_nota(1.8), notas))

"""
O codigo acima se diferencia do do video pois, ao executar ao inves de receber o resultado das notas que era 
esparado foi recebido o resultado no terminal <map object at 0x7a24afd343a0>, com isso fui ver nos comentários e isso se dá 
devido a mudança de python 2 para python 3 , com isso tive que transforma-lo em uma lista para obter o resultado correto.
"""

print(nota_final)
print(nota_final_2)

def somar(a, b):
    return a + b

total = reduce(somar , notas, 0) #reduz a sequencia inteira par apenas 1 valor
print(total)

# def mais_um_meio(nota):
#     return nota + 1.5
# for i,  nota in enumerate(notas):
#     notas[i] = nota + 1.5

#for i in range(len(notas)):
#   notas[i] = notas[i] + 1.5

#ambos os casos acima somam 1.5 as notas apresentadas anteriormente , contudo foram usadas apenas de exemplo


