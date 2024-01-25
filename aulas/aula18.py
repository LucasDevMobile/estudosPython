dados=[]                     # cria uma lista vazia

dados.append('lucas')        # adiciona 'lucas a lista

dados.append(35)             # adiciona 35 a lista

pessoas=[]                   # cria uma lista vazia

pessoas.append(dados[:])     # adiciona a lista dados dentro da lista pessoas

print(pessoas)               # printa a lista pessoas

pessoas=[['pedro,25'],['maria',30],['jose,40']]   # cria 3 listas dentro da lista [pessoas]

print(pessoas[0][0])         # printa a lista do pedro com o nome do pedro
print(pessoas[1][1])         # printa a lista da maria com a idade [30] 
print(pessoas[1])            # printa [maria,30]

#=======================================================================================================#

teste=[]                     # cria uma lista vazia
teste.append('gustavo')      # adiciona 'gustavo a lista 
teste.append(40)             # adiciona 48 a lista 
galera=[]                    # cria uma lista vazia
galera.append(teste[:])      # galera recebe uma copia de teste 
teste[0]='maria'             # muda o nome de gustavo pra maria
teste[1]=22                  # muda a idade de 40 pra 22
galera.append(teste[:])      # lista galera recebe uma copia da lista teste modificada
print(galera)                # printa a copia original + a copia modificada

#=======================================================================================================#

galera=[['pedro,25'],['maria',30],['jose,40']]

for pessoa in galera:
    print(pessoa)            # printa uma lista com as pessoas e idades
    print(pessoa[0])         # printa apenas os nomes de tds pessoas da lista
    print(pessoa[1])         # printa a idade de todas pessoas da lista
    
#=======================================================================================================#

galera=[]                    # cria uma lista
dados=[]                     # cria uma lista para pegar os dados temporariamente
totalmaior = totalmenor=0
for cont in range (0,3):     
    dados.append(str(input('Nome: ')))      # le o nome e a idade e joga na lista dados
    dados.append(int(input('idade: ')))
    galera.append(dados[:])                 # faz uma copia de dados na lista galera 
    dados.clear()                           # limpa a lista dados
    
for pessoa in galera:                       # faz a checagem da lista galera
    if pessoa[1] >=21:                      # faz a comparacao da pessoa[1] ou seja a idade  nome[0] idade [1]
        print(f'{pessoa[0]} eh maior de idade')
        totalmaior+=1
    else:
        print(f'{pessoa[0]} eh menor de idade')
        totalmenor+=1
        
print(f'A quantidade de pessoas maiores foi {totalmaior}')
print(f'A quantidade de pessoas menores foi {totalmenor}')
    