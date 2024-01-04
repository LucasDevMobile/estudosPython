#faca um programa q leia o peso de cinco pessoas,no final mostre qual foi maior e menor peso

maiorpeso=0
menorpeso=9999

for c in range(1,6):
    peso=int(input('Peso da {} pessoa:'.format(c)))

    if peso>maiorpeso:
        maiorpeso=peso
        
#   if c==1:     <lendo a primeira pessoa>
#        maiorpeso=c    <vai receber o valor da primeira pessoa q digitou>
#        menorpeso=c    <vai receber o valor da primeira pessoa q digitou>
#   else:               <se nao for o primeiro laco> ou seja vai considerar o maior digitado
#        if peso>maiorpeso:
#           maiorpeso=peso 

#        if peso<menorpeso:
#           menorpeso=peso

    if peso < menorpeso:
        menorpeso=peso
print('O maior peso eh {} kilos'.format(maiorpeso))
print('O menor peso eh {} kilos'.format(menorpeso))    