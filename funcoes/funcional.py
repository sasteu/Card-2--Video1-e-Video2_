def soma(a, b):  
    return a + b

def sub(a, b):  
    return a - b

#somar = soma  
#print(somar(3, 4))  # Como usar 'somar' para realizar uma soma.

def operacao_aritmetica(fn, op1, op2):  
    return fn(op1, op2)

resultado = operacao_aritmetica(soma, 13, 48)  
print(resultado)  

resultado = operacao_aritmetica(sub, 13, 48)  
print(resultado)  

def soma_parcial(a):  # Define uma função que aceita um número 'a' e retorna outra função que somará 'a' com outro valor.
    def concluir_soma(b):  # Função interna que realiza a soma de 'a' com 'b'.
        return a + b
    return concluir_soma  # Retorna a função 'concluir_soma'.

resultado_final = soma_parcial(10)(12)  # Primeiro, 'soma_parcial(10)' retorna uma função, que em seguida é chamada com o valor 12.
print(resultado_final)  
