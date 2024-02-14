#crie um programa q leia nome,sexo,idade pergunte se quer continuar
#guardar cada pessoa em um dict e os dict em uma lista
#qts pessoas cadastradas
#media de idade
#lista com mulheres
#lista com idade acima da media

cadastro=[]
pessoas={}
mulheres=[]
idade=[]
acima=[]

while True:
    
    pessoas ['nome']=str(input('Digite seu nome:'))
    
    pessoas ['sexo']=str(input('Digite seu sexo (M/F)')).upper()
    while pessoas['sexo'] not in 'M' 'F':
        print('ERRO, digite M ou F para o sexo')
        pessoas ['sexo']=str(input('Digite seu sexo (M/F)')).upper()
          
    pessoas ['idade']=int(input('Digite sua idade:'))
          
    cadastro.append(pessoas.copy())
    
    idade.append(pessoas['idade'])
     
    
    if pessoas['sexo']=='F':
        mulheres.append(pessoas.copy())
    
    continuar=str(input('Deseja continuar? S/N:')).upper()
    if continuar not in 'S':
        break
 
media=sum(idade)/(len(cadastro))

for pessoa in cadastro:
    if pessoa['idade'] > media:
        acima.append(pessoa)
   
print()   
print(f'Lista de pessoas cadastradas {cadastro}')
print() 
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas')
print() 
print(f'Essa eh a lista das mulheres {mulheres}')
print()
print(f'A media de idade foi {media} anos')
print()
print(f'As pessoas acima da media de idade sao {acima}')
