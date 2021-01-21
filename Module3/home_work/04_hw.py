
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]

# Для создания входных данных используем решение из задачи 2
import random

n = int(input('Введите количество элементов: '))
numbers = []
i = 0
while i < n:
    numbers.append(random.randint(-100, 100))
    i += 1
print(numbers)     # Отладка
# Чтобы наверняка в списке были нужные числа
#numbers.append(25)
#numbers.append(1)
#numbers.append(4)

sq_root_numbers = []
for number in numbers:
    if number > 0:
        sq_root = number ** (0.5)
        if sq_root % 1 == 0:
            sq_root_numbers.append(int(sq_root))

print(sq_root_numbers)
