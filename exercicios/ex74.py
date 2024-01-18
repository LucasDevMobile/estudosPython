#crie um programa q gere 5 numeros aleatorios
#mostre a listagem dos numeros gerados e tambem indique o menor e maior valor da tupla

from random import randint

# Lista para armazenar os 5 números aleatórios
numeros = [randint(1, 100) for _ in range(5)]

# Exibe os números antes de ordenar
print("Números antes de ordenar:", numeros)

# Ordena a lista
numeros_ordenados = sorted(numeros)

# Exibe os números ordenados
print("Números ordenados:", numeros_ordenados)

print(f'O maior numero eh {numeros_ordenados[4]} e o menor numero eh {numeros_ordenados[0]}')






   

   







