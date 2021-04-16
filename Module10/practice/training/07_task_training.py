# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
import random

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(str(random.randint(10 ** 20000, 10 ** 20001 - 1)))
