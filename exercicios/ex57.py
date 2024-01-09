#faca um programa q leia o sexo de uma pessoa mas so aceita M ou F.caso errado peca digitacao ate o valor correto

sexo=str(input('Qual o seu sexo? ')).upper()

while sexo!= 'F' and sexo != 'M':
    print('Digite uma opcao valida : ')
    sexo=str(input('Qual o seu sexo? ')).upper()
M='Masculino'
F='Feminino'
if sexo=='M':
    print('Obrigado, voce eh do sexo {}'.format(M))
else:
    print('Obrigado, voce eh do sexo {}'.format(F))

