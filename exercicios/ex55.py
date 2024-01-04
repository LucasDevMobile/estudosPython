#faca um programa q leia o peso de cinco pessoas,no final mostre qual foi maior e menor peso

maiorpeso=0
menorpeso=9999

for c in range(1,6):
    peso=int(input('Qual o seu peso:'))

    if peso>maiorpeso:
        maiorpeso=peso

    if peso < menorpeso:
        menorpeso=peso
print('O maior peso eh {} kilos'.format(maiorpeso))
print('O menor peso eh {} kilos'.format(menorpeso))    