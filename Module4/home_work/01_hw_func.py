# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
def num_to_digits_sequence(num):
    '''
    Генератор преобразует число в последовательность цифр, начиная с последней цифры и двигаясь к началу
    1234 --> 4, 3, 2, 1
    :param num: Целое число
    :return:
    '''
    while num:
        digit = int(num % 10)
        num //= 10
        yield digit


def lucky_ticket(ticket_number):
    # Решение со строками
    if 0:
        pass
        string = str(ticket_number)
        digits = tuple(map(int, string))
        return  sum(digits[:3]) == sum(digits[3:])

    # экзотика с использованием генератора
    if 1:
        pass
        digits = tuple(num_to_digits_sequence(ticket_number))
        return sum(digits[:3]) == sum(digits[3:])


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123005))
print(lucky_ticket(123321))
print(lucky_ticket(436751))
