a = 3 #define uma variavel int chamada a com valor 3
b = 4.4 #define uma variavel float chamada b com valor 4.4

print(a+b)#imprime a soma de ambos os valores das variaveis

texto = 'Sua idade é... '
idade = 19

print(f'{texto} {idade}')
"""antes de ser impressa a variavel int precisa ser convertida em string já que ira ser juntada ao texto.
print(texto + str(idade)) podendo ser feita dessa maneira, contudo a maneira presente no codigo acima se mostra mais facil.
O metodo usado acima é a interpolação dos valores. """

saudacao = " bomdia "
print(5 * saudacao) # essa linha no video foi apenas para mostar que podemos fazer com strings em python sendo uma variavel ou um texto direto colocado.

#segundo o video no minuto 17:05 (referindo-se ao primeiro video), o python NÃO apresenta constantes, com isso usamos de letras maiusculas por convenção para definir constantes

PI =  3.1415 #define a constante

raio = float (input('informe o raio da circunferencia?'))# input é utilizado para que haja uma entrada de info pelo usuario (como receber um nome, numero de algo ou etc)
#Já o float anterior a esse input foi utilizado para que o resultado do input fosse convertido ao float.

area = PI * pow(raio, 2) #aqui foi feito o calculo da area


print(f'A área de circ é {area} m²')