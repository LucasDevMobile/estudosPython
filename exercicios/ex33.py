# Faca um programa q leia tres numeros e mostre qual e o maior e qual eh o menor

num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
num3=int(input('Digite o terceiro numero: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3


if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))