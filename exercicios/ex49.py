#reforce o exercicio 9 mostrando a tabuada de um numero que o usuario escolher usando o laco for

num=int(input('Digite um numero:'))
print('='*11)
for c in range(1,11):
    print('{} x {} = {}'.format(num,c,num*c))
print('='*11)
        