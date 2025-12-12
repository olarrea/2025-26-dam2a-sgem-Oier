alumnos = [
    {
        "nombre": "Bruce Banner",
        "trabajos": [80, 50, 40, 20],
        "test": [75, 75],
        "practicas": [78.20, 77.20]
    },
    {
        "nombre": "Harry Potter",
        "trabajos": [82, 56, 44, 30],
        "test": [80, 78],
        "practicas": [67.90, 78.72]
    },
    {
        "nombre": "Hermione Ranger",
        "trabajos": [95, 100, 100, 100],
        "test": [99, 100],
        "practicas": [95.0, 80.5]
    },
    {
        "nombre": "Peter Parker",
        "trabajos": [30, 10, 100, 100],
        "test": [90, 10],
        "practicas": [50.0, 50.0]
    },
    {
        "nombre": "Super Mario",
        "trabajos": [77, 82, 23, 39],
        "test": [18, 60],
        "practicas": [80.6, 59.3]
    }
]

def calcular_nota(alumno):
    trabajos = sum(alumno["trabajos"]) / len(alumno["trabajos"])
    test = sum(alumno["test"]) / len(alumno["test"])
    practicas = sum(alumno["practicas"]) / len(alumno["practicas"])

    return trabajos * 0.10 + test * 0.50 + practicas * 0.40


def obtener_calificacion(nota):
    if nota >= 90:
        return "Sobresaliente"
    elif nota >= 70:
        return "Notable"
    elif nota >= 60:
        return "Bien"
    elif nota >= 50:
        return "Suficiente"
    else:
        return "Necesita mejorar"


def mostrar_alumno(alumno, nota, calificacion):
    print(f"\n{alumno['nombre']}")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print(f"Nota media final: {nota:.2f}")
    print(f"Calificación final: {calificacion}")

filtrado = input("¿Desea filtrar por calificación (S/N)? ").upper()

while filtrado not in ("S", "N"):
    filtrado = input("Respuesta no válida. ¿Desea filtrar por calificación (S/N)? ").upper()

if filtrado == "S":
    opciones = [
        "sobresaliente",
        "notable",
        "bien",
        "suficiente",
        "necesita mejorar",
        "mostrar todo"
    ]

    print("Opciones:", " - ".join(opciones).title())
    filtro = input("Valor: ").lower()

    while filtro not in opciones:
        filtro = input("Valor no válido. Introduzca uno correcto: ").lower()
else:
    filtro = "mostrar todo"

for alumno in alumnos:
    nota = calcular_nota(alumno)
    calificacion = obtener_calificacion(nota)

    if filtro == "mostrar todo" or calificacion.lower() == filtro:
        mostrar_alumno(alumno, nota, calificacion)
