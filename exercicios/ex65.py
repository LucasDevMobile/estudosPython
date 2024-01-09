#crie um programa q leia varios numeros inteiros,no final mostre a media entre eles e qual maior e menor
#o programa deve perguntar se o usuario quer ou nao digitar mais numeros

cont = 0
soma = 0

while True:
    num = int(input('Digite um numero inteiro: '))
    cont += 1
    soma += num
    
    num2 = int(input('Você deseja continuar? Digite 1 para sim e 2 para não: '))
    
    if num2 != 1:
        break

media = soma / cont
print(f'A média dos números digitados é: {media}')



  
   

    
   
    
    
    
    