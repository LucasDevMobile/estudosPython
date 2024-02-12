#crie um programa onde 4 jogadores joguem um dado
#no final mostre o resultado de todos e qual foi o vencedor

from random import randint


resultados = {}

resultados['jogador1'] = randint(1, 6)
resultados['jogador2'] = randint(1, 6)
resultados['jogador3'] = randint(1, 6)
resultados['jogador4'] = randint(1, 6)


for jogador, resultado in resultados.items():
    print(f'{jogador} tirou {resultado}')


pontuacao_maxima = max(resultados.values())


vencedores = [jogador for jogador, resultado in resultados.items() if resultado == pontuacao_maxima]


if len(vencedores) == 1:
    print(f'O vencedor é o {vencedores[0]} com {pontuacao_maxima} pontos!')
else:
    print(f'Temos um empate! Os vencedores com {pontuacao_maxima} pontos são: {", ".join(vencedores)}')
