# crie um programa que tem uma tupla preenchida por extenso de 0 a 20
#o programa devera ler o numero e printar ele por extenso

num=int(input('Digite um numero entre 0 e 20:'))

numext= ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
         'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete',
         'Dezoito', 'Dezenove', 'Vinte')

while num < 0 or num > 20:   
    num=int(input('Digite um numero entre 0 e 20:'))

print(f'Voce digitou o numero {numext[num]}')
    
    

    
   
    