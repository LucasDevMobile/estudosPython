#escreva um programa que faca o computador jogar jokenpo com vc
from random import randint

print('')
jogador=int(input('Digite 1 para pedra, 2 para papel ou 3 para tesoura: '))

computador= randint(1,3.)

if jogador==1 and computador==3:
    print('Ganhou')
elif jogador==1 and computador==2:
    print('Perdeu')
elif jogador==2 and computador==3:
    print('Perdeu')
elif jogador==2 and computador==1:
    print('Venceu')
elif jogador==3 and computador==2:
    print('Venceu')
elif jogador==3 and computador==1:
    print('Perdeu')
else:print('Empate')
print('Eu escolhi',computador)