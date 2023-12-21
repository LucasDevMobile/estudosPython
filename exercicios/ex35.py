# Crie um programa q leia o comprimento de tres retas e diga se pode ou nao formar um triangulo

a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

def verificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


# Verificação e exibição do resultado
if verificar_triangulo(a, b, c):
    print("É possível formar um triângulo com essas retas.")
else:
    print("Não é possível formar um triângulo com essas retas.")
