"""Анализ программы со списком символов."""

import random

list_4 = []
n = int(input("Введите размер массива: "))
for _ in range(n):
    list_4.append(chr(random.randint(45, 100)))

print("Исходный массив:")
print(list_4)
count = 0
for symbol in list_4:
    if symbol.isalpha():
        count += 1
print("Количество букв:", count)
new_string = "".join(list_4)
result = new_string.lower()
print("Исходная строка:", new_string)
print("Строка в нижнем регистре:", result)
