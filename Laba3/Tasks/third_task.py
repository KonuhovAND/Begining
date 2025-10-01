text = input("Введите строку: ")
k = int(input("Введите сдвиг: "))

result = ""
for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        shifted = (ord(char) - start + k) % 26 - start
        result += chr(shifted)
    else:
        result += char

print("Зашифрованный текст:", result)
