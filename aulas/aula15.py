ont=0
soma=0

while True:    #enqunto for verdade
     num=int(input('Digite um numero inteiro:'))
     if num==999:   #so para o loop quando tiver um break
          break
     cont=cont+1
     soma=soma+num
print(f'A quantidade de numeros digitados foi {cont} e a soma entre eles foi {soma}')
   