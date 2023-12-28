#A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria de acordo com a idade: ate 9 anos=mirim,ate 14=infantil,ate 19=junior,ate 20=senior,acima=master

from datetime import date

ano= int(input('Digite o ano que voce nasceu: '))
ano=date.today().year-ano

if ano <=9:
    print('Mirim')

elif 10<= ano <=14:
    print('Infantil')

elif 15<= ano <=19:
    print('Junior')

elif ano==20:
    print('Senior')

else: print('Master')


