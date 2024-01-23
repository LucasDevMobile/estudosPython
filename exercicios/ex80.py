# Cria uma lista vazia para armazenar os valores
lista_ordenada = []

# Loop para inserir 5 valores
for i in range(5):
    # Solicita ao usuário para inserir um valor
    valor = int(input(f"Insira o {i + 1}º valor: "))

    # Encontra a posição correta para inserir o valor na lista
    posicao = 0
    while posicao < len(lista_ordenada) and lista_ordenada[posicao] < valor:
        posicao += 1

    # Insere o valor na posição correta
    lista_ordenada.insert(posicao, valor)

    # Exibe a posição em que o valor foi inserido
    print(f"O valor {valor} foi inserido na posição {posicao + 1} da lista.")

# Exibe a lista ordenada
print("Lista ordenada:", lista_ordenada)
