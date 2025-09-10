#  Решите квадратное уравнение вида ax² + bx + c = 0,
# где коэффициенты a, b и c вводятся пользователем.
# Выведите корни или сообщение, что их нет.


def solver(a, b, c):
    D = b**2 - 4 * a * c
    if D < 0:
        print("You enter wrong 'a', 'b','c'. Please enter correct data")
        a = float(input('Enter first value for "a": '))
        b = float(input('Enter second value for "b": '))
        c = float(input('Enter third value for "c": '))

    elif D == 0:
        print("First and Second X for that is:" - b / (2 * a))
    else:
        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)
        print(f"First X: {x1}, Second X: {x2}")


def main():
    try:
        print("Enter values for that: ax² + bx + c = 0")
        a = float(input('Enter first value for "a": '))
        b = float(input('Enter second value for "b": '))
        c = float(input('Enter third value for "c": '))
    except ValueError as verr:
        print(verr)
    else:
        solver(a = a,b = b,c = c)



main()