from functools import reduce  

def somar_nota(delta):  
    def somar(nota): 
        return nota + delta
    return somar  

notas = [6.4, 7.2, 5.8, 8.4]  

notas_finais = map(somar_nota(1.5), notas)  # Usa a função 'map' para aplicar a função 'somar_nota(1.5)' a cada elemento da lista 'notas'.
print(list(notas_finais))  # Converte o resultado de 'map' em uma lista e exibe as notas finais.

def somar(a, b):  
    return a + b

total = reduce(somar, notas, 0)  # Usa 'reduce' para somar todas as notas da lista, começando com o valor inicial 0.
print(total)  

# for i, nota in enumerate(notas):  
#    notas[i] = nota + 1.5  # Adiciona 1.5 a cada nota, modificando diretamente a lista original.

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5  # Outra forma de adicionar 1.5 a cada nota, percorrendo a lista por índices.
