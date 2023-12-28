#escreva um programa que faca o computador jogar jokenpo com vc
from random import randint
from time import sleep

print('')
itens= ('PEDRA','PAPEL','TESOURA')
computador=randint(0,2)

print('''Suas opcoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador=int(input('Qual eh a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*12)
print('Jogador jogou {} '.format(itens[jogador]))
print('Computador jogou {} '.format(itens[computador]))
print('-='*12)

if computador ==0:
    if jogador==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCEU')
    elif jogador==2:
        print('COMPUTADOR VENCEU')
    else: print('Jogada invalida')
    
elif computador==1:
    if jogador==0:
        print('COMPUTADOR VENCEU')
    elif jogador==1:
         print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCEU')
    else: print('Jogada invalida')
    
elif computador==2:
    if jogador==0:
        print('JOGADOR VENCEU')
    elif jogador==1:
         print('COMPUTADOR VENCEU')
    elif jogador==2:
        print('EMPATE')
    else: print('Jogada invalida')
    



