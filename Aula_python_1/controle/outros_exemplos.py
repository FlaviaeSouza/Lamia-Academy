

pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas: # se p in pessoas siga para o laço de repetição
    for a in adjs: #se a in adjs siga para o laço de repetição
        print(f'{p} é {a}!')
print (' ')

for i in [1,2,3]:
    pass #permite que o codigo continue
print (' ')

for i in range(1,11):
    if i % 2 == 1:
        continue #sempre quando for impar ele vai continuar e se n for ele imprime i (sai da repetição e vai para a proxima)
    print(i)
print (' ')

for i in range(1, 11):
    if i == 5:
        break # sai do laço
    print(i)
print (' ')

print('Fim!')

#Quanto mais explicito fica o codigo melhor é para a interpretação dele