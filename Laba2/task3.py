import datetime
import colorama as cm
from pprint import pprint

def what_to_do():

    print(""" Напишите программу, которая проверяла бы
    корректность сгенерированных дат. Основной функцией
    программы должна быть функция check_dates(*dates), которая
    принимает на вход произвольное количество дат от
    пользователя.
    В конце работы функция должна вернуть список всех
    корректных дат, а также их количество, самую раннюю и самую
    позднюю дату, список будущих дат относительно текущего дня.
    Если же функция встретила некорректную дату, но она должна
    пропустить её и вывести на консоль соответствующее
    предупреждение """)


def check_dates(*dates):
    """
    DD.MM.YYYY
    """
    valid_dates = []
    for date in dates:
        try:
            day,month,year = date
            new_date = datetime.datetime(year=year,month=month,day=day)
        except ValueError:
            print(cm.Back.RED + f"{data} - is not valid")
        else:
            valid_dates.append(date)
    pprint(f"All valid dates - {valid_dates}")
    print(f"Самая раняя дата - {min(valid_dates)},самая поздняя дата - {max(valid_dates)}")
    print(f"коли-во дат - {len(valid_dates)}")
    get_today_date()

    

def get_today_date():
    today_date = datetime.today().strftime('%d-%m-%Y')
    day,month,year = datetime.today().strftime('%d %m %Y').split(' ')
    n = 0
    while n <0:
        for y in range(year,year+50):
            for m in range(month,13):
                for d in range(dy+1,31):
                    try:
                        new_date = datetime.datetime(year=y,month=m,day=d)
                        print(new_date)
                        n+=1
                    except ValueError:
                        break
                    
def main():
    print(r"""DD.MM.YYYY""")
    try:
        n = int(input("Введите кол-во дней для анализа"))