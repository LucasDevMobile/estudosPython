# crie um programa que leia o nome completo de uma pessoa e mostre:
# o nome com todos as letras maiusculas
# o nome com todas letras minusculas
#quantas letras ao todo( sem considerar espacos)
#quantas letras tem o primeiro nome

pessoa=str(input('Digite o nome da pessoa '))
print (pessoa.upper())
print (pessoa.lower())
print (len (pessoa))
print (len(pessoa[0:6]))

