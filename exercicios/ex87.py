#melhore o desafio anterior mostrando
# a soma de todos valores 
#soma da terceira coluna
#maior valor da segunda linha

soma_total =0
soma_terceira_coluna = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para {linha}, {coluna}: '))
        
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='' )
    print()


for linha in matriz:
    for elemento in linha:
        soma_total += elemento

print("A soma dos elementos da lista multidimensional é:", soma_total)


for linha in matriz:
    soma_terceira_coluna += linha[2]

print("A soma dos elementos da terceira coluna é:", soma_terceira_coluna)

maior_valor_segunda_linha = max(matriz[1])

print("O maior valor na segunda linha é:", maior_valor_segunda_linha)