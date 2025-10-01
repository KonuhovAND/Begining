n = int(input("Введите количество чисел Фибоначчи: "))

fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i] + fib[i - 1])

print("Первые", n, "чисел Фибоначчи:")
print(fib[:n])
