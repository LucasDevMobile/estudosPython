#faca um programa que leia um numero e mostre seu fatorial
#exemplo: 5! 5*4*3*2*1=120

numero = int(input("Digite um número para calcular o fatorial: "))
c=numero  # contador comeca com o numero digitado
f=1  #fator inicial na multiplicacao
print('Calculando {}! = '.format(numero))
while c>0:
    print('{}'.format(c),end='') #end '' nao pula de linha
    print(' x 'if c > 1 else ' = ',end='')
    f=f*c
    c=c-1
print('{}'.format(f))

