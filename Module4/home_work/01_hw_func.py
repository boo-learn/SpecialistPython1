# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):

    a = list(map(int, str(ticket_number)))
    if len(a) == 6:
        if a[0] + a[1] + a[2] == a[3] + a[4] + a[5]:
            return "Счастливый"

    return "НЕсчастливый"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
