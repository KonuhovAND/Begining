# Напечатайте все трехзначные числа с заданной
# пользователем суммой цифр


def generate_numeber(number):
    for num in range(100, 1000):
        if number == (num % 10 + num // 10 - 9 * (num // 100)):
            print(num, end=" ")


def main():
    try:
        number = int(input("Enter number in range 1-27: "))
        if number < 1 or number > 27:
            raise ValueError("Enter valid number!")
        generate_numeber(number)
    except Exception as exc:
        print(exc, f"{number} is not in range [1,27]")


main()
