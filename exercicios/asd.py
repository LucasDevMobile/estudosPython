lista = []

while True:
    valor = int(input('Digite um valor: '))
    
    if valor not in lista:
        lista.append(valor)
    else:
        print('Valor já existente. Não será adicionado novamente.')
    
    continuar = input('Deseja continuar [S/N]: ').upper()
    
    if continuar == 'N':
        break

lista.sort()
print(f'Valores em ordem crescente: {lista}')
