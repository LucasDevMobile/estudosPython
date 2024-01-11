from random import randint

print('=' * 26)
print('Vamos jogar par ou ímpar?')
print('=' * 26)

cont = 0

while True:
    jogador = int(input('Escolha seu número: '))
    jogador1 = str(input('Par ou ímpar? [P/I]')).upper()

    computador = randint(0, 10)
    result = jogador + computador

    print(f'Você escolheu {jogador} e o computador escolheu {computador}. O resultado é {result}.')

    if (result % 2 == 0 and jogador1 == 'P') or (result % 2 != 0 and jogador1 == 'I'):
        print('Você venceu!')
        cont += 1
    else:
        print('Você perdeu!')
        break

print(f'Você venceu {cont}x antes de perder')
