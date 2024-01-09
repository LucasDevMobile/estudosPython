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
menor=numero2>numero1



while pessoa==pessoa:
     
     if pessoa==1:
          print(numero1+numero2)
          break
     elif pessoa==2:
          print(numero1*numero2)
          break
     elif pessoa==3:
          if numero1>numero2:print('O numero {} eh maior'.format(numero1))
          else:print('O numero {} eh maior'.format(numero2))
          break
     
          
          
     else:break
     
          
print('fim')


   
    
    


    
 