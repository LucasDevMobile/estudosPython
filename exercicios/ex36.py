#escreva um programa que aprove o emprestimo bancario para comprar uma casa.O programa vai perguntar o valor da casa
#o salario do comprador e em qts anos ele vai pagar. Calcule o valor da prestacao mensal, sabendo que ele nao pode
#exceder 30% do salario,ou entao o emprestimo sera negado.

valorCasa=float(input('Qual o valor do imovel? '))
salario=float(input('Qual o seu salario? '))
parcelas=int(input('Em quantas parcelas voce deseja pagar? '))
prestacao=valorCasa/parcelas

if prestacao>salario *30/100:
    print('EMPRESTIMO NEGADO')
else:
    print('O valor do emprestimo sera {:.0f} parcelas de R$ {:.3f} '.format(parcelas,prestacao))
    


