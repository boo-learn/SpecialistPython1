# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    number1 = ticket_number // 1000
    number2 = 0
    inter_number = 0
    sum1 = 0
    sum2 = 0
    x = 0
    y = 0
    while x < 3:
        inter_number = number1 % 10
        number1 //= 10
        sum1 += number3
        x += 1
    while y < 3:
        number2 = ticket_number % 10
        ticket_number //= 10
        sum2 += number2
        y += 1
    if sum1 == sum2:
        return True
    return False
# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(481301))
#думаю, что можно сделать и гораздо короче, но я придумал только так
