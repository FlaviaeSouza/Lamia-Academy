from functools import reduce
from salgados_pratica import recheio,Salgados

print("""Bem vindo a Lanchonete!
Qual será o pedido de hoje? :) \n""")

def Receber_recheio():
    Recheio = recheio() # criando o objeto da classe recheio
    tipo_es = input('Qual o sabor de salgado desejado? digite o nome, restrito as opções abaixo! \n1 - Frango \n2 - Carne \n3 - Presunto e queijo \n \nResposta: ')

    if tipo_es != 'Carne' and tipo_es != 'Frango' and tipo_es != 'Presunto e Queijo':#se o tipo não for um dos possiveis faça:
        print('Infelizmente não possuimos esse sabor no momento! :(')#imprime uma mensagem na tela
        return 0.1 #esse return foi adicionado para durante o while ser possivel finalizar o codigo caso não seja um sabor possivel
    
    else: # se a opção selecionada for valida, relaciona ela com a class criada no salgados.py
            if tipo_es == 'Carne':
                return Recheio.carne()
            
            elif tipo_es == 'Frango':
                return Recheio.Frango()

            elif tipo_es == 'Presunto e Queijo':
                return Recheio.Presunto_queijo()



def Receber_quantidade():
    print('Tabela de preços(Acima de 10 unidades receba 20% de desconto)')# na mesma ordem que aparece o tipo an pergunta 1
    for salgado in Salgados: # utilizamos do dicionário presente em salgados.py para exibir os precos de cada um
                print(salgado['preco']) 

    quant =  int(input('Quantos salgados voce gostaria? \n\n Resposta:'))#recebe a quanitdade de salgados

    if quant >= 10:#se quantidade recebida é maior que 10 aplica desconto
        desc = 0.20

    else:#se não for faça:
        desc = 0.0

    return quant, desc #retorna dois valores para que sejam armazenados individualmente em uma variavel


def Receber_tipo():
    print('Por favor escolha entre:\n ')
    for salgado in Salgados:# percorre o dicionario para apresentar os nomes dos salgados possiveis
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

i = 1 # inicia a variavel de controle do while
while i > 0: #loop que basicamente não acaba, como no bloco não tem nada que decremente um, isso acontece justamente para que seja possivel permitir o cliente fazer o pedido quantas vezes queira
    tipo = Receber_tipo() 
    sabor = Receber_recheio()

    if  sabor == 0.1:
        print("faça um novo pedido!")
        break

    #essa proxima parte poderia ter sido feita mais facilmente utilizando for in , depois um if onde a gente pegaria o preço se o salgado selecionado fosse do mesmo tipo , contudo queria utilizar os lambdas, filter e map para testar
    obter_preco = lambda Salgados:Salgados['preco'] # pega toda a parte do dicionário chamada preço
    definir_se_igual = lambda Salgados: Salgados['nome'] == tipo #pega o dicionario de salgados passa por cada item desse dicionário, e compara com o tipo recebido pela pergunta
    acumulador = lambda total,preco: total + preco #faz um acumulador para que seja possivel somar o total de salgados

    obter_preco_tipo = list(filter(definir_se_igual, Salgados))#filtra os elementos de Salgados aplicando a função lambda definir_se_igual mantendo o que resulta em True
    preco_1 = list(map(obter_preco, obter_preco_tipo))#O map aplica a a função obter_preco a todos os itens filtrados acima retornando o preco de cada um
    preco_parcial = reduce(acumulador,preco_1,0)#o reduce aplica o acumulador, somando todos os valores e retornando total

    quantidade, desc = Receber_quantidade() #como a função devolve dois valores, conseguimos fazer com que duas variaveis recebam seus valores de forma respectivamente na ordem
    preco_final = ((preco_parcial * quantidade) * (1-desc))#calcula o preço dps de pegar o preco do dicionario multiplica pela quantidade e aplica desconto se tiver
    Finalizar_pedido(preco_final,quantidade,tipo,sabor)#chama a função feita antes para finalizar o pedido, utilizando dos valores recebidos das outras funções e preco_final

    print('Deseja fazer mais um pedido?') 
    a = input('Resposta:(s/n) ') # recebe a confirmação
    if a == 's':# se desejar fazer mais um pedido, ou seja se a == s for verdadeiro, retorna ao while
        pass #mantem a execução desse laço de repetição(while),retornando ao inicio para um novo pedido
    
    elif a  == 'n':# se for igual a n ou seja verdadeiro, imprime volte sempre e finaliza o codigo, e se for qualquer outra entrada tambem (contudo não apresenta o volte sempre)
        print('Volte Sempre!')
        break #finaliza o codigo

    else:
        break #finaliza o codigo


#Teria como fazer esse codigo de uma maneira mais simples e até mesmo um pouco mais eficiente, contudo foi feito dessa forma com o intuito de usar alguns dos principais pontos vistos em aula