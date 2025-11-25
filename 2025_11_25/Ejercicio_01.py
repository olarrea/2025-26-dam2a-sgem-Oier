import random

rawStudentNames = ["Mikel", "IA_400", "Magnus", "Thor", "Terminator", "Spiderman",
                   "Yerai", "Carla", "Jokin", "Julen", "Xabier", "Eduardo", "Manuel",
                   "Yahya", "Oier", "Irene", "Rubén", "David", "Mamadi", "Ibón",
                   "Eneko", "Sugarev", "Luka", "Diego"]

num = input("Introduce un numero del 1 al 20: ")

while not num.isnumeric() or int(num) < 1 or int(num) > 20:
    print("El numero debe ser entre el 1 y el 20, y debe ser numerico.")
    num = input("Introduce un numero del 1 al 20: ")

numero = int(num)
alumnos_aleatorios = random.sample(rawStudentNames, numero)

for alumno in alumnos_aleatorios:
    print(alumno)
