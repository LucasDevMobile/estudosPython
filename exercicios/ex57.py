#faca um programa q leia o sexo de uma pessoa mas so aceita M ou F.caso errado peca digitacao ate o valor correto

sexo=str(input('Qual o seu sexo? M/F ')).upper() [0].strip   #pega apenas a primeira letra

while sexo!= 'F' and sexo != 'M':   #pode se usar while sexo not in 'mMfF'
    print('Digite uma opcao valida : ')
    sexo=str(input('Qual o seu sexo? ')).upper()
M='Masculino'
F='Feminino'
if sexo=='M':
    print('Obrigado, voce eh do sexo {}'.format(M))
else:
    print('Obrigado, voce eh do sexo {}'.format(F))

