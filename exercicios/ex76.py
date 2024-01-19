# crie uma tupla com nomes e precos no final mostre uma tabela

lista= ('computador', 9000,'mouse', 400, 'teclado', 850, 'monitor', 2000 , 'headset', 1200)

print('-'*30)
print('LISTA DE PRECOS')
print('-'*30)

for posicao in range(0, len(lista)):
    if posicao %2==0:
        print(f'{lista[posicao]:.<30}',end='')
    else:
        print(f'R$ {lista[posicao]:>7.2f}')