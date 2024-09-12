from functools import reduce

alunos = [ 
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Bruno', 'nota': 7.3},
    {'nome': 'Claudia', 'nota': 6.4},
    {'nome': 'Diogo', 'nota': 6.5},
    {'nome': 'Ernesto', 'nota': 7.6},
]

somar = lambda a, b: a + b  # Define uma função lambda que recebe dois números e retorna a soma deles

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]  # Cria uma lista apenas com os alunos cuja nota é maior ou igual a 7 (aprovados)
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]  # Extrai as notas dos alunos aprovados em uma lista separada
total = reduce(somar, notas_alunos_aprovados, 0)  # Usa 'reduce' para somar todas as notas dos alunos aprovados, começando com o valor inicial 0

print(notas_alunos_aprovados) 
print(total / len(alunos_aprovados))  
