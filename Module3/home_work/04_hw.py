# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
import random
numbers = []
n = int(input("Введите  n:"))
for i in range(0, n):
    numbers.append(random.randint(-100,100))
print("numbers:", numbers)
new = []
for sqrt in numbers:
    if sqrt > 0 and (sqrt ** 0.5).is_integer():
        new.append(int(sqrt ** 0.5))
print("new:", new)
