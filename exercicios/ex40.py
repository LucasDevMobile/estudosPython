#escreva um programa que leia duas notas de alunos e calcule sua media,mostrando uma msg de acordo com a media 
#media abaixo de 5.0 reprovado, media entre 5.0 e 6.9 recuperacao, media 7.0 ou superior aprovado

nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))
media=(nota1+nota2)/2 

if media< 5:
    print('REPROVADO')
elif 5 <= media <= 6.9:   # pode se usar elif media > 5 and <=6.9
    print('RECUPERACAO')
else:
    print('APROVADO')