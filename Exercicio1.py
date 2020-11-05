#   Exercicio 1
"""
- Escreva um programa que receba uma string digitada pelo usuário e caso a string seja igual a “medieval”,
exiba no console: “espada”;
- Caso contrário, se a string for igual a “futurista”, exiba no console: “sabre de luz”; - Caso contrário,
exiba no console: “Tente novamente.”.
"""

contador = 1
while contador != 0:
    estilo = input("Informe o seu estilo: ").strip().lower()  # Tira o espaço e coloca em minusculo

    if estilo == "medieval":
        print("espada")
        contador = 0
    elif estilo == "futurista":
        print("sabre de luz")
        contador = 0
    else:
        print("tente novamente")
