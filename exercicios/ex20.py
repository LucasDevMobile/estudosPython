# sortear a ordem de apresentacao de trabalhos de 4 alunos
from random import shuffle

aluno1=input('Nome do aluno')
aluno2=input('Nome do aluno')
aluno3=input('Nome do aluno')
aluno4=input('Nome do aluno')
lista = [aluno1,aluno2,aluno3,aluno4]
ordem= shuffle(lista)
print('A ordem de apresentacao eh {}'.format(lista))
