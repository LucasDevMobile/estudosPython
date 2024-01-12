#Crie um programa q leia o nome e o preco de varios produtos,perguntar se quer continuar
#mostrar total gasto,qts produtos custam mais de 1000,nome do produto mais barato

total = maismil =0
barato=None
print('')
print('-='*7)
print('LOJAS PYTHON')
print('-='*7)
print('')

while True:

    produto=str(input('Digite o nome do produto:'))
    preco=float(input('Digite o valor do produto:'))

    next=' '
    while next not in 'SN':
        next=str(input('Deseja continuar [S/N]')).upper()

    if preco>1000:
        maismil+=1

    total=total+preco

    
    if barato is None or preco < barato:
        barato = preco


    if next=='N':
        break

print('')
print(f'O gasto total nas compras foi R$ {total:.2f}')
print('')
print(f'A quantidade de produtos maior que mil reais foi {maismil}')
print('')
print(f'O produto mais barato foi R$ {barato:.2f}')
