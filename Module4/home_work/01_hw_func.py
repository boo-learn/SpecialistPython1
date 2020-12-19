# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
   lucky = []
    while digit > 0:
        lucky.append(digit % 10)
        digit = digit // 10
    l1 = int(lucky[0]) + int(lucky[1]) + int(lucky[2])
    l2 = int(lucky[3]) + int(lucky[4]) + int(lucky[5])
    if l1 == l2:
        return "Lucky ticket"
    else:
        return "General ticket"


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
