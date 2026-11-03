from functools import reduce

alunos = [

    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 9.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}

]


aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# lambdas são funções anonimas (funções que não precisam de def e de uma unica linha)
# aluno_honra = lambda aluno: aluno['nota'] >= 9


obter_nota = lambda aluno:aluno['nota']
somar = lambda  a,b: a+b


alunos_aprovados = list(filter(aluno_aprovado, alunos)) # pega todos os alunos da lista e aplica um filtro, onde apenas os alunos que foram 
#aprovados vão ser presentes no array final ou seja o alunos_aprovados.
# alunos_honras = list(filter(aluno_honra, alunos))
#o list foi usado pelo mesmo motivo do list em map.

#lista de  dicionários em uma lista de float com map


notas_aprovados = list(map(obter_nota, alunos_aprovados))
total= reduce (somar, notas_aprovados, 0)

print(notas_aprovados)
print(total / len(notas_aprovados))