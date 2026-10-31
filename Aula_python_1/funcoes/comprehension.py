#! python 3
from functools import reduce

alunos = [

    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 9.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}

]


obter_nota = lambda aluno: aluno['nota']
somar = lambda  a, b: a + b


alunos_aprovados = [aluno for aluno in alunos if aluno ['nota'] >= 7]#gera uma lista com o nome dos alunos e notas separadamente
notas_aprovados = [aluno['nota'] for aluno in alunos_aprovados] # deixa da mesma forma que o anterior contudo feito de forma diferente
total= reduce (somar, notas_aprovados, 0)

#print(alunos_aprovados)
print(notas_aprovados)
print(total / len(notas_aprovados))

# de modo geral esse codigo segue a mesma linha apresentada no lambdas.py, por isso não tem tantos comentários,
# comentei apenas oq entendi que mudou entre ambos