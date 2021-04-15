# Дана строка из пяти целых чисел, разделенных пробелом.
# Пример входных данных: "2 12 -45 7 10"
# Напишите программу, которая находит среди них минимальное положительное число.
# Если таких чисел несколько - вывести любое из них.

# При решении задачи требуется учесть формат входных данных.
# Если входные данные некорректные, сообщить об этом.
import sys

while True:
    str_input = input("строка из пяти целых чисел, разделенных пробелом: ")
    str_numbers = str_input.split()
    try:
        numbers = [int(x) for x in str_numbers]
        if len(numbers) != 5:
            raise ValueError
        break
    except (ValueError, TypeError):
        print("неверный ввод")
    except Exception as e:
        print(e)
        sys.exit()

try:
    print( min([x for x in numbers if x > 0]) )
except ValueError:
    print("Нет подходящих чисел")
