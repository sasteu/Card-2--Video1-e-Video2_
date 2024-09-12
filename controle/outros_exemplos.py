pessoas = ['Gui', 'Rebeca']
adj = ['Feio', 'Inteligente']

for p in pessoas: #loop dentro de loop
    for a in adj:
        print(f'{p} é {a}!')
        

for i in [1, 2, 3]: #usa pass para indicar uma repetição vazia
    pass


for i in range(1, 11): #sempre que for 1 ele pula quando for 0 ele imprime o valor de i
    if i % 2:
        continue
    print(i, end=' ')
    
print(' ')
    
for i in range(1, 11): #interrompe o loop quando i for 5
    if i == 5:
        break
    print(i, end=' ')
    
print(' ')
    
print('Fim')