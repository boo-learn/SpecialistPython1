# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum_start = sum(map(int, str(ticket_number)[0:3]))  # Посчитал сумму первых трех цифр
    sum_end = sum(map(int, str(ticket_number)[-3:]))    # Посчитал сумму последних трех цифр
    if sum_start == sum_end:
        return True
    return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(111112))
