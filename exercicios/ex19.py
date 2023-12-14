#um professor quer sortear um dos seus 4 alunos para apagar o quadro,crie um programa q ajude ele,lendo o nome dos alunos e escrevendo o nome do escolhido
import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Lista de alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sortear um aluno aleatoriamente
aluno_escolhido = random.choice(alunos)

# Exibir o resultado
print('O aluno escolhido para apagar o quadro foi: {}'.format(aluno_escolhido))