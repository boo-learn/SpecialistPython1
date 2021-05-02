# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

n_initial = int(input("Please input the number of cards: "))
n_remaining=0
n=0
i = 1
j = 1
while j <= n_initial:
    n+=j
    j+=1
while i<=(n_initial-1):
    n_n = int( input("Please input the numbers of the remaining cards: "))
    n_remaining = n_remaining + n_n
    i+=1
n_lost = n - n_remaining
print("you lost your card number ", n_lost)
