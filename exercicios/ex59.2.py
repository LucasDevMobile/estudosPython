from time import sleep

n1=int(input('Dgite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
opcao=0
while opcao!=5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    print('')
    opcao=int(input('Qual a sua opcao? '))
    
    if opcao==1:
        soma=n1+n2
        print('A soma entre {} e {} eh {}'.format(n1,n2,soma))
        
    elif opcao==2:
        mult=n1*n2
        print('O resultado de {}x{} eh {}'.format(n1,n2,mult))
        
    elif opcao==3:
        if n1>n2:
            maior=n1
        else:maior=n2
        print('Entre {} e {} o maior valor eh {}'.format(n1,n2,maior))
        
    elif opcao==4:
        print('Informe os numeros novamente') 
        n1=int(input('Dgite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: ')) 
        
    elif opcao==5:
        print('Finalizando')
        
    else:
        print('Opcao invalida!')
    print('=-='*10)
    sleep(2)
          
    
print('Fim do Programa!')
