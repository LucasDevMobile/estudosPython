inicio=int(input('inicio '))
fim=int(input('fim '))
passo=int(input('passo '))   # le os dados do usuario e printa (passo= de qts em qts)
for num in range(inicio, fim+1, passo):
    print(num)
print('fim')