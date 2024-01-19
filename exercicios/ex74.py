#crie um programa q gere 5 numeros aleatorios
#mostre a listagem dos numeros gerados e tambem indique o menor e maior valor da tupla

from random import randint


numeros = [randint(1, 100) for c in range(5)]

print(f'Lista de numeros {numeros}')

tupla = sorted(numeros)

print(f'O maior numero eh {tupla[4]} e o menor numero eh {tupla[0]}')

#Outra forma:

numeros=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram:', end='')

for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')









   

   







