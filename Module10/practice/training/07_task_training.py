# Напишите программу генерирующую и записывающую в файле произвольное 20000-значное целое число.
import random

str_num = [str(random.randint(1, 9))] # Первый элемент не может быть нулём
str_num.extend([str(random.randint(0, 9)) for _ in range(20000 - 1)]) # Досыпаем остальных в массив
with open('num_dump.txt', 'w') as file:
    file.write(''.join(str_num)) # Объеденяем и сохраняем
