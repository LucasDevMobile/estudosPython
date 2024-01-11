#crie um programa q leia a idade e sexo de varias pessoas..a cada pessoa perguntar se continua ou nao.
#no final mostrar = qts pessoas tem mais de 18 ats homens foram cadastrados e qts mulheres tem menos de 20 anos

print('='*20)
print('CADASTRO DE PESSOAS')
print('='*20)

maior=0
homem=0
menor20=0

while True:
    idade=int(input('Qual a sua idade?'))
    
    if idade>18:
        maior+=1
    sexo=str(input('Qual o seu sexo? [M/F]')).upper()
    
    if sexo=='M':
        homem+=1
        
    if sexo=='F' and idade<20:
        menor20+=1
    
    continuar=str(input('Voce deseja continuar? [S/N]')).upper()
    
    if continuar=='N':
        break
print(f'Pessoas com mais de 18 anos= {maior}, Mulheres com menos de 20 anos= {menor20}, Total de homens= {homem}')