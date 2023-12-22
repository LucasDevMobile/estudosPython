# Desenvolva um programa que pergunte a distancia de uma viagem em km
# Calcule o preco da passagem,cobrando R$ 0.50 por km para viagens ate 200km e R$0.45 para viagens mais longas

distancia=float(input('Qual a distancia da viajem? '))

if distancia<=200:
    preco=distancia*0.50
   
else:
    preco=distancia*0.45
    print('O valor da passagem eh {:.2f} reais'.format(preco))    


