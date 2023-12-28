# Crie um programa q leia o comprimento de tres retas e diga se pode ou nao formar um triangulo

r1= float(input('Primeiro segmento '))
r2= float(input('Segundo segmento '))
r3= float(input('Terceiro segmento '))

if r1< r2 + r3 and r2< r1 + r3 and r3< r1 + r2:
    print('Os segmentos podem formar um triangulo ')
else:
    print('Os segmentos nao podem formar um triangulo ')