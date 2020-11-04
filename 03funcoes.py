# Função -> Pegar um trecho de código e dar um nome para ele
# Esse trecho de código só será executado quando chamarmos esse nome

# Para criar uma função, usamos a declaração 'def nome_funcao():'

# Todo o conteúdo que tiver dentro da função, terá um espaçamento adicional

def exibir_numero():
    print("Exibir numero")
    print("Fim da função")


exibir_numero()


# def jogo(estilo):
#     contador = 1
#     while contador != 0:
#
#         if estilo == "medieval":
#             print("espada")
#             contador = 0
#         elif estilo == "futurista":
#             print("sabre de luz")
#             contador = 0
#         else:
#             print("tente novamente")
#
#
# estilo = input("Informe o seu estilo: ").strip().lower()  # Tira o espaço e coloca em minusculo)
# jogo(estilo)
#####################################################################################################################
################################ FUNÇÂO RECURSIVA ###################################################################
# #   função recursiva
# def jogo():
#     estilo = input("Informe o seu estilo: ").strip().lower()  # Tira o espaço e coloca em minusculo)
#
#     if estilo == "medieval":
#         print("espada")
#     elif estilo == "futurista":
#         print("sabre de luz")
#     else:
#         print("tente novamente")
#         jogo()
#
#
# jogo()
#####################################################################################################################
################################ FUNÇÂO QUE USA PARTE DA PALAVRA ###################################################################
def jogar():  # Declara a função jogar, mas não a executa
    escolha_usuario = input("Você é uma pessoa futurista ou tá mais pro medieval? ").strip().lower()

    if 'medieval' in escolha_usuario:
        print("Você recebeu uma espada!")
    elif 'futur' in escolha_usuario:
        print("Você recebeu um sabre de luz!")
    else:
        print("Tente novamente.")
        print("estou dentro do else")

    print("estou fora do else, mas dentro da função (def)")


print("estou fora da função (def)")

print("Jogo 1")
jogar()  # Executa a função jogar()

print("Jogo 2")
jogar()


def somar_numeros(a, b):
    resultado = a + b
    return resultado


a = float(input("Informe o valor 1: "))
b = float(input("Informe o valor 2: "))
print(f"a soma de {a} + {b} é {somar_numeros(a, b)}")


def pegar_numero(texto):
    numero = float(input(texto))
    return numero


def somar_numeros2(a, b):
    resultado = a + b
    return resultado


a = pegar_numero("Digite o valor de A: ")
b = pegar_numero("Digite o valor de B: ")

resultado = somar_numeros2(a, b)

print(f"O valor de {a} + {b} = {resultado}")


def jogar():
    print("Seja bem-vindo(a) ao jogo.")
    escolha = pegar_numero("Digite um número: ")
    escolha2 = pegar_numero("Digite um número 2: ")
    print(f"Você escolheu o número: {escolha}")
    print(f"{escolha} + {escolha2} = {escolha + escolha2}")


jogar()


# Parâmetros opcionais

def teste(a, c, b=30):  # argumentos pre declarados devem vir no final
    print(a + b + c)


teste(10, 20)
teste(10, 20, 50)


def somar_numeros3(numero1, numero2, exibir=False):
    resultado = numero1 + numero2

    if exibir:
        print(f"O resultado de {numero1} + {numero2} é {resultado}.")

    return resultado  # Return encerra a função, não podemos colocar nada embaixo dele


somar_numeros3(5, 9, True)
somar_numeros3(10, 20)

print("Fim do bloco")
