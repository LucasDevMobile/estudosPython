#crie um programa para inserir 5 valores em ordem

lista=[]

valor=int(input('Digite um valor:'))
lista.append(valor)
valor=int(input('Digite um valor:'))
lista.append(valor)

valor=int(input('Digite um valor:'))

if valor < max(lista) in lista:
    lista.insert(0,valor)
    
print(lista)