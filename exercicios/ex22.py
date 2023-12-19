# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todos as letras maiusculas
# o nome com todas letras minusculas
#quantas letras ao todo( sem considerar espacos)
#quantas letras tem o primeiro nome

nome=str(input('Digite o nome da pessoa ')).strip()    #o .strip exclui espacos digitados sem querer
print('Analisando seu nome...')
print('Seu nome em maiusculas eh {} '.format(nome.upper()))
print('Seu nome em minusculas eh {} '.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)-nome.count(' ')))  # -nome.count tira os espacos do meio
print('Seu primeiro nome tem {} letras '.format(nome.find(' '))) # .find ' ' acha o primeiro espaco entre os nomes


