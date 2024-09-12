from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota' : 7.2},
    {'nome': 'Bruno', 'nota' : 7.3},
    {'nome': 'Claudia', 'nota' : 6.4},
    {'nome': 'Diogo', 'nota' : 6.5},
    {'nome': 'Ernesto', 'nota' : 7.6},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7  # lambda para verificar aprovação
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

# Converte o resultado de filter para uma lista para usar várias vezes
alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados, 0)

print(notas_alunos_aprovados)
print(total / len(alunos_aprovados)) 
