"""
Exercício 13

Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.
Dificuldade: Principiante
1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão
escolhida é realizada.
3 - Se C é a temperatura em Celsius e F em farenheit, as fórmulas de conversão são:
C = 5 * (F - 32) / 9
F = (9 * C / 5) + 32
"""

def cls():
    print("\n" * 100)


def tipo_numerico(num):
    try:
        float(num)
        return True  # Se for bem-sucedido, retorna verdadeiro.
    except:
        pass  # Silenciosamente ignora qualquer exceção.
    return False  # Se este ponto for alcançado, a entrada não é um número e a função retorna falso


def Temperatura():
    temperatura = str(input("\n\nDigite a temperatura:"))

    if tipo_numerico(temperatura) == True:
        temperatura = float(temperatura)
        print("temperatura", type(temperatura))
        return float(temperatura)
    else:
        print("ERRO valor invalido!!\n")
        Temperatura()


def escolha():
    lista_opcoes = ['1', '2']
    escolhido = str(input("\nDigite a opção 1 ou 2 \n\t1 - De Celsius para Farenheit\n\t2 - De Farenheit para Celsius\nDigite sua opção:"))
    if (tipo_numerico(escolhido) == True) and (escolhido in lista_opcoes):
        escolhido = float(escolhido)
        return escolhido
    else:
        print("\n\tERRO valor invalido!!\n")
        escolha()


def Farenheit(Cel):
    F = (9 * Cel / 5) + 32
    return F


def Celsius(Fare):
    C = 5 * (Fare - 32) / 9
    return C


def conversao(temperatura, escolha_temperatura):
    if escolha_temperatura == 1:
        converter = Farenheit(temperatura)
    else:
        converter = Celsius(temperatura)
    return converter


def imprimir(temperatura, escolha_temperatura, conversao):
    if escolha_temperatura == 1:
        print(f"\n\nA temperatura {temperatura}ºC é {conversao}ºF")
    else:
        print(f"\n\nA temperatura {temperatura}ºF é {conversao}ºC")


def converter_temperatura():
    temperatura = Temperatura()
    print("temperatura_2", type(temperatura))

    escolha_temperatura = escolha()
    print("escolha_temperatura", type(escolha_temperatura))

    convertido = conversao(temperatura, escolha_temperatura)
    imprimir(temperatura, escolha_temperatura, convertido)


contador = 2
while contador != 1:
    print("\nDeseja converter a temperatura ?\n\tDigite uma das opções:\n\t 1 - sair\n\t 2 - converter ")
    contador = str(input("Digite a sua opção: "))
    op = ['1', '2']

    if tipo_numerico(contador) == True and contador in op:
        contador = float(contador)
    else:
        print("\nERRO valor invalido!!\n")
        contador = 0

    if contador == 2:
        cls()
        converter_temperatura()
    elif contador == 1:
        print("\n", "\tOBRIGADO!! " * 6, "\n", "\tOBRIGADO!! " * 6, "\n", "\tOBRIGADO!! " * 6)
