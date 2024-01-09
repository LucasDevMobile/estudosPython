# crie um programa q leia nome,idade,sexo de 4 pessoas e diga: a media de idade, o homem mais velho e qts mulheres tem menos de 20 anos

contsexo=0 
media=0
idade_velho=0
nomevelho=""
for c in range (1,5):



    nome=str(input('Qual o seu nome:'))
    idade=int(input('Qual a sua idade?'))
    sexo=(input('Qual o seu sexo? Digite m para masculino ou f para feminino:'))

    media=media+idade/4
    if idade <20 and sexo=='f':
        contsexo=contsexo+1

    if sexo == 'm' and idade > idade_velho:
        idade_velho = idade
        nomevelho = nome
    
        
print('A quantidade de mulheres com menos de 20 anos eh {}'.format(contsexo))

print('A media de idade eh {} anos'.format(media))

print('O homem mais velho eh o {}'.format(nomevelho))












