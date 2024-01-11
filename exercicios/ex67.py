while True:
    # Escolha o número para a tabuada
    numero = int(input("Qual tabuada voce deseja saber?: "))
    print('')
    
    if numero <0:                                                 # esse eh o loop principal soh eh interrompido caso o usuario digite numero negativo
        # Se o usuário digitar -1, sair do loop principal
        break

    # Inicializa o multiplicador
    multiplicador = 1

    while True:
        # Calcula e imprime o resultado
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")      # loop secundario executa tudo q esta dentro e para no multiplicador 11 pq a tabuada vai ate 10
        print('')                                               # esse break soh para o loop secundario, depois disso volta pro loop principal executando tudo novamente

        # Incrementa o multiplicador
        multiplicador += 1

        # Se o multiplicador atingir 11, saia do loop interno
        if multiplicador == 11:
            break
print('Obrigado por utilizar minha tabuada :)')
