# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. 
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся 
# карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

n = int(input("Введите n:"))
s = n * (n + 1) / 2
i = 1
tmp = 0
while i < n:
    k = int(input("Введите число:"))
    tmp += k
    i += 1
print("отсутствует:", int(s - tmp))
