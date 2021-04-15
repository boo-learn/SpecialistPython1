# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    n_left = ticket_number // 1000
    n_right = ticket_number % 1000
    sum_left = n_left // 100 + (n_left // 10) % 10 + n_left % 10
    sum_right = n_right // 100 + (n_right // 10) % 10 + n_right % 10
    print(n_left, sum_left, n_right, sum_right)
    return sum_left == sum_right


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
