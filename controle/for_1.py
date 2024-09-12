for i in range(10): #loop de 0 a 10
    print(i, end=' ')
    
print('')
    
for i in range(1, 11): #loop de 1 a 11
    print(i, end=' ')
    
print('')
    
for i in range(1, 100, 7): #loop de 1 a 100 de 7 em 7
    print(i, end=' ')
    
print('')

for i in range(20, 0, -3): #loop de 20 a 0 de -3 em -3
    print(i, end=' ')

print('')
    
nums = [2, 4, 6, 8]

for n in nums: #loop com os numeros da lista
    print(n, end=' ')

print('')
    
texto = 'Python é muito massa!'

for letra in texto: #loop com as letras da string
    print(letra, end=' ')

print('')

for n in {1, 2, 3, 4, 5, 5, 5}: #loop com os numeros da tupla, excluindo a repetição
    print(n, end=' ')

print('')

produto = {
    'nome': 'Caneta',
    'preco': 8.00,
    'desc': 0.5
}

for atrib in produto: #loop com as chaves e valores
    print(atrib, ': ', produto[atrib])
    
print('')
    
for atrib, valor in produto.items():
    print(atrib, ': ', valor)

print('')
    
for valor in produto.values(): #loop com os valores
    print(valor, end=' ')

print('')

for atrib in produto.keys(): #loop com as chaves
    print(atrib, end=' ')
