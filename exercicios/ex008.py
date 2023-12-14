#escreva um programa q leia um valor em metros,e o exiba convertido em centimetros e milimetros

medida=int(input('Qual a medida?'))
cent=(medida*100)
mili=(medida*1000)
print('O valor em centimetros e {},o valor em milimetros e {}'.format(cent,mili))