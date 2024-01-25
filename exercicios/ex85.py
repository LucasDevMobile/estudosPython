#crie um programa digitar 7 valores e cadastrar em uma lista unica
#separar par e impar nessa lista
#mostrar valores em modo crescente

lista=[]
for c  in range(0,7):
    lista.append(int(input('Digite um valor:')))
    
for c in lista:
    if c % 2 == 0:
        lista=c
               
        print(f'Os valores pares sao {lista}')
for c in lista:
    if c %2 !=0:
        print(f'Os valores impares sao {c}')
        
        
        
    

    

    

    