# crie um programa q leia um numero real qualquer e mostre na tela a sua porcao inteira
# exemplo: o numero 6.127 tem a parte inteira 6
import math

num=float(input('Digite um numero'))

print('O inteiro de {} e {} '.format(num,math.trunc(num)))  #exibe math.trunk de (num)
                                                            #tb se se usar (int) no lugar de math.trunk