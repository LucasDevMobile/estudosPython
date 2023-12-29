#faca um programa q calcule a soma entre tds numeros impares multiplos de 3 entre 1 e 500
soma=0
for c in range(1,499,3):

    print(c+2)
    
    soma=soma+c
print('A soma dos numeros eh {}'.format(soma))