#crie um programa q leia 4 valores e guarde em uma tupla
#qts vezes apareceu 9
#q posicao foi digitado primeiro 3
#numeros pares

n1=int(input('Digite o primeiro numero:'))
n2=int(input('Digite o segundo numero:'))
n3=int(input('Digite o terceiro numero:'))
n4=int(input('Digite o quarto numero:'))

tupla=(n1,n2,n3,n4)
par=0
print(f'O numero nove apareceu {tupla.count(9)}x')

if 3 in tupla:
    print(f'O numero 3 foi digitado na posicao {tupla.index(3)}')
else:print('O numero 3 nao foi digitado')

for c in tupla:
    if c % 2 ==0:
     par+=1
print(f'A quantidade de numeros pares foi {par}')

#outra forma:

num=int(input('Digite o primeiro numero:')),
int(input('Digite o primeiro numero:')),
int(input('Digite o primeiro numero:')),
int(input('Digite o primeiro numero:'))

print(f'O numero nove apareceu {num.count(9)}x')

if 3 in num:
    print(f'O numero 3 foi digitado na posicao {num.index(3)}')
else:print('O numero 3 nao foi digitado')

print('Os valores pares digitados foram ',end='')

for n in num:
    if n% 2 ==0:
        print(n, end='')


     