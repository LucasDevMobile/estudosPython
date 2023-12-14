import math
# Quando se importa a biblioteca inteira,eh necessario usar (math.sqrt) no codigo

#caso importe uma parte,pode se usar apenas o (sqrt)

num=int(input('Digite um numero '))
raiz= math.sqrt(num)                                       # Usa o comando sqrt (raiz quadrada) da biblioteca math q foi importada
print('A raiza de {} e igual a {:.0f}'.format(num,raiz))   # O comando :.0f formata o resultado no caso com uma casa decimal