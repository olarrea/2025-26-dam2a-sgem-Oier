class Rectangle:
    def __init__(self, x, y, width, height):

        if width < 0 or height < 0 or x < 0 or y < 0:
            print("No se pueden pasar valores negativos")
            exit()

        self.x = x
        self.y = y
        self.width = width
        self.height = height

def intersecting(r1, r2):

    if r1.x + r1.width < r2.x:
        return False

    if r2.x + r2.width < r1.x:
        return False

    if r1.y + r1.height < r2.y:
        return False

    if r2.y + r2.height < r1.y:
        return False

    return True


a = Rectangle(10, 20, 100, 20)
b = Rectangle(10, 40, 15, 20)
c = Rectangle(50, 50, 20, 30)

print(intersecting(a, b))
print(intersecting(a, c))
print(intersecting(b, c))
