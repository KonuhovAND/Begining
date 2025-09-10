#  Пользователь вводит с консоли три числа: размер
# вклада, процентную ставку и количество лет, на которое
# рассчитан вклад. Выведите на консоль таблицу в формате «год
# - сумма», которая отображала бы рост вклада по годам.


def is_item_less_than_zero(item, name):
    if item <= 0:
        raise ValueError(f"{name.capitalize()} is less than 0, enter positive {name}")


def main():
    try:
        print("3.5 years = 3 years")
        print("4.93 years = 4 years")

        value = float(input("Enter amount of money u want to put(more than 0): "))
        is_item_less_than_zero(value, "value")

        percent = float(input("Enter percent(more than 0): "))
        is_item_less_than_zero(percent, "percent")

        years = int(float(input("Enter how long u want to hold money(more than 0): ")))
        is_item_less_than_zero(years, "years")


    except Exception as exc:
        print(exc)
    else:
        print(f"{'YEARS':<10}{'VALUE':<5}")
        for year in range(1, years + 1):
                value *= 1 + (percent / 100)
                print(f"{year:<10}{round(value, 2):<5}")
main()
