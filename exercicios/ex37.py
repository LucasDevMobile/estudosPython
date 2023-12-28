#escreva um programa que leia um numero inteiro e peca p usuario escolher a base de conversao:
#1 para binario 2 para octal 3 para hexadecimal

num=int(input('Digite um numero inteiro: '))

print('''Escolha uma das bases para conversao: 
[1] Converter para BINARIO 
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao=int(input('Sua opcao: '))

if opcao==1:
    print('{} convertido para BINARIO eh igual a {}'.format(num,bin(num)[2:]))
elif opcao==2:
    print('{} convertido para OCTAL eh {}'.format(num,oct(num)[2:]))
elif opcao==3:
    print('{} convertido para HEXADECIMAL eh {}'.format(num,hex(num)[2:]))
else:
    print('Opcao invalida')