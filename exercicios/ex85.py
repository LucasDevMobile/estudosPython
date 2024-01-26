#crie um programa digitar 7 valores e cadastrar em uma lista unica
#separar par e impar nessa lista
#mostrar valores em modo crescente

lista=[[],[]]
valore=0

for c in range(1,8):
    valor=int(input('Digite um valor: '))

    if valor % 2 ==0:
        lista[0].append(valor)

    else: lista[1].append(valor)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares foram {lista[0]}')
print(f'Os valores impares foram {lista[1]}')

        
               
          

    
        
        
    

    

    

    