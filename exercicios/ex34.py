# Crie um programa q pergunte o salario de um funcionario e calcule o valor do  seu aumento.
# Para salarios + 1250 o aumento eh 10%, para inferiores o aumento eh 15%

salario=int(input('Qual o seu salario? '))


aumento1=(salario*0.10)

aumento2=(salario*0.15)

if salario>=1250:
    print(salario+aumento1)

else:
    print(salario+aumento2)
    