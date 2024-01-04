#faca um programa q calcule a soma entre tds numeros impares multiplos de 3 entre 1 e 500
soma=0
cont=0
for c in range(1,501,2):
    if c % 3==0:
        soma=soma+c
        cont=cont+1

print('A soma de todos os {} valores solicitados eh {}'.format(cont,soma))