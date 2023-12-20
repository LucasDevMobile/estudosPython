#crie um programa q leia o nome de uma cidade e diga se ela comeca ou nao com o nome "santo"

cidade=str(input('Em que cidade voce nasceu? ')).strip()
print(cidade[:5].upper()=='SANTO')