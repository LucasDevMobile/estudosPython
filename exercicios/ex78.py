#faca um programa que leaia 5 valores e guarde em uma lista
#mostre o maior e menor valor digitado e suas posicoes

lista=[]


lista.append(int(input('Digite o primeiro numero:'))),
lista.append(int(input('Digite o segundo numero:'))),
lista.append(int(input('Digite o terceiro numero:'))),
lista.append(int(input('Digite o quarto numero:'))),
lista.append(int(input('Digite o quinto numero:')))

maior=max(lista)
menor=min(lista)

print(f'Os numeros digitados foram {lista}')

print(f'O maior valor digitado foi {max(lista)} na posicao {lista.index(maior)} e o menor foi {min(lista)} na posicao {lista.index(menor)}')

