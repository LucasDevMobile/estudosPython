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