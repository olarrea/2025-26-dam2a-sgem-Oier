entrada = input("Introduce capital, años, interes: ")
capital, años, interes = entrada.split(",")
capital = float(capital)
años = float(años)
interes = float(interes)
final = capital * (1 + interes) ** años
print(final)