#   Exercicio 1

contador = 1
while contador != 0:
    estilo = input("Informe o seu estilo: ").strip().lower() # Tira o espaço e coloca em minusculo

    if estilo == "medieval":
        print("espada")
        contador = 0
    elif estilo == "futurista":
        print("sabre de luz")
        contador = 0
    else:
        print("tente novamente")
