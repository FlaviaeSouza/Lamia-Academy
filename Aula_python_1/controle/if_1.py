
nota = float(input('informe a nota do aluno: ')) # recebe a nota do aluno com o input e converte em float
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado: # se nota maior igual a nove  for True execute esse bloco a seguir (e se for comportado)
    # Identação é a forma utilizada para definir blocos em python por exemplo a seguir vamos utiliza-lo para definir o inicio e fim do if
    print('Parabens!')
    print('Você está no quadro de honra')

elif nota >= 7:
    print('Aprovado!')

else: 
    print('Reprovado :c')


print(nota)
