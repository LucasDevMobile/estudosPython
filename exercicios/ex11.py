#faca um programa q leia a altura e largura de uma parede em metros,calcule sua area e a quantidade de tinta necessaria,cada lt de tinta pinta 2m2

p1=int(input('Qual a altura da parede? '))
p2=int(input('Qual a largura da parede? '))
area=(p1*p2)
print('A area da parede e {}'.format(area))
tinta=(area/2)
print('A quantidade de tinta necessaria sera {} litros'.format(tinta))
