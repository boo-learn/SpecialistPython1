# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    numbers = tuple(map(int, str(ticket_number)))
    rev_numbers = tuple(reversed(numbers))
    return sum(numbers[:len(numbers)//2]) == sum(rev_numbers[:len(rev_numbers)//2])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
