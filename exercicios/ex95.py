#crie um programa que gerencie um jogador.o programa va ler nome e qts partidas ele jogou
#qts gols na partida 1,2,3,4
#depois vai ler quantidade de gols em cada partida
#guarde em um dicionario incluindo total de gols feitos no campeonato

#{'nome':zico,'gols':[3,0,2,1,4],'total':10}

#o campo nome tem o valor zico
#o campo gols tem o valor [3,0,2,1,4]
#o campo total tem o valor 10

#o jogador zico jogou 5 partidas
#na partida 0 fez 3 gols
#na partida 1 fez 0 gols....etc

#perguntar se quer continuar (JOGADORES)
#cada jogador eh um dicionario,sao jogados em uma lista
#0 ronaldo [2,3,1] 6
#1 rivaldo [2,4,3] 9

# mostrar dados de qual jogador (999) para parar
# mostrar qts gols fez em cada jogo

desempenho = {}
time= []
gols=[]
gols2=[]

while True:

    desempenho ['nome']=str(input('Digite o nome do jogador:'))
    partidas=int(input('Digite a quantidade de partidas:'))

    for gol in range (partidas):
        
        gols.append(int(input(f'Digite a quantidade de gols na partida {gol} :')))
    print()
    
    desempenho['gols']=gols.copy()
    
    total=sum(gols)

    desempenho['total']=total
    gols2=gols.copy()
    gols.clear()

    time.append(desempenho.copy())
     
    continuar=str(input('Deseja continuar? S/N:')).upper()
    if continuar not in 'S':
        break
print()
print(f'Esse eh o time{time}')
print()

while True:
    jogador = input('De qual jogador voce deseja saber os dados? Digite 999 para parar: ')
    
    if jogador == '999':
        break

    for c in time:
        if c['nome'] == jogador:
            print(c)
            for k, v in enumerate(c['gols']):
                print(f'Na partida {k} {c["nome"]} fez {v} gols')

    
            
        
        
            







       
    
