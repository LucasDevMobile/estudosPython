#faca um programa q leia nome e media de um aluno guardando em um dicionario
#no final mostre na tela

final={}

final ['nome']=str(input('Digite seu nome:'))
final['media']=float(input('Digite a media:'))

if final ['media'] < 5:
    print(f'Voce foi reprovado, sua media foi {final["media"]}')
else:
    print(f'Voce foi aprovado,sua media foi {final["media"]}')



