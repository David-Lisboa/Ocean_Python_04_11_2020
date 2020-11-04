#   Logica Booleana

print('1 == 1:', 1 == 1)  # igual
print('1 != 1:', 1 != 1)  # igual
print('1 < 1:', 1 < 1)  # igual
print('1 <= 1:', 1 <= 1)  # igual
print('1 > 1:', 1 > 1)  # igual
print('1 >= 1:', 1 >= 1)  # igual

idade = 50

maior_idade = idade >= 18

print(5 + 15 == 20)

print("Rei" == "Arthur")
print("Rei" == "Rei")

print(1.0 == 1)  # true
print(1 == '1')  # true

idade = 30
maior_idade = idade >= 18
menor_idade = not maior_idade
print(idade, maior_idade, menor_idade)

#   IF e ELSE

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

