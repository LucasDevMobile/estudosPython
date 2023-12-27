#escreva um programa que leia o ano de nascimento de uma pessoa e informe de acordo com a idade
#se ele ainda vai se alistar no exercito, se eh a hora de se alistar, se ja passou do tempo de alistamento
#seu programa tambem devera mostrar o tempo que falta ou q passou do prazo
from datetime import date

ano=int(input('Em que ano voce nasceu? '))
ano=date.today().year-ano
falta=18-ano
passou=ano-18

if ano<18:
    print('Voce ainda vai se alistar,faltam {} anos '.format(falta))
elif ano==18:
    print('Esta na hora de se alistar ')
else:
    print('Voce ja passou {} anos da data de alistamento'.format(passou))


