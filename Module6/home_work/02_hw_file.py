# Дан файл data/info.txt, в каждой строке которого содержится строка или целое число
# Найдите сумму всех чисел, пропуская все строки содержащие не числовые значения

with open("data/info.txt", "r") as f:
    # Строчки читаются из файла со знаком переноса строки.
    # Поэтому, в генераторе, перед парсингом int(), очищаем каждую с помощью метода strip()
    numbers = [int(clean_line) for clean_line in [raw_line.strip() for raw_line in f.readlines()] if clean_line.isdigit()]
    total = sum(numbers)
    print(total)
