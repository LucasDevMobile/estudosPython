#faca um programa q leia a frase pelo teclado e mostre:
#quantas vezes aparece a letra "a"
#em q posicao ela aparece a primeira vez
#em q posicao ela aparece a ultima vez

frase= input('Digite uma frase ')
qtd=frase.count('a')
p1=frase.find('a')+1
p2=frase.rfind('a')+1
print ('A letra A aparece {} vezes '.format(qtd))
print('A posicao q ela aparece a primeira vez e {} '.format(p1))
print('A posicao q ela aparece a ultima vez e {} '.format(p2))

