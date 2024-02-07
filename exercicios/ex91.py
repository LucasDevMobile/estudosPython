from random import randint

# Resultados dos dados para cada jogador
resultados = {}

resultados['jogador1'] = randint(1, 6)
resultados['jogador2'] = randint(1, 6)
resultados['jogador3'] = randint(1, 6)
resultados['jogador4'] = randint(1, 6)

# Imprime os resultados de cada jogador
for jogador, resultado in resultados.items():
    print(f'{jogador} tirou {resultado}')

# Calcula a pontuação máxima
pontuacao_maxima = max(resultados.values())

# Identifica os jogadores que obtiveram a pontuação máxima
vencedores = [jogador for jogador, resultado in resultados.items() if resultado == pontuacao_maxima]

# Imprime o vencedor ou vencedores
if len(vencedores) == 1:
    print(f'O vencedor é o {vencedores[0]} com {pontuacao_maxima} pontos!')
else:
    print(f'Temos um empate! Os vencedores com {pontuacao_maxima} pontos são: {", ".join(vencedores)}')
