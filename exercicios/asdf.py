temp=[]
lista=[]


for c  in range(0,7):
    temp.append(int(input('Digite um valor:')))
    
for c in temp:
    if c % 2 == 0:
        lista.append(c)
        lista.sort()
      
    

    
    
     
    

print(f'Os numeros pares sao [{lista}]')
print(f'Os numeros impares sao [{lista}]')
