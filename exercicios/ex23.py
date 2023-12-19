#faca um programa q leia numeros de 0 a 9999 e mostre na tela cada um dos digitos separados
# exemplo: digite o numero 1834
#unidade4,dezena,3centena 8,milhar 1

numeros=input('digite um numero ')

unidade=numeros[3]
dezena = numeros[2]
centena = numeros[1]
milhar = numeros[0]
print ('unidade {} dezena {}centena {} milhar {}'.format(unidade,dezena,centena,milhar))

