from functools import reduce

alunos = {

    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}

}


aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# lambdas são funções anonimas (funções que não precisam de def e de uma unica linha)





print(alunos)