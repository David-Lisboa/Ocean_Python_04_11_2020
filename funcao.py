# Exercício 2: "Quem é você?"
"""
Nome: Input de Informações
Objetivo: Receber dados do usuário, trabalhar com os valores e exibir para o usuário.
Dificuldade: Principiante
1 - Crie um programa que receba do usuário seu nome, idade e gênero;
2 - Exiba na tela seguinte mensagem: "Olá, {nome}, você possui {idade} anos de idade e é do gênero {genero}.";
3 - Exiba também: "Já pensou no que você fará no seu aniversário de {idade + 1} anos?.".

Adicionando uma pimentinha extra: "Se o usuário digitar idade 1, exiba apenas "ano" em vez de "anos".
"""

nome = input("Digite o seu nome: ").title()
idade = int(input("Digite a sua idade: "))
genero = input("Digite o seu genero: ").title()

if idade < 2:
    ano = "ano"
else:
    ano = "anos"

print(f"Olá {nome}, você possui {idade} {ano} e é do genero {genero}.")
print(f"Já pensou no que você fara no seu aniversario de {idade+1} anos?")