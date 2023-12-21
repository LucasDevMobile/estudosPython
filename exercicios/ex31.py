# Desenvolva um programa que pergunte a distancia de uma viagem em km
# Calcule o preco da passagem,cobrando R$ 0.50 por km para viagens ate 200km e R$0.45 para viagens mais longas

distancia=int(input('Qual a distancia da viajem? '))

valor1=0.50
valor2=0.45

if distancia<=200:
    print('O valor da passagem eh {} reais'.format(distancia*valor1))
if distancia >200:
    print('O valor da passagem eh {} reais'.format(distancia*valor2))    


