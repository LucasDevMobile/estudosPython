# crie um programa q leia o comprimento do cateto adjacente de um triangulo retangulo,calcule e mostre o comprimento da hipotenusa

co=float(input('Medida do cateto oposto'))
ca=float(input('Medida do cateto adjacente'))
hip= (co ** 2 + ca ** 2) **((1/2))      # ou hip= math.hypot(co,ca) hypote calcula a
print('A medida da hipotenusa eh {:.2f} centimetros '.format(hip))