nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

 
if nota >= 9 and comportado:
     print('Duas palavras: para bens! :p')
     print('Quadro de Honra')
     
elif nota >= 7:
    print('Aprovado')
    
elif nota >= 5.5:
    print('Recuperação')
    
else:
    print('Reprovado')

print(nota)