

n = int(input("Введите количество чисел Фибоначчи: "))

def fibanachi_numbers(n):
    fib = [0,1, 1]
    for i in range(2, n):
        fib.append(fib[i] + fib[i - 1])

    print("Первые", n, "(чисел Фибоначчи:")
    print(fib[:n])
fibanachi_numbers(n=n)