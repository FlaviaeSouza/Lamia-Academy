#! python3
"""
def saudacao(): #nossa primeira função não vai receber nenhum parametro, Def é usado para definir uma função
    #toda função em python define um bloco ent mesmo que a funcao n faça nada ela precisa no minimo de um pass
    print('Bom dia')
"""

def saudacao(nome = 'pessoa', idade = 20): #nossa segunda função possui um parametro do tipo string e outro int, o nome = 'pessoa' serve,
#para mesmo que a pessoa não coloque uma string no parametro o codigo consiga continuar, nesse caso ele ja tem uma 
#predefinida que seria 'pessoa'
    print(f'Bom dia {nome}!\n  você nem parece ter {idade} anos!')#\n é utilizado apra quebra de linha

# def saudacao(): 
#     print('Boa tarde')
#função apenas para mostrar que python n tem sobrecarga, contudo quando chamamos duas
# funções com o mesmo nome pode ter sobrescrição


def soma_e_multi(a,b,x):
    return (a+b)*x #foi colocado () por conta da precedencia

if __name__ == '__main__': #usado se quiser que aconteça, caso o codigo seja executado no arquivo que deu start a sua aplicação.
    saudacao('Ana', idade = 30)