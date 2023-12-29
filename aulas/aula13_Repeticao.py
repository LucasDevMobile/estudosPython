for num in range(1,6):
    print('oi')              # printa o 'oi 5 vezes
    
for num in range(1,6):       # printa os numeros de 1 a 5
    print(num)
    
for num in range(1,6,2):     # printa os numeros de 1 a 5 de 2 em 2
    print(num)
    
for num in range(6,0,-1):    # printa os numeros do 6 ate o 1
    print(num)
    
n=int(input('Digite um numero: '))
for num in range(0,n+1):     # printa a sequencia q o usuario digitar
    print(num)
    
inicio=int(input('inicio '))
fim=int(input('fim '))
passo=int(input('passo '))   # le os dados do usuario e printa (passo= de qts em qts)
for num in range(inicio, fim+1, passo):
    print(num)
print('fim')

for num in range(0,3):       # vai pedir p usuario digitar um numero 3 vezes
    numero=int(input('Digite um numero'))
    
soma=0
for num in range(1,4):
    numero=int(input('Digite um Numero'))
    soma=soma + numero       # pede para o usuario digitar 3 valores e faz a soma
print('O valor do somatorio foi {}'.format(soma))
    
    
