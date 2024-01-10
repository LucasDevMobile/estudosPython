#crie um programa q leia um numero n e mostre os n primeiros elementos de um fibonacci

print('-'*22)
print('Sequencia de Fibonacci')
print('-'*22)
n=int(input('Quantos termos voce quer mostrar? '))
termo1=0
termo2=1

print('~'*22)
print('{} 🠖 {}'.format(termo1,termo2), end='')
cont=3
while cont<=n:
    termo3=termo1+termo2
    print(' 🠖 {}'.format(termo3),end='')
    termo1=termo2
    termo2=termo3
    cont+=1
print(' 🠖 FIM')