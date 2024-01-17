#  tuplas sao variaveis que recebem mais de um atributo

lanche= ('hamburguer','suco','sorvete','cafe')

print(lanche[2])   # vai fazer o print do item 3 da tupla (comeca no 0)

print(lanche[1:3]) # printa suco e sorvete (ignora o 3)

print(lanche[-1])  # printa cafe (-1 eh o ultimo, -2 seria sorvete)

print(lanche[1:])  # printa o elemento 1 ate o final

print(sorted(lanche)) # printa em ordem alfabetica

print(lanche[:2])  # printa do inicio ao elemento 3

print (len(lanche)) # vai printar quantos itens tem na tupla


for comida in lanche:
    print(f'Eu vou comer {comida}') #printa cada item da tupla em uma linha
    
for cont in range (0,len(lanche)):  # printa mostrando a posicao de cada item
    print(f'Eu vou comer {lanche[cont]} na posicao {cont}') 
    
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}') # mesma coisa do ex acima mas usando enumerate
    

a = (2,5,4)
b = (5,8,1,2)
c = a+b

print(c)  # nao vai somar os numeros,o resultado sera 2,5,4,5,8,1,2

print(c.count(5)) #conta qts vezes aparece o 5

print(c.index8)  #mostra a posicao q esta o 8 (em caso de de numero repetido mostra sempre o primeiro)

print(c.index(5,1)) #mostra a posicao do primeiro 5 a partir da posicao 1

pessoa=('lucas',35,87)   #tuplas aceitam dados diferentes juntos como numeros e strings