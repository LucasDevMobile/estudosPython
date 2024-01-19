
n1=int(input('digite um numero'))
n2=int(input('digite um numero'))
n3=int(input('digite um numero'))
n4=int(input('digite um numero'))

tupla=(n1,n2,n3,n4)


print(f'O numero 9 apareceu {tupla.count(9)}x')
print(f'O primeiro valor 3 foi digitado na posicao:{tupla.index(3)}')

if tupla %2 == 0:
    tupla+=1
    print(tupla) 
