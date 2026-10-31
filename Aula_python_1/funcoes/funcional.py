 
def soma(a, b):
    return a + b

def sub(a, b):
    return a - b


#armazenar a função dentro de uma variavel
somar = soma
print(somar(3,4))

def op_art(fn, op1, op2):
    #passa a função que vai operar em cima dos dois valores (op1 e op2)
    return fn(op1, op2)

#mostrando como a função funciona com as funções sub e soma como parametro
result = op_art(soma , 13, 48)
print(result)

result_sub = op_art(sub , 13, 48)
print(result_sub)


def soma_parcial(a):
    def concluir_soma(b):
        return a+b
    return concluir_soma

# Na função acima foi declarada uma função dentro de outra, e a segunda função vai ser retornada de modo a quando a primeira
#função for chamada, o resultado dela n vai ser a+b mas sim o resultado de uma função

f = soma_parcial(10)
resultado_1 =  f(5)
print(resultado_1)

# ou resultado_1 = soma_parcial(10)(12)
#print(resultado_1)
#outra forma de obter o mesmo resultado

#isso serve para voce tornar a execução final tardia, caso n tenha o parametro b, ou tenha um processamento
#pesado anteriormente, já que permite guardar o resultado de parte do processamento permitindo assim que o código
#se torne mais eficiente, no video ele da um exemplo colocando uma parte esperado do tempo e usa disso para exemplificar isso,
#não coloquei no código pois achei que em algum momento caso precisa-se revisar ficar mais confuso e explicar por comentários
#se tornaria mais simples.

