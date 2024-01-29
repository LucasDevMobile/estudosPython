#crie um programa q crie palpites da mega sena
#perguntar quantos jogos que e sortear 6 numeros p cada jogo
#lista composta
from random import randint


jogos=[]
lista=[]
quantidade=int(input('Quantos jogos voce quer fazer?'))
totaljogos=1

while totaljogos<=quantidade:
    cont=0

    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    totaljogos+=1
    print(f'')
    
for i,l in enumerate(jogos):
    print(f'Jogo{i+1}: {l}')
    
