#escreva um programa que leia o peso e altura de uma pessoa,calcule o imc e mostre seu status de acordo com tabela:
#abaixo de 18.5=abaixo do peso,entre 18.5 e 25=peso ideal,25 a 30=sobrepeso,30 a 40= obesidade,acima 40=morbida
print('')
peso=float(input('Qual a o seu peso? '))
altura=float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Voce esta abaixo do peso')

elif 18.5<= imc <=25:
    print('Parabens voce esta no peso ideal')

elif 26<= imc <=30:
    print('Voce esta acima do peso')

elif 31<= imc <=40:
    print('Voce esta obeso (a)')

else:print('CUIDADO VOCE ESTA COM OBESIDADE MORBIDA ')


