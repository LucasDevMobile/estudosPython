estado={}
brasil=[]

for c in range(0,3):
    estado['uf']=str(input('unidade federativa: '))   # vai adicionar uf ao dict estado 3x
    estado['sigla']=str(input('sigla do estado: '))   # vai adicionar sigla ao dict estado 3x
    brasil.append(estado.copy())                      # adiciona o dict estado a lista brasil
    
for e in brasil:
    for v in e.values():      # pra cada value no e q sao os dicionarios
        print(v)
