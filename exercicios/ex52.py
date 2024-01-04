# faca um programa q leia um numero e diga se ele eh primo

num=int(input('Digite um numero:'))
total=0
for c in range(1,num+1):
    if num % c ==0:
        print('\033[34m', end='')
        total+=1
    else:
        print('\033[31m',end='')
    print('{} '.format(c),end='')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num,total))
if total==2:
    print('E por isso ele eh primo')
else:
    print('E por isso ele nao eh primo')
