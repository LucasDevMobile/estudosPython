# Faca um programa q leia um ano qualquer e mostre se ele eh bissexto

ano=int(input('digite o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Esse ano eh Bissexto')
       
else:
    print('Esse ano nao eh Bissexto')
        