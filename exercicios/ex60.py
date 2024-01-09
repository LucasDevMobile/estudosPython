#faca um programa que leia um numero e mostre seu fatorial
#exemplo: 5! 5*4*3*2*1=120

numero = int(input("Digite um número para calcular o fatorial: "))

# Verificar se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    # Inicializar o resultado
    resultado = 1

    # Calcular o fatorial usando um loop while
    while numero > 1:
        resultado *= numero
        numero -= 1

    # Exibir o resultado
    print(f"{numero}! = {resultado}")
