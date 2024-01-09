#desenvolva um programa q leia o primeiro termo e a razao de uma P.A no final mostre os 10 primeiros termos

primeiro=int(input('Primeiro termo '))
razao=int(input('Razao '))
decimo=primeiro+(10-1)*razao

for c in range(primeiro,decimo+razao,razao):
    print('{}'.format(c),end=' >')
