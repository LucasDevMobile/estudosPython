# crie um programa q leia nome,idade,sexo de 4 pessoas e diga: a media de idade, o homem mais velho e qts mulheres tem menos de 20 anos

contsexo=0 
media=0
for c in range (1,3):



    nome=str(input('Qual o seu nome:'))
    idade=int(input('Qual a sua idade?'))
    sexo=(input('Qual o seu sexo? Digite m para masculino ou f para feminino:'))

    media=media+idade/4
    if idade <20 and sexo=='f':
        contsexo=contsexo+1
    
        
print('A quantidade de mulheres com menos de 20 anos eh {}'.format(contsexo))

print('A media de idade eh {} anos'.format(media))









