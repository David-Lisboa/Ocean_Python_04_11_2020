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


#
# case = '-25'
#
# #   case = input("escolha um valor de 0 a 10")
# verificacao = str.isnumeric(case)
#
# if verificacao == True:
#     print("O número digitado foi {}".format(case))
# elif verificacao == False:
#     print("Digite apenas numeros!")

def is_number(num):
    """Testa se arg é um número."""
    try:
        # Tente converter a entrada.
        float(num)
        # Se for bem-sucedido, retorna verdadeiro.
        return True

    except:
        # Silenciosamente ignora qualquer exceção.
        pass
    # Se este ponto for alcançado, a entrada não é um número e a função
    # retorna falso
    return False

string_var = "raccoon ninja"
is_number(string_var)
print(f"{string_var}={is_number(string_var)} do tipo {type(string_var)}")
if is_number(string_var) == True:
    string_var = float(string_var)
    print(f"{string_var}={is_number(string_var)} do tipo {type(string_var)}")
else:
    print("Digite novamente")

string_var = "123"
is_number(string_var)
print(f"{string_var}={is_number(string_var)} do tipo {type(string_var)}")
if is_number(string_var) == True:
    string_var = float(string_var)
    print(f"{string_var}={is_number(string_var)} do tipo {type(string_var)}")
else:
    print("Digite novamente")

string_var = "-123"
is_number(string_var)
print(f"{string_var}={is_number(string_var)} do tipo {type(is_number(string_var))}")

string_var = "-1.23"
is_number(string_var)
print(f"{string_var}={is_number(string_var)} do tipo {type(is_number(string_var))}")

string_var = "1.23"
is_number(string_var)
print(f"{string_var}={is_number(string_var)} do tipo {type(is_number(string_var))}")
