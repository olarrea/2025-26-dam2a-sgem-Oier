info = input("Introduce una o varias palabras: ")
espacios = info.replace(" ", "")
if espacios.isalpha():
    resultado = sorted(espacios)
    print(resultado)
else:
    print("No es una entrada valida")