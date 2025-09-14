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


def stats_calculator(*args, mode=""):
    if mode == "basic":
        print(f"Max - {max(*args)}, min - {min(*args)}, avg - {st.mean(*args)}")
    elif mode == "advanced":
        print(f"Max - {max(*args)}, min - {min(*args)}, avg - {st.mean(*args)}")
        print(f"Median - {st.median(*args)},moda - {st.mode(*args)}")
    elif mode == "scientific":
        print(f"Max - {max(*args)}, min - {min(*args)}, avg - {st.mean(*args)}")
        print(f"Median - {st.median(*args)},moda - {st.mode(*args)}")
        print(f"")