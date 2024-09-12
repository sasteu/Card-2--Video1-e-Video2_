def soma(*nums):  # Define a função 'soma' que recebe múltiplos argumentos, armazenados como uma tupla.
    total = 0  
    for n in nums:  
        total += n  
    return total  # Retorna o valor final de 'total' (a soma de todos os números).

def resultado_final(**kwargs):  # Define a função 'resultado_final' que recebe argumentos nomeados, armazenados como um dicionário.
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'  # Verifica se a nota é maior ou igual a 7. Se for, define o status como 'aprovado(a)', caso contrário, 'reprovado(a)'.
    return f'{kwargs["nome"]} foi {status}'  
