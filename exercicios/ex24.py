#crie um programa q leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"

cidade=input(' Digite o nome da cidade ')

if ('santo' in cidade):
    print('A cidade {} comeca com santo '.format(cidade) ) 
else:print('A cidade nao comeca com santo')
