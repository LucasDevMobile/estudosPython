nome = str(input('Qual seu nome? '))
if nome == 'Lucas':
    print('Que nome bonito')
    
elif nome== 'ana' or nome == 'maria' or nome == 'pedro':
    print('nome maravilhoso')
    
elif nome in 'junior larissa noah danilo':
    print('nome comum no brasil')
    
else:
    print('seu nome eh normal')
print('Tenha um bom dia {}'.format(nome))