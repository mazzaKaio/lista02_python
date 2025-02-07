# 10 - Escreva um programa que pergunte quantos pedaços o bolo tem, em seguida pergunte ao usuario quantos pedaços ele comeu, calcule quantos pedaços ainda tem e exiba
# o resultado com uma mensagem de livre escolha

pedacosBolo = int(input("Digite quantos pedaços tem o bolo:"))
pedacosComidos = int(input("Digite quantos pedaços você comeu:"))

pedacosRestantes = pedacosBolo - pedacosComidos

print("O bolo tem:", pedacosBolo, "pedaços")
print("Você comeu:", pedacosComidos, "pedaços")
print("Ainda restam:", pedacosRestantes, "pedaços do bolo")