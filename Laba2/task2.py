# Напишите программу, которая бы проводила
# несложные статистические вычисления по запросу
# пользователя. Основной функцией программы должна быть
# функция stats_calculator(*args, mode=”basic”).
# Функция stats_calculator принимает на вход произвольное
# количество чисел для последующего анализа, а также аргумент
# mode (по умолчанию ”basic”), который определяет её режим
# работы в соответствии со следующей таблицей:
# mode что надо вычислить
#
# basic максимум, минимум, среднее арифметическое
# advanced всё, что в basic, а также медиану и моду
# scientific всё, что в advanced, а также среднее
# геометрическое и среднее гармоническое.
# Возможно, для решения этой задачи вам понадобиться изучить
# модуль статистик
import statistics as st
import re


def basic(*args):
    print(f"Max - {max(args)}, min - {min(args)}, avg - {st.mean(args)}")


def advanced(*args):
    basic(*args)
    print(f"Median - {st.median(args)},moda - {st.mode(args)}")


def scientific(*args):
    advanced(*args)
    print(f"Avg geom - {st.geometric_mean(args)}, avg harmonic - {st.harmonic_mean(args)}")


def stats_calculator(*args, mode):
    if mode == "bs":
        basic(*args)
    elif mode == "ad":
        advanced(*args)
    elif mode == "sc":
        scientific(*args)


def main():
    try:
        data = list(map(float, (input('Enter data to analyze: ')).split()))
    except ValueError as verr:
        print(f"{verr}\nPlese,enter valid data [1,1.5,12]")
        data = list(map(float, (input('Enter data to analyze: ')).split()))
    try:
        mode = input("""Enter mode to operations \n1)basic(bs)\n2)advanced (ad)\n3)scientific(sc): """)
    except ValueError as verr:
        print(f"{verr}\n Please correct mode")
        mode = str(input(r"""Enter mode to operations 1)basic(bs)\n2)advanced (ad)\n3)scientific(sc)\n: """))
    stats_calculator(*data, mode=mode)


main()
