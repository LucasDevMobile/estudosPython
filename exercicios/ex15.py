# Escreva um programa q pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias alugado
# Calcule o preco a pagar,sabendo q o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km=float(input('Quantidade de km? '))
dia=float(input('Quantidade de dias? '))
valor= (km*0.15) + (dia*60)
print('O valor total foi {} reais'.format(valor))