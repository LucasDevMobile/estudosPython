#Crie um programa q leia o nome e duas notas de alunos e guarde em uma lista
#perguntar se quer continuar
#mostrar media a acessar nome do aluno pra saber qual foram as duas notas

ficha=[]

while True:

    aluno=str(input('Digite o nome:'))
    nota1=float(input('Digite a primeira nota:'))
    nota2=float(input('Digite a primeira nota:'))
    media=(nota1+nota2) / 2

    ficha.append([aluno,[nota1,nota2],media])
    
    continuar=str(input('Deseja continuar [S/N]')).upper()
    if continuar=='N':
        break

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    opc=int(input('Mostrar notas de qual aluno? (999 para interromper):'))
    if opc==999:
        break
    if opc<=len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1] }')
    
