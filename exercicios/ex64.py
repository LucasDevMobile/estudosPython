#crie um programa q leia varios numeros inteiros.O programa so vai parar quando o usuario digitar o valor 999
#que eh a condicao de parada.No final mostre qts numeros foram digitados e qual foi a soma entre eles

num=int(input('Digite um numero inteiro: '))
cont=0
sum=num

while num != 999:
    num=int(input('Digite um numero inteiro: '))
    cont=cont+1
    sum=sum+num
print('A quantidade de numeros digitados foi {} e a soma entre eles eh {} '.format(cont,sum-999))   