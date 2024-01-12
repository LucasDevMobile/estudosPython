print('='*20)
print('CADASTRO DE PESSOAS')
print('='*20)

maior = 0
homem = 0
menor20 = 0

while True:
    try:
        idade = int(input('Qual a sua idade? '))
    except ValueError:
        print('Por favor, digite uma idade válida.')
        continue  # Volta para o início do loop
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo? [M/F] ')).upper()

    if idade > 18:
        maior += 1

    if sexo == 'M':
        homem += 1

    if sexo == 'F' and idade < 20:
        menor20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você deseja continuar? [S/N] ')).upper()

    if continuar == 'N':
        break

print(f'Pessoas com mais de 18 anos: {maior}, Mulheres com menos de 20 anos: {menor20}, Total de homens: {homem}')
