"""Практическое занятие № 7, вариант 11, задача 2."""

path = input("Введите полный путь к файлу: ")
print("Исходная строка:", path)

if len(path) >= 2 and path[1] == ":":
    path_without_disk = path[2:]
else:
    path_without_disk = path

parts = path_without_disk.strip("\\").split("\\")
if len(parts) > 1 and parts[0]:
    first_folder = parts[0]
else:
    first_folder = "\\"

print("Результирующая строка:", first_folder)
