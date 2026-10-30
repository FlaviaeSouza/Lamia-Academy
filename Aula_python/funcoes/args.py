def soma(*nums):
    total = 0
    for n in nums:
        total  += n
    return total

# A função acima faz a soma de todos os numeros em uma tupla

def resultado_final(**Kwargs):
#**kwargs coleta número variável de argumentos nomeados (palavraas chave) em um dicionario
    status = 'aprovado(a)' if Kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{Kwargs["nome"]} foi {status}' 
    