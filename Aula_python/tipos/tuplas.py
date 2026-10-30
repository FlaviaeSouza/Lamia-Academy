nomes = ('Ana', 'Bia', 'Gui', 'Leo', 'Ana') #cria uma tupla com nomes nela

print('Bia' in nomes) #imprime se é false ou true que bia esta como um elemento da tupla, e nesse caso tem que ser exatemente como escrito na tupla, esse exemplo serve para listas tbm

print(nomes[0])#primeiro elemento
print(nomes[1:3])#primeiro elemento até o terceiro sem incluir o terceiro
print(nomes[1:-1])
print(nomes[2:])#do segundo ate o final sem incluir o segundo
print(nomes[:-2])#todos ate o penultimo sem incluir o penultimo

#vale resltar que, não foi incluido nessa parte do codigo mas no video mostra que mesmo se for apenas uma string como por exemplo 
#y = ('Bia', ), mesmo que n tenha mais nenhum elemento e pareça uma string o codigo considera como tupla por conta da virgula

print(type(nomes)) #mostra o tipo (que nesse caso seria uma tupla)
print(nomes) #imprime a tupla