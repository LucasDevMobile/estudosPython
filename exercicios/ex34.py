# Crie um programa q pergunte o salario de um funcionario e calcule o valor do  seu aumento.
# Para salarios + 1250 o aumento eh 10%, para inferiores o aumento eh 15%

"""salario=float(input('Qual o seu salario? '))


aumento1=(salario*0.10)

aumento2=(salario*0.15)

if salario>=1250:
    print(salario+aumento1)

else:
    print(salario+aumento2)"""
    
# Outra forma

salario=int(input('Qual o seu salario? '))

if salario<=1250:
    novo=salario + (salario* 15 / 100)
else:
    novo=salario+ (salario* 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,novo))


    