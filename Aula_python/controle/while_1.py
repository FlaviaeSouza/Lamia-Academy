total = 10
qtde = 0
nota = 0

while nota != -1: #enquanto x for True execute o  bloco, quando for False saia do bloco
    nota = float(input('informe a nota ou -1 para sair: '))#recebe a nota dos alunos
    if nota != -1:# se n for -1 executa:
        qtde += 1 #aumenta 1 a qtd a cada loop
        total += nota #adiciona a nota atual a somatória de notas

print(f'Á média da turma é {total / qtde}')


"""
O while pode ser usado de uma forma determinada
ex:

x = 10

while x:
    ...

é possivel contudo o while sempre vai precisar de uma forma de sair desse laço de repetição ou seja, precisamos de algo 
que nesse caso diminua o valor de x ficando assim:
x = 10

while x:
    x -= 1


"""