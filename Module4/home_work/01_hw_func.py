# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    str1 = ticket_str[:3]
    str2 = ticket_str[3:]
    sum1=0
    for element in str1:
        sum1 = sum1 + int(element)
    sum2=0
    for element in str2:
        sum2 = sum2 + int(element)

    return sum1 == sum2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
