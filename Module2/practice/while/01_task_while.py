# Даны два целые числа a и b. Выведите на экран все целые четные числа от a до b включительно.
# Формат входных данных: Дано два целых числа a и b. Гарантируется, что a < b
# Формат выходных данных: Выведите все числа, требуемые по условию задачи.

a = int(input("Введите число 1 : "))
b = int(input("Введите число 2 : "))

while a <= b:
    a += 1
    print (a-1)
