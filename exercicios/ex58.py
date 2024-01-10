from random import randint

computador=randint(0,9)
jogador=int(input('Digite um numero entre 0 e 9: '))
cont=0

while computador!=jogador:   #pode se criar uma variavel chamada acertou=false e usar while not acertou
    jogador=int(input('Digite um numero entre 0 e 9: '))
    cont=cont+1
print('PARABENS VOCE GANHOU!!!')
print('Voce errou {}x ate acertar'.format(cont))

    
