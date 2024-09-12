def saudacao(nome='Pessoa', idade=20):  # Define a função 'saudacao' com valores padrão para 'nome' e 'idade'
    print(f'Bom dia! {nome}!\n Voce nem parece ter {idade} anos!')  # Exibe uma saudação com o nome e a idade

if __name__ == '__main__':  # Verifica se o arquivo está sendo executado diretamente, e não importado como módulo
    saudacao('Ana', idade=30)  # Se for o arquivo principal, chama a função 'saudacao' passando 'Ana' e 'idade=30'

def soma_e_multi(a, b, x):  # Define a função 'soma_e_multi' que recebe três parâmetros
    return a + b * x  # Retorna o resultado da soma de 'a' com o produto de 'b' e 'x'
