total = 0
pessoas = []
mais_pesadas = []
mais_leves = []

while True:
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    
    pessoas.append((nome, peso))
    total += 1

    continuar = input('Você deseja continuar? [S/N] ').upper()
    if continuar != 'S':
        break

# Inicializar variáveis para armazenar o maior e o menor peso
maior_peso = float('-inf')
menor_peso = float('inf')

# Encontrar as pessoas mais pesadas e mais leves usando if
for pessoa in pessoas:
    if pessoa[1] > maior_peso:
        mais_pesadas = [pessoa]
        maior_peso = pessoa[1]
    elif pessoa[1] == maior_peso:
        mais_pesadas.append(pessoa)
    
    if pessoa[1] < menor_peso:
        mais_leves = [pessoa]
        menor_peso = pessoa[1]
    elif pessoa[1] == menor_peso:
        mais_leves.append(pessoa)

print(f'Foram cadastradas {total} pessoas.')
print(f'As pessoas mais pesadas são: {mais_pesadas}')
print(f'As pessoas mais leves são: {mais_leves}')
``