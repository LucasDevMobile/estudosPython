valores= []

for cont in range(0,5):
    valores.append(int(input('Digite um valor')))
    
for posicao, valor in enumerate(valores):
    print(f'Na posicao {posicao} encontrei o valor {valor}') 
