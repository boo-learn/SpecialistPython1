# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
N = int(input('Введите номер максимальной карточки:'))
sum = N
i = 1
while i < N-1:
    sum += int(input('Введите номер карточки:'))
    i += 1
print("Потерянная карточка", int(N*(N+1)/2-sum))

