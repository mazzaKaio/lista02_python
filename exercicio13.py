# 13 - Escreva um programa que solicite um determinado número de dias, em seguida exiba o quanto estes dias equivalem em horas, minutos e segundos

diasDigitados = int(input("Insira um determinado número de dias:"))

horas = int(diasDigitados * 24)
minutos = int(diasDigitados * 1440)
segundos = int(diasDigitados * 86400)

print("Em", diasDigitados, "dias há:")
print(horas, "horas")
print(minutos, "minutos")
print(segundos, "segundos")