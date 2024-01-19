#listas sao mutaveis

lista=['lanche','coca','doce','agua']

lista[2]='cerveja'          # troca o doce pela cerveja

lista.append('chocolate')   # adiciona um item no fim da lista

lista.insert(1,'dog')       # adiciona um item na posicao desejada

del lista[3]                # remove o item na posicao selecionada

lista.pop(3)                # remove o ultimo item da lista ou o selecionado, msm sem selecionar precisa do ()  

lista.remove('doce')        # remove o item pelo nome (se tiver nomes ou numeros repetidos remove o primeiro)

if 'coca' in lista:
    lista.remove('coca')    # remove o item caso ele esteja na lista
    
#========================================================================================================#

# criando listas com Range

valores=list(range(4,11))   # cria uma lista de 4 ate 10

valores.sort()              # ordena os valores da lista

valores.sort(reverse=True)  # ordena na ordem inversa

len(valores)                # mostra quantos elementos tem na lista

#========================================================================================================#

#Exemplos:

#1::::::::::::::

valores= []                 # cria uma lista vazia

valores.append(5)           
valores.append(9)           # adiciona valores a lista
valores.append(4)

for posicao, valor in enumerate(valores):
    print(f'Na posicao {posicao} encontrei o valor {valor}')    #printa a posicao e o valor de cada numero da lista
    
#2::::::::::::::

valores= []

for cont in range(0,5):
    valores.append(int(input('Digite um valor')))   # mesma coisa do ex acima mas o usuario digita os valores
    
for posicao, valor in enumerate(valores):
    print(f'Na posicao {posicao} encontrei o valor {valor}') 
    
#3::::::::::::::

a= [2,3,4,7]
b=a             # a partir do momento em q se liga 2 listas a mudanca q fizer em uma serve pra outra
b[2]=8          # nesse caso a lista A e B terao seu valor da posicao 2 alterado pra 8

#4::::::::::::::

a= [2,3,4,7]
b=a [:]            # faz uma copia dos valores de A e nao tem ligacao com A
b[2]=8 






    
    




  

