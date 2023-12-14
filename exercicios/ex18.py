#crie um programa q leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente desses angulos
import math
an=float (input('Digite o angulo'))
seno= math.sin(math.radians(an))
print ('O angulo de {} tem o seno de {:.2f}'.format(an,seno))
cosseno=math.cos(math.radians(an))
print ('O angulo de {} tem o cosseno de {:.2f}'.format(an,cosseno))
tangente=math.tan(math.radians(an))
print ('O angulo de {} tem o tangente de {:.2f}'.format(an,tangente))


