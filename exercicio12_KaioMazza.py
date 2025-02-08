# 12 - Escreva um programa que pergunte o valor total da conta, em seguida pergunte quantos clientes existem, divida a conta pelos clientes
# e exiba o quanto cada cliente deve pagar, seguida da mensagem "Cada cliente deve pagar: [?]"

totalConta = float(input("Digite quantos reais(R$) deu a conta: "))
totalClientes = int(input("Digite em quantos clientes vão ser dividida a conta: "))

divisao = float(totalConta / totalClientes)

print("Cada cliente deverá pagar", divisao, "reais(R$)")