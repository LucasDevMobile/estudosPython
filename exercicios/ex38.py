#escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mesnsagem
#o primeiro valor eh maior,o segundo valor eh maior,nao existe valor maior,os dois sao iguais

n1=int(input('Digite o primeiro numero '))
n2=int(input('Digite o segundo numero '))

if n1>n2:
    print('O primeiro numero eh maior ')
elif n2>n1:
    print('O segundo numero eh maior ')
else: print('Nao existe numero maior, os dois sao iguais! ')