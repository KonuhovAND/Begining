import datetime
from pprint import pprint

""" Напишите программу, которая проверяла бы
    корректность сгенерированных дат. Основной функцией
    программы должна быть функция check_dates(*dates), которая
    принимает на вход произвольное количество дат от
    пользователя.
    В конце работы функция должна вернуть список всех
    корректных дат, а также их количество, самую раннюю и самую
    позднюю дату, список будущих дат относительно текущего дня.
    Если же функция встретила некорректную дату, но она должна
    пропустить её и вывести на консоль соответствующее
    предупреждение """


def check_dates(*dates):
    """
    DD.MM.YYYY
    """
    valid_dates = []
    future_dates = []
    current_date = datetime.datetime.now()
    for date in dates:
        try:
            day,month,year = map(int,date.split('.'))
            new_date = datetime.datetime(year=year,month=month,day=day)
            valid_dates.append(new_date)
            
            if new_date > current_date:
                future_dates.append(new_date) 
        except (ValueError,AttributeError) as er:
            print( f"{date} - is not valid{str(er)}")
    if valid_dates:
        valid_dates_str = [date.strftime('%d.%m.%y') for date in valid_dates]
        future_dates_str = [date.strftime('%d.%m.%y') for date in future_dates]
        pprint(f"All valid dates + {valid_dates_str}")
        pprint(f"All future dates - {future_dates_str}")
        print(f"Самая раняя дата - {min(valid_dates).strftime("%d.%m.%Y")},самая поздняя дата - {max(valid_dates).strftime("%d.%m.%Y")}")
        print(f"коли-во дат - {len(valid_dates_str)}")
    else:
        print('No valid dates found!')
    return valid_dates


def main():
    
    try:
        n = int(input("Введите кол-во дней для анализа"))
        if n<=0:
            raise ValueError
    except ValueError:
        print("Please, enter positive number")
        n = int(input("Введите кол-во дней для анализа"))
    print(r"""DD.MM.YYYY""")
    dates = []
    for day in range(n):
        date = input('Enter day: ')
        dates.append(date)
    check_dates(*dates)
main()