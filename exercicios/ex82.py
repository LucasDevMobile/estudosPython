#crie um programa q leia varios numeros e coloque em uma lsita
#crie duas listas exttras que vao conter apenas os valores pares e impares
#mostre o conteudo das 3 listas

listafull=[]
listapar=[]
listaimpar=[]


while True:

    valor=int(input('Digite um valor:'))
    listafull.append(valor)

    continuar = input('Deseja continuar [S/N]: ').upper()
    if continuar == 'N':
        break

for c in listafull:
        if c %2==0:
            listapar.append(c)
        else:
             listaimpar.append(c)
        
print(f'Lista completa:{listafull}')
print(f'Lista de numeros pares:{listapar}')
print(f'Lista de numeros impares:{listaimpar}')




