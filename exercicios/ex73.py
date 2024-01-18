#crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirao na ordem de colocacao
#depois mostre: apenas os 5 primeiros
#os 4 ultimos
#ordem alfabetica
#posicao do corinthians

bralileirao = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'RB Bragantino', 'Fluminense',
              'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá Saf', 'Corinthians',
                'Cruzeiro', 'Vasco', 'Bahia', 'Santos')
print('')

print(f'Os cinco primeiros colocados sao:{bralileirao [0:5]}')
print('')
print(f'Os 4 ultimos colocados sao:{bralileirao[-4:]}')
print('')
print(f'Os times em ordem alfabetica sao:{sorted(bralileirao)}')
print('')
print(f'A posicao do corinthians no campeonato eh:{bralileirao.index('Corinthians')}')
