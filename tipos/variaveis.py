#!python3
a = 3
b = 4.4

print(a + b)

texto = 'Sua idade e...'
idade = 23

# print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = 'bom dia '
print(3 * saudacao)

PI = 3.14
raio = float(input('Informe o raio da circunferencia? '))
area = PI * pow(raio, 2)
print(f'A area da circ é {area} m2.')