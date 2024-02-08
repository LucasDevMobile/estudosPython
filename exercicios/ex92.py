#crie um programa q leia nome,ano nascimento e carteira de trabalho e cadastreo os com idade em um dict
#se por acaso a ctps for diferente de zero,o dicionario recebera tambem o ano de contratacao e salario
#calcule alem da idade,com qts anos a pessoa vai se aposentar

from datetime import date

pessoa={}

pessoa['nome']= str(input('Digite seu nome:'))
pessoa['nascimento']= int(input('Digite o ano que voce nasceu:'))
pessoa['ctps']= int(input('Digite sua carteira de trabalho:'))

idade=date.today().year - pessoa["nascimento"]

pessoa['idade']=idade

if pessoa['ctps'] != 0:
    pessoa['Ano contratacao']=int(input('Digite o ano que foi contratado'))
    pessoa['salario']=float(input('Digite seu salario:'))
    
aposentadoria=pessoa["Ano contratacao"]+ 35 - date.today().year
    



print(f'{pessoa["nome"]} tem {idade} anos e vai se aposentar em {aposentadoria} anos ')
