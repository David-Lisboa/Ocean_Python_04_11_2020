#   Logica Booleana

print('1 == 1:', 1 == 1)  # É igual a
print('1 != 1:', 1 != 1)  # Diferente de
print('1 < 0:', 1 < 0)  # Menor que
print('1 <= 0:', 1 <= 0)  # Menor que ou igual a
print('1 > 1:', 1 > 1)  # Maior que
print('1 >= 1:', 1 >= 1)  # Maior que ou igual a

idade = 50

maior_idade = idade >= 18

print(5 + 15 == 20)

print("Rei" == "Arthur")
print("Rei" == "Rei")

print(1 == 1)  # True
print(1.0 == 1)  # True
print(1 == "1")  # False
print(type(1.0), type(1), type("1"))

idade = 30
maior_idade = idade >= 18
menor_idade = not maior_idade
print(idade, maior_idade, menor_idade)

# Operador 'not' (em outras linguagens também é conhecido como ! (ponto de exclamação))
# A função dele é inverter o sinal de um booleano
# not True, transforma o True em False
# not False, transforma o False em True

print(not True)  # False
print(not False)  # True

# Operador and: É usado em comparações de booleanos
# Para que o resultado de uma operação com 'and' seja True, todos os lados precisam ser True

print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(True and True and True)  # True
print(True and True and False)  # False

print(not (True and False))  # True
print(not True and False)  # False
print(False == False)  # True
print(True and (True != False))
print((True and True) != False)

# Operador 'or' -> Apenas um dos lados precisa ser True

print(True or False)  # True
print(False or False)  # False
print(True or True)  # True

print(not False or False)  # True

print(not False and True or True)  # True
print(not False and False or True)  # True

print(not True and False or True)  # True
print(not True and (False or True))  # False

# if: representa 'se'. Se algo for igual a True
# elif: el representa 'caso contrário', juntando com o 'if', representa 'caso contrário, se'.
# Ele ocorre quando a condição do if for igual a False, e a condição do 'elif' for igual a True
# else: representa 'caso contrário', ou seja, quando todos as condições de if/elif anteriores não ocorreram

# O if é o único que pode ser declarado sozinho
# Todos os outros precisam vir na sequência e eles são opcionais

if True:
    print("Esse if será lido.")

if False:
    print("Esse if nunca será lido.")

if True:
    print("esse if sera lido")
else:
    print("esse if não sera lido")

if False:
    print("esse if nunca sera lido")
elif True:
    print("esse elif sera lido")
else:
    print("esse if não sera lido")

idade = 10
maior_idade = idade >= 18
print(idade, maior_idade, menor_idade)

if maior_idade:
    print("A pessoa é maior idade.")
else:
    print("A pessoa é menor de idade.\n")

sexo = 'feminino'
idade = 30

maior_idade = idade >= 18
menor_idade = not maior_idade

print(idade, type(idade), maior_idade, type(maior_idade))

if maior_idade:
    print("A pessoa é maior de idade.")
elif menor_idade:
    print("A pessoa é menor de idade.")

if menor_idade:
    print("If separado, apenas para os casos em que a pessoa é menor de idade")

if not maior_idade:
    print("Menor de idade")

if sexo == 'feminino' and maior_idade:
    print("Essa pessoa é do sexo feminino e é maior de idade.")
