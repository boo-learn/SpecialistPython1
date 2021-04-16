# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию.
# Найдите:
# 1. Количество элементов списка не превышающие 10
# 2. Сумму всех положительных элементов списка
# 3. Среднее арифметическое всех четных элементов

import random
size = 10
lst = [random.randint(-10,20) for _ in range(size)]
print(lst)

# 1
count = 0
for el in lst:
    if el > 10:
        count += 1
print(count)

# 2

lst2 = sum([el for el in lst if el > 0])
print(lst2)

# 3

lst3 = [el for el in lst if el % 2 == 0]
res = sum(lst3)/len(lst3)
print(res)
