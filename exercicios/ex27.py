#crie um programa q leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o ultimo nome separadamente
#Exemplo: Ana Maria de Souza
#primeiro = ana     ultimo = souza

nome=str(input('Digite seu nome completo ')).strip()

nomecom=nome.split()
primeiro_nome=nomecom[0]
ultimo_nome=nomecom[-1]

print('Primeiro nome: {}'.format(primeiro_nome))
print('Último nome: {}'.format(ultimo_nome))






