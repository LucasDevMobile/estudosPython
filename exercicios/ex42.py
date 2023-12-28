#reforece o ex 35 mostrando q tipo de triangulo pode ser formado,equilatero=tds lados iguais,
# isosceles=2 lados iguais, escaleno=todos lados diferentes

r1= float(input('Primeiro segmento '))
r2= float(input('Segundo segmento '))
r3= float(input('Terceiro segmento '))

if r1< r2 + r3 and r2< r1 + r3 and r3< r1 + r2:
    print('Os segmentos podem formar um triangulo ',end='')   # end    mostra o proximo print na mesma linha
    if r1== r2 ==r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOCELES')
else:
    print('Os segmentos nao podem formar um triangulo ')