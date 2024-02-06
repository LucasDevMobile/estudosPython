
#dicionarios sao declarados com {}

dados={'nome':'Lucas','idade':35,'sexo':'Masculino'} #item
       #"key" "value"
       
print(dados['nome'])  #vai imprimir Lucas

dados['peso'] = 87     # adiciona a key peso e valor 87 ao dicionario

dados['sexo']='Masculino'  # vai adicionar a key 'sexo' ao dicionario

dados['nome'] = 'arthur'   # troca o nome 

del dados['idade']       # remove a key idade da lista

print(dados.values())   # vai printar tos valores do dicionario (Lucas,35,Masculino)
print(dados.keys())     # vai printar tds as keys (nome,idade,sexo)
print(dados.items())    # vai printar a lista completa

# ================================================================================================

# USANDO FOR:

for k, v, in dados.items():   # Vai procurar por cada key e Value no dicionario ( items, dicionario completo) e printar
    print(f'O {k} eh {v}')    # o {k} nome eh {v} Lucas # O idade eh 35 # o sexo eh masculino
    
#=================================================================================================

# DICIONARIO DENTRO DA LISTA

locadora=[]                                                      # lista vazia
filme1={'titulo':'matrix','ano':1999,'diretor':'georgelucas'}   # dicionario filme 1
filme2={'titulo':'avengers','ano':2012,'diretor':'josswhedon'}  # dicionario filme 2

locadora.append(filme1)  # adiciona o dicionario 1 a lista
locadora.append(filme2)  # #adiciona o dicionario 2 a lista

locadora
#    __________________________________________________________________
#   |                               |                                 |
#   |'matrix'| 1999 | 'georgelucas' | 'avengers' | 2012 | 'josswhedon'|
#   | titulo | ano  |    diretor    |   titulo   |  ano | 'diretor'   |
#   |_______________________________|_________________________________|
# (indice 0 da lista)  0             (indice 1 da lista)  1

print(locadora[0]['ano'])   # vai printar o valor de (ano) do indice 0 da lista,ou seja, 1999
print(locadora)[1]['titulo']  # vai printar o valor de (titulo) do indice 1 da lista 'avengers

#=================================================================================================

# EXEMPLOS:

pessoas = {'nome':'Lucas','idade':35,'sexo':'M'}

print(pessoas)  #'nome':'Lucas','idade':35,'sexo':'M'

print(pessoas['nome'])  #'Lucas'

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')  # tem q usar aspas duplas e colchetes nos prints

print(pessoas.keys())      # printa tds as keys, nesse caso 'nome','idade','sexo'

print(pessoas.values())    # printa tds values, nesse caso 'Lucas',35,'M'

print(pessoas.items())     # printa o dict completo, 'nome':'Lucas','idade':35,'sexo':'M'

#===================================================================================================

for k in pessoas.keys():   # pra cada uma das keys
    print(k)               # nome,sexo,idade
    
for v in pessoas.values():  # pra cada valor
    print(v)                   # lucas,35,M
    
for k, v in pessoas.items():  # pra cada key e valor
    print(f'{k} = {v}')        # NOME=LUCAS   IDADE=35    SEXO=M
    
#====================================================================================================

# INPUT COM LISTA E DICIONARIO

estado={}
brasil=[]

for c in range(0,3):
    estado['uf']=str(input('unidade federativa: '))   # vai adicionar a key 'uf' ao dict estado 3x
    estado['sigla']=str(input('sigla do estado: '))   # vai adicionar a key 'sigla' ao dict estado 3x
    brasil.append(estado.copy())                      # adiciona o dict estado a lista brasil
    
    print(brasil) # [{'uf': 'franca', 'sigla': 'sp'}, {'uf': 'uberaba', 'sigla': 'mg'}, {'uf': 'rio de janeiro', 'sigla': 'rj'}]
    
for e in brasil:  # pra cada dicionario em brasil
    
    print(e)      # {'uf': 'franca', 'sigla': 'sp'}
                  # {'uf': 'uberaba', 'sigla': 'mg'}
                  # {'uf': 'rio de janeiro', 'sigla': 'rj'}
                  
# ex2

for e in brasil:
    for k, v in e.items():     # pra cada key e value no 'e' q sao os dict adicionados
        
        print(f'O campo {k} tem valor {v}')     #O campo uf tem valor franca
                                                #O campo sigla tem valor sp
                                                #O campo uf tem valor uberaba
                                                #O campo sigla tem valor mg
                                                #O campo uf tem valor rio de janeiro
                                                #O campo sigla tem valor rj
                                                
# ex3

for e in brasil:
    for v in e.values():      # pra cada value no e q sao os dicionarios
        print(v)              #sp
                              #uberaba
                              #mg
                              #rio de janeiro
                              #rj


