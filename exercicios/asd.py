tupla = ('arthur', 'lucas', 'ana', 'sergio', 'larissa', 'marcia', 'rodrigo', 'lauane', 'alice', 'noah', 'danilo')

vogais = 'aeiou'

for palavra in tupla:
    print(f'Na palavra {palavra} temos as vogais:', end=' ')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
    print()  # Pular para a próxima linha após imprimir as vogais de uma palavra
