# Escreva um programa q leia a velocidade de um carro
# Se ele ultrapassar 80km/h,mostre uma mensagem dizendo q ele foi multado
# A multa vai custar R$ 7.00 por cada km acima do limite

vel=int(input('Velocidade do carro '))

multaKm = 7
limite = 80
kmUltrapassado = vel-limite

if vel > limite:
   
    valorMulta = (kmUltrapassado*multaKm)

    print('Voce foi multado')
    print('O valor da multa foi {:.2f} reais'.format(valorMulta))
