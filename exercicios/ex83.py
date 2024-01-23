#crie um programa q digite uma expressao q use parenteses
#devera analisar se a expressao esta com parenteses abertos e fechados na ordem correta
# ex: ((a+b)*(a*c)-2) errado

expressao = input("Digite uma expressão com parênteses: ")
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if not pilha:
            print("Os parênteses não estão balanceados.")
            break  # Se encontrou ')' sem correspondente '('
        pilha.pop()

if not pilha:
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")
