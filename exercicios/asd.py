from random import randint

# Lista para armazenar os 5 números aleatórios
numeros = [randint(1, 100) for _ in range(5)]

# Exibe os números antes de ordenar
print("Números antes de ordenar:", numeros)

# Ordena a lista
numeros_ordenados = sorted(numeros)

# Exibe os números ordenados
print("Números ordenados:", numeros_ordenados)
