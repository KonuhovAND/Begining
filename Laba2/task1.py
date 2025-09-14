# Напишите программу, которая бы по запросу
# пользователя вычисляла бы площадь и периметр круга,
# прямоугольника, треугольника и многоугольника по
# введённым с консоли данным (координаты вершин, радиус…).
import math
import colorama


def perimetr(*coordinates, radius: float = 0) -> float:
    if coordinates:  # многоугольник
        p = 0
        n = len(coordinates)
        for i in range(n):
            p += distance(coordinates[i], coordinates[(i + 1) % n])
        return p
    elif radius > 0:  # круг
        return 2 * math.pi * radius
    else:
        return 0


def distance(coordinate1, coordinate2):
    return (
        (coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2
    ) ** 0.5


def ploshad_treugolnika(p1, p2, p3):
    return 0.5 * abs(
        (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    )


def ploshad_mnogougolnika(*coordinates):
    """Формула шнуровки, работает для любых многоугольников)"""
    ploshad = 0
    n = len(coordinates)
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        ploshad += x1 * y2 - x2 * y1
    return abs(ploshad) / 2


def solver(*coordinates, raduis: float = 0):
    print()
    if len(coordinates) == 1:
        if raduis > 0:
            print(f"Circle area is {round(math.pi * raduis**2, 2)}")
            print(f"Circle perimeter is {round(perimetr(radius=raduis), 2)}")

    else:
        if len(coordinates) == 3:
            print(f"Triangle area is {ploshad_treugolnika(*coordinates)}")
            print(f"Triangle perimeter is {round(perimetr(*coordinates), 2)}")
        elif len(coordinates) >= 4:
            print(f"Polygon area is {ploshad_mnogougolnika(*coordinates)}")
            print(f"Polygon perimeter is {round(perimetr(*coordinates), 2)}")
        else:
            print(colorama.Back.RED + "Please enter more sides for shape")


def main():
    try:
        n = int(input("How many points? "))
        radius = float(input("Please,enter raduis: "))

        if n < 0:
            raise ValueError("Please, enter not empty amount of coordinates!")
        if radius < 0:
            raise ValueError("Please, enter positive raduis!")
    except ValueError as verr:
        print(verr)
        n = int(input("How many points? "))
        radius = float(input("Please,enter raduis"))

    coordinates = []
    for i in range(n):
        try:
            x, y = map(float, input(f"Enter x y for point {i + 1}: ").split())
        except ValueError:
            print("Please, enter not empty data")
            x, y = map(float, input(f"Enter x y for point {i + 1}: ").split())
        coordinates.append([x, y])

    radius = 0 if not radius else float(radius)
    solver(*coordinates, raduis=radius)


main()
