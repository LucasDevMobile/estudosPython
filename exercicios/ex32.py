# Faca um programa q leia um ano qualquer e mostre se ele eh bissexto

from datetime import date

ano=int(input('Que ano voce quer analizar? Digite 0 para o ano atual '))

if ano==0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100!=0 or ano % 400==0:
    print('O ano {} eh BISSEXTO'.format(ano))
else:
    print('O ano {} nao eh BISSEXTO'.format(ano))
    

        