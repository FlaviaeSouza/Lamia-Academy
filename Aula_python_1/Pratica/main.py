from functools import reduce
from salgados import recheio,Salgados

print("""Bem vindo a Lanchonete!
Qual será o pedido de hoje? :) \n""")

def Receber_recheio():
    Recheio = recheio()
    tipo_es = input('Qual o sabor de salgado desejado? digite o nome, restrito as opções abaixo! \n1 - Frango \n2 - Carne \n3 - Presunto e queijo \n \nResposta: ')

    if tipo_es != 'Carne' and tipo_es != 'Frango' and tipo_es != 'Presunto e Queijo':
        print('Infelizmente não possuimos esse sabor no momento! :(')
        return 0.1
    else:
            if tipo_es == 'Carne':
                return Recheio.carne()
            
            elif tipo_es == 'Frango':
                return Recheio.Frango()

            elif tipo_es == 'Presunto e Queijo':
                return Recheio.Presunto_queijo()



def Receber_quantidade():
    print('Tabela de preços(Acima de 10 unidades receba 20% de desconto)')# na mesma ordem que aparece o tipo an pergunta 1
    for salgado in Salgados:
                print(salgado['preco'])

    quant =  int(input('Quantos salgados voce gostaria? \n\n Resposta:'))

    if quant >= 10:
        desc = 0.20

    else:
        desc = 0.0

    return quant, desc


def Receber_tipo():
    print('Por favor escolha entre:\n ')
    for salgado in Salgados:
        print(salgado['nome'])
    tipo = input('\nResposta: ')
    return tipo

def Finalizar_pedido(preco_final,quantidade,tipo,sabor):
    print(f'Por favor confirme, O pedido consiste em um salgado de {tipo}, com recheio de {sabor}, de {quantidade} unidades e com preço final de {preco_final}')
    confirma = input('Confirma?(s/n): ')
    if confirma == 's':
        print('Seu pedido será preparado!')

    elif confirma == 'n':
        print('Por favor inicie o processo novamente :(')

i = 1
while i > 0:
    tipo = Receber_tipo()
    sabor = Receber_recheio()

    if  sabor == 0.1:
        print("faça um novo pedido!")
        break

    obter_preco = lambda Salgados:Salgados['preco']
    definir_se_igual = lambda Salgados: Salgados['nome'] == tipo
    acumulador = lambda total,preco: total + preco

    obter_preco_tipo = list(filter(definir_se_igual, Salgados))
    preco_1 = list(map(obter_preco, obter_preco_tipo))
    preco_parcial = reduce(acumulador,preco_1,0)

    quantidade, desc = Receber_quantidade()
    preco_final = ((preco_parcial * quantidade) * (1-desc))
    Finalizar_pedido(preco_final,quantidade,tipo,sabor)

    print('Deseja fazer mais um pedido?')
    a = input('Resposta:(s/n) ')
    if a == 's':
        pass
    
    elif a  == 'n':
        print('Volte Sempre!')
        break

    else:
        break
