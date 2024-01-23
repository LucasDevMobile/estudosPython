#crie um programa q leia varios numeros e coloque em uma lista e mostre:
#quantos numeros foram digitados
#lista ordenada de forma descrescente
#se o 5 foi digitado e esta ou nao na lista

lista=[]
cont=0
while True:
    valor=int(input('Digite um valor:'))

    continuar = input('Deseja continuar [S/N]: ').upper()

    lista.append(valor)

    cont+=1
    
    if continuar == 'N':
        break   

if 5 in lista:
    print('o valor 5 foi digitado e esta na lista')
else:print('O numero 5 nao esta na lista')

lista.sort(reverse=True)  

print(f'Fora digitados {cont} numeros')

print(f'A lista decrescente ficou assim: {lista}')
