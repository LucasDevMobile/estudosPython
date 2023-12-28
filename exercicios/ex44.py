#escreva um programa que calcule o valor a ser pago por um produto considerando seu preco normal e condicao pagamento
#a vista dinheiro/cheque=10% desconto
#a vista cartao=5% desconto
#em ate 2x cartao= preco normal
#3x ou mais  no cartao= 20% juros

produto= float(input('Qual o valor do produto? '))
forma=int(input("""Qual a forma de pagamento?
                  
[1] Para dinheiro ou cheque a vista
[2] Para cartao a vista
[3] Para parcelar em 2x no cartao
[4] Para parcelar em 3x ou mais no cartao: """))




if forma==1:
    f1=produto-(produto*10)/100
    print('O valor total sera R$ {}'.format(f1))

elif forma==2:
    f2=produto-(produto*5)/100
    print('O valor total sera R$ {}'.format(f2))

elif forma==3:
    f3=produto/2
    print('O valor total sera 2 parcelas de {} reais'.format(f3))

elif forma==4:
    parcelas=int(input('Em quantas vezes voce vai dividir? '))
    f4=(produto/parcelas)+(produto*20)/100/parcelas
    print('O Valor total sera {} parcelas de R$ {}'.format(parcelas,f4))




    
    


