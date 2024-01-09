#crie um programa que leia dois valores emostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

numero1=int(input('Dgite o primeiro valor: '))
numero2=int(input('Digite o segundo valor: '))
print('')


print('''
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos numeros
 [5] sair do programa''')
print('')

pessoa=int(input('O que deseja fazer com esses valores? '))
maior=numero1>numero2
maior2=numero2>numero1

if pessoa == 1:
    print('O resultado da soma dos valores eh {}'.format(numero1+numero2))
elif pessoa == 2:
    print('O resultado da multiplicacao dos valores eh {}'.format(numero1*numero2))
elif pessoa == 3:
    if numero1>numero2:
        print('O numero {} eh maior que o numero {}'.format(numero1,numero2))
    else:print('O numero {} eh maior que  o numero {}'.format(numero2,numero1))
elif pessoa ==5:
    print('Voce fechou o programa')
    
while pessoa == 4:
    numero1=int(input('Dgite o primeiro valor: '))
    numero2=int(input('Digite o segundo valor: '))
    print('''
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos numeros
 [5] sair do programa''')

    pessoa=int(input('O que deseja fazer com esses valores? '))
   
    if pessoa == 1:
        print('O resultado da soma dos valores eh {}'.format(numero1+numero2))
    elif pessoa == 2:
        print('O resultado da multiplicacao dos valores eh {}'.format(numero1*numero2))
    elif pessoa == 3:
        if numero1>numero2:
            print('O numero {} eh maior que o numero {}'.format(numero1,numero2))
        else:print('O numero {} eh maior que  o numero {}'.format(numero2,numero1))
    elif pessoa ==5:
        print('Voce fechou o programa')
    
    


   
    
    


    
 