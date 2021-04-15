# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
while True:
    try:
        numbers = [int(digit) for digit in input('Введите 5 целых чисел через пробел: ').split(' ')]
        if len(numbers) != 5:
            raise ValueError
        break
    except ValueError:
        print('Необходимо ввести 5 целых чисел через пробел')

print(f'Наименьшее число {min(numbers)}')
