bruce = {
    "nombre": "Bruce Banner",
    "trabajos": [80, 50, 40, 20],
    "test": [75, 75],
    "practicas": [78.20, 77.20]
}

harry = {
    "nombre": "Harry Potter",
    "trabajos": [82, 56, 44, 30],
    "test": [80, 78],
    "practicas": [67.90, 78.72]
}

hermione = {
    "nombre": "Hermione Ranger",
    "trabajos": [95, 100, 100, 100],
    "test": [99, 100],
    "practicas": [95.0, 80.5]
}

peter = {
    "nombre": "Peter Parker",
    "trabajos": [30, 10, 100, 100],
    "test": [90, 10],
    "practicas": [50.0, 50.0]
}

mario = {
    "nombre": "Super Mario",
    "trabajos": [77, 82, 23, 39],
    "test": [18, 60],
    "practicas": [80.6, 59.3]
}

alumnos = [bruce, harry, hermione, peter, mario]

filtrado = input("¿Desea filtrar por calificación (S/N)? ")

while filtrado.upper() != "N" and filtrado.upper() != "S":
    print("Respuesta no válida.")
    filtrado = input("¿Desea filtrar por calificación (S/N)? ")

if filtrado.upper() == "N":

    for alumno in alumnos:

        trabajos = sum(alumno["trabajos"]) / 4
        test = sum(alumno["test"]) / 2
        practicas = sum(alumno["practicas"]) / 2

        nota = (trabajos * 0.10) + (test * 0.50) + (practicas * 0.40)

        if nota >= 90:
            calificacion = "Sobresaliente"
        elif nota >= 70:
            calificacion = "Notable"
        elif nota >= 60:
            calificacion = "Bien"
        elif nota >= 50:
            calificacion = "Suficiente"
        else:
            calificacion = "Necesita mejorar"

        print("\n" + alumno["nombre"])
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("Nota media final para", alumno["nombre"], ":", nota)
        print("Calificación final de", alumno["nombre"], ":", calificacion)

else:

    print("Introduzca uno de los siguientes valores:")
    print("Sobresaliente - Notable - Bien - Suficiente - Necesita mejorar - Mostrar todo")

    valor = input("Valor: ").lower()

    lista_valores = ["sobresaliente", "notable", "bien", "suficiente", "necesita mejorar", "mostrar todo"]

    while valor not in lista_valores:
        print("Valor no válido, por favor introduzca uno de los siguientes valores:")
        print("Sobresaliente - Notable - Bien - Suficiente - Necesita mejorar - Mostrar todo")
        valor = input("Valor: ").lower()

    for alumno in alumnos:

        trabajos = sum(alumno["trabajos"]) / 4
        test = sum(alumno["test"]) / 2
        practicas = sum(alumno["practicas"]) / 2

        nota = (trabajos * 0.10) + (test * 0.50) + (practicas * 0.40)

        if nota >= 90:
            calificacion = "Sobresaliente"
        elif nota >= 70:
            calificacion = "Notable"
        elif nota >= 60:
            calificacion = "Bien"
        elif nota >= 50:
            calificacion = "Suficiente"
        else:
            calificacion = "Necesita mejorar"

        if valor == "mostrar todo":

            print(alumno["nombre"])
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Nota media final para", alumno["nombre"], ":", nota)
            print("Calificación final de", alumno["nombre"], ":", calificacion)

        elif calificacion.lower() == valor:

            print(alumno["nombre"])
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            print("Nota media final para", alumno["nombre"], ":", nota)
            print("Calificación final de", alumno["nombre"], ":", calificacion)
