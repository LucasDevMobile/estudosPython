# Escreva um programa q faca o computador"pensar" em um numero inteiro entre 0 e 5 e peca para o usuario
#tentar descobrir qual foi o numero escolhido. O programa devera escrever na tela venceu ou perdeu.
from random import randint
from time import sleep

computador=randint(0,1)
print('Estou pensando em um numero de 0 a 5, tente adivinhar '.upper())
jogador=int(input('Em que numero pensei? '))
print('Processando...')
sleep(2)
if jogador == computador:
    print('Parabens voce ganhou!'.upper())
else:
    print('VOCE PERDEU, eu pensei no numero {} e nao {}'.format(computador,jogador))