#crie um programa q leia varios numeros inteiros,no final mostre a media entre eles e qual maior e menor
#o programa deve perguntar se o usuario quer ou nao digitar mais numeros

resposta='S'
soma=0
quantidade=0
media=0
maior=0
menor=0

while resposta in 'Ss':
    num=int(input('Digite um numero:'))
    soma=soma+num
    quantidade=quantidade+1
    if quantidade==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num < menor:
            menor=num
    
    resposta= str(input('Quer continuar? [S/N] ')).upper().strip() [0]
media=soma/num
print('Voce digitou {} numeros e a media foi {}'.format(quantidade,media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior,menor))

  
   

    
   
    
    
    
    