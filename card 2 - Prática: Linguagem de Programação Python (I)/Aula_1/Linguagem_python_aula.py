#! python3
#aula_1_python 
# (#! é utilizado para especificar o interpretador utilizado)

# print('Bem vindo') print é utilizado para exibir informações no terminal
# import Pacotes.Sub.Arquivo_teste #O import é utilizado para que seja possivel importar (outros codigos)

"""
vale resaltar que os conjunto de aspas ultizados aqui apra fazer um comentário, são tambem utilizados
para strings de multiplas linhas.
"""
#from tipos import variaveis, basicos

"""ou from tipos import variaveis, esse 'comando' é mais utilizado quando deseja-se 
importar mais de uma parte do que sera importado;
EX: from tipos import variaveis, numeros"""

#exercicios de tipos:
#import tipos.lista_aula
#import tipos.tuplas_aula
#import tipos.conjuntos_aula
#import tipos.dicionario_aula

#exercicios de operadores:
#import operadores.unarios_aula
#import operadores.aritmeticos_aula
#import operadores.relacionais_aula
#import operadores.atribuição_aula
#import operadores.logicos_aula
#import operadores.ternario_aula

#exercicios de controle:
#import controle.if_1_aula
#import controle.if_2_aula
#import controle.for_1_aula
#import controle.while_1_aula
#import controle.outros_exemplos_aula

#exercicios de funções

#from funcoes import basico_aula
#para acessar a função precisamos usar o name space ligado a esse modulo,
#ou seja não podemos usar apenas saudação(), pois não vai funcionar precisamos relacionar  a basico
#basico.saudacao()
# basico.saudacao('Lurdes')
# basico.saudacao('Adelaide', 89)
# basico.saudacao(idade = 87)
# o fato do python n ter sobrecarga
#(quando voce usa o mesmo nome para diversas funcoes e varios metodos contudo com parametros diferentes)
#permite que voce tenha duas funções de nomes iguais que façam coisas diferentes
# a = basico.soma_e_multi(x=10, a=2, b=3)
# print(a)
#preferivel que uma função retorne algo e depois seja impressa caso necessário, e que n tenha apenas o print dentro de sua função
#isso acontece por que se usarmos return podemos chamar a função mais de uma vez e atribuir valores diferentes e com isso printar
#somente caso necessário, ja que em aplicações normais não se costuma usar o print no terminal(costuma ser apenas para debug e etc)

# from funcoes import args_aula
# ambos os exemplos abaixo são de packs o primeiro sendo de tupla e o segundo de dicionário
# s = args.soma(1,2,3,4,5,6,7,8,9,10)
# print(s)
# resultado = args.resultado_final(nome='Pedro', nota=7.3)
# print(resultado)

#from funcoes import funcional_aula
#import funcoes.map_reduce_aula
#import funcoes.lambdas_aula
#import funcoes.comprehension_aula


#exercicios de oo
#import oo.produto_aula
#import oo.heranca_aula
#import oo.membros_aula