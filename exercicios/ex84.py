# crie um programa q leia nome e peso de varias pessoas e guarde em uma lista
#qts pessoas foram cadastradas
#mais pesadas
#mais leves


temp=[]
princ=[]
maior = menor = 0

while True:
    temp.append(str(input('Digite seu nome:')))
    temp.append(float(input('Digite seu peso:')))
    
    if len(princ)==0:                                #ele vai ser = 0 pq ainda ninguem esta cadastrado    
        maior=menor=temp[1]                          #temp[1] peso, se torna o maior e eo menor
    else:
        if temp[1] > maior:
            maior=temp[1]
        if temp[1]< menor:
            menor=temp[1] 
            
    princ.append(temp[:])
    temp.clear()
    
    continuar = str(input('Você deseja continuar? [S/N] ')).upper()
    if continuar not in ('S'):
        break   
    
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')


for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
        
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')  
      
for p in princ:
    if p[1]==menor:
        print(f'[{p[0]}] ',end='')
    
    


          
        
    
    
    
    
    


