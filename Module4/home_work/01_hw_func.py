# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    str_tn = str(ticket_number)
    l_tn = len(str_tn)
    #if l_tn%2 == 0:
    for i in range(int(l_tn/2)):
        sum1 += int(str_tn[i])
        sum2 += int(str_tn[l_tn - i - 1])
    return sum1 == sum2


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
