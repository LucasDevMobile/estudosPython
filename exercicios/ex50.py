#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas dos pares,desconsiderar impar digitado

soma=0
cont=0
for c in range (1,7):
    
    num=int(input('Digite o {} valor:'.format(c)))
    if num % 2 ==0:
        soma += num   # soma=soma+num
        cont += 1     # cont= cont+1
    
print('Voce informou {} numeros pares e a soma foi {}'.format(cont,soma))

   
    

    
    


    
    
        
    
    
    
    
    
    


