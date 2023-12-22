# Escreva um programa q leia a velocidade de um carro
# Se ele ultrapassar 80km/h,mostre uma mensagem dizendo q ele foi multado
# A multa vai custar R$ 7.00 por cada km acima do limite

vel=float(input('Velocidade do carro '))


if vel > 80:
   
    valorMulta = (vel-80)*7

    print('Voce foi multado')
    print('O valor da multa foi {:.2f} reais'.format(valorMulta))
else: print('Tenha um bom dia, dirija com seguranca ')
