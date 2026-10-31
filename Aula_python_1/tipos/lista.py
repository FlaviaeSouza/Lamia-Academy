nums = [1,2,3] #cria u a lista a guarda os valore 1, 2 e 3 em ordem
print(type(nums)) #imprime o tipo de nums

nums.append(3) # append coloca mais um numero a lista
nums.append(4)
nums.append(500)

print(len(nums))
nums[3] = 100 #define a quarta casa da lista com o numero 100 dentro
nums.insert(0, -200)# coloca um novo numero a lista e diz tambem a posição dele na lista
print(nums[-1])#pega o ultimo elemento, contudo apenas colocar o numero de elementos-1 já da certo tbm (se tenho 7 em uma lista para pegar o ultimo basta colocar 6)
print(nums[-2])#pega o penultimo elemento.
print(nums) #imprime a lista    

