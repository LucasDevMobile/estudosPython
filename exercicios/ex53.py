#crie um programa q leia uma frase e diga se ela eh palindromo,desconsiderando espacos
#exemplo: apos a sopa, a sacada da casa, a torre da derrota,o lobo ama o bolo,anotaram a data da maratona 

frase=str(input('Digite uma frase:')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print(junto,inverso)
if inverso == junto:
    print('Temos um palindromo')
else:print('Nao eh um palindromo')