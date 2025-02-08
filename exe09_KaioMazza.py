# 09 - Escreva um programa que peça ao usuario para inserir três números inteiros, some os dois primeiros e multiplique esse total pelo terceiro
# Exiba o resultado da operação com a seguinte mensagem: "O total é [?]"

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite mais um número inteiro:"))
num3 = int(input("Digite mais um número inteiro:"))

resultadoOperacao = (num1 + num2) * num3

print("O total é:", resultadoOperacao)