# Даны два целые числа a и b. Выведите на экран все целые четные числа от a до b включительно.
# Формат входных данных: Дано два целых числа a и b. Гарантируется, что a < b
# Формат выходных данных: Выведите все числа, требуемые по условию задачи.

# TODO: your code here

a = int(input("a = "))
b = int(input("b = "))
if not a < b:
    print("error")

if a % 2 == 0:
    i = a    
else:
    i = a + 1

while i <= b:
    print(i)
    i += 2
