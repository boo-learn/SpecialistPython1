# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.

def run():
    numbers = get_numbers()
    min_positive = get_min_positive(numbers)
    print(min_positive)

def get_numbers():
    try:
        input_str = input('Введите несколько чисел, разделяя пробелом (пример: 1 2 3 4 -7 8 5): ')
        return [int(num_str) for num_str in input_str.split(' ') if len(num_str) > 0]
    except Exception as error:
        print(f'Ошибка во время разбора входных данных: {error}')
        return get_numbers()

def get_min_positive(numbers):
    return min(filter(lambda num: num > 0, numbers))

run()
