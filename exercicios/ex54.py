# crie um programa q leia o ano de nascimento de sete pessoas e mostre qts pessoas ainda nao sao maiores de idade e qts ja sao
from datetime import date
contmaior=0
contmenor=0
ano1=date.today().year
for c in range (1,8):
    ano=int(input('Digite o ano que voce nasceu:'))

    if ano1-ano>=18:
        contmaior=contmaior+1
    else:contmenor=contmenor+1


print('{} pessoas sao maiores de idade e {} sao menores de idade'.format(contmaior,contmenor))