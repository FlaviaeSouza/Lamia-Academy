
"""for i in range(10):
    print(i)
 


for i in range(1, 11):
    print(i)

#em ambos os casos acima se forma um laço de repetição onde ele printa i até que chegue no valor final ou seja
no primeiro caso de 0 a 10 e no segundo de 1 a 11



for i in range(1, 100, 7): # ele conta de 1 a 100 so que de 7 em 7
    print(i)
print(' ')

for i in range(20, 0, -2): # podendo contar de trás para frente tbm
    print(i)
print(' ')


nums = [2, 4, 6, 8]

for n in nums:
    print(n, end = ',')

#o codigo acima mostra o for para imprimir uma lista

texto = 'Python é muito massa'
for letra in texto:
    print(letra, end = ' ')

#o codigo acima mostra for para imprimir uma string com as letras seapradas
    
for n in {1,2,3,4,4,4}:
    print(n, end = ' ')

#o codigo acima mostra o for para imprimir um conjunto
"""


produto = {
    'nome' : 'caneta',
    'preco' : 8.80,
    'desc' : 0.5
}


"""
for ch in produto:
    print(atrib, produto[atrib])

"""

for atrib, valor in produto.items():
    print(atrib, '=>', valor)

# 2 formas diferentes de mostrar o mesmo resultado

for valor in produto.values():
    print(valor, end=' ')
#percorre somente os valores

for atrib in produto.keys():
    print(atrib, end=' ')
#percorre somente as chaves



