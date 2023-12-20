# Exemplo 1
"""nome=str(input('Digite seu nome ')).strip()
if nome.upper() == 'LUCAS':
    print('Que nome lindo')
print('Bom dia {}'.format(nome))"""

#Exemplo 2
nota1=float(input('Digite sua nota: '))
nota2=float(input('Digite sua segunda nota: '))
media=(nota1+nota2)/2
print('Sua media foi {:.1f}'.format(media))

if media>=6:
    print('Sua nota esta boa')
else:
    print('Sua nota esta ruim')

