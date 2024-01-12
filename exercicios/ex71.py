# criacao de caixa eletronico

print('='*30)
print('{:^30}'.format('BANCO LUCAS'))
print('='*30)
valor=int(input('Qual valor deseja sacar:'))

total=valor
cedula=50
totced=0

while True:
    if total>=cedula:   #se o valor digitado for maior q 50 faz valor-50 e conta uma vez pra cada -50 possivel
        total-=cedula
        totced+=1
    else:
        if totced>0:    
            print(f'Total de {totced} cedulas de R${cedula}')     #printa quando acabar o valor
            
        if cedula==50:       
            cedula=20   #faz a mesma conta acima porem diminuindo o valor da cedula na medida q n da mais pra dividir
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        totced=0
        if total==0:
            break
        
print('='*50)
print('{:^50}'.format('OBRIGADO POR UTILIZAR NOSSO CAIXA ELETRONICO'))
print('='*50)


    



