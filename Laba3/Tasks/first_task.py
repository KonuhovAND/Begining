ticket = input("Введите шестизначный номер билета: ")

if len(ticket) == 6:
    first_half = sum(int(digit) for digit in ticket[:3])
    second_half = sum(int(digit) for digit in ticket[3:])
    if first_half == second_half:
        print("Счастливый билет!")
    else:
        print("Обычный билет.")
else:
    print("Ошибка: нужно ввести шестизначное число.")
