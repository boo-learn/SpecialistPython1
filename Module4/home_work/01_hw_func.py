# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    numbers = [int(digit) for digit in str(ticket_number)]
    if len(numbers) % 2 != 0:
        return False
    half_len = len(numbers) // 2
    return sum(numbers[:half_len]) == sum(numbers[half_len:])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(43700))
