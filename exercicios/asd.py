while True:
    # Escolha o número para a tabuada
    numero = int(input("Digite o número para a tabuada (ou digite 0 para sair): "))

    if numero == 0:
        # Se o usuário digitar 0, sair do loop principal
        break

    # Inicializa o multiplicador
    multiplicador = 1

    while True:
        # Calcula e imprime o resultado
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")

        # Incrementa o multiplicador
        multiplicador += 1

        # Se o multiplicador atingir 11, saia do loop interno
        if multiplicador == 11:
            break
