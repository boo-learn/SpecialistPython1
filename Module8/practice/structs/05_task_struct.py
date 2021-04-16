# Создайте словарь из строки следующим образом:
# в качестве ключей возьмите буквы строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

# Пример: для строки 'pythonist'
# Получим словарь: {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 's': 1, 'i': 1}
# Примечание: т.к. ключи неупорядочены, порядок следования ключей может быть произвольным
src_string = 'pythonist'

letters = {char: src_string.count(char) for char in src_string}
print(letters)
