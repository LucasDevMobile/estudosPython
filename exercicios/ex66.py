# crie um programa que leia varios numeros inteiros.O programa so vai parar quando o usuario digitar o valor 999,que eh a condicao de parada.
# no final mostre quantos numeros foram digitados e qual foi a soma entre eles,desconsiderando o flag (999)
cont=0
soma=0

while True:
     num=int(input('Digite um numero inteiro:'))
     if num==999:
          break
     cont=cont+1
     soma=soma+num
print(f'A quantidade de numeros digitados foi {cont} e a soma entre eles foi {soma}')
   