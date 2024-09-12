
total = 0
nota = 0
qtde = 0

while nota != -1: #faz um loop ate que a condição de termino ocorra
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde += 1
        total += nota

print(f'A méd da turam é {total / qtde}') 

x = 10

while x: #igual for mas usando while, melhor usar for nesse caso
    print(x)
    x -= 1

print('Fim')
