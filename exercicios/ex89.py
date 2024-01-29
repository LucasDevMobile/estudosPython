#Crie um programa q leia o nome e duas notas de alunos e guarde em uma lista
#perguntar se quer continuar
#mostrar media a acessar nome do aluno pra saber qual foram as duas notas

lista=[]

while True:

    aluno=str(input('Digite o nome:'))
    nota=float(input('Digite a primeira nota:'))
    nota2=float(input('Digite a primeira nota:'))
    lista.append(aluno)
    lista.append(nota)
    lista.append(nota2)
    continuar=str(input('Deseja continuar [S/N]')).upper()
    if continuar=='N':
        break
print(lista)

    
